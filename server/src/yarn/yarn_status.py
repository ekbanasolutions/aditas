import json
import re
from http.client import HTTPException

from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render
import requests

from configuration.models import Restart_after_configuration
from administer.models import Nodes, Services
from django.contrib import messages
from administer import context_processors
from administer.helper import helper
from yarn.models import Yarn


def index(request):
    obj = helper(request, Yarn)
    master_ip = ""
    master = ""
    client = True
    nodemanagers = []
    context = context_processors.base_variables_all(request)
    if obj.atleast_one_client_is_installed():
        if obj.clientIsInstalledOnMaster():
            master = obj.get_active_master()
            if master:
                master_ip = master["ip"]
                context["master_ip"] = master_ip
                context["master_id"] = master["id"]
                context["client"] = client
            else:
                messages.error(request,
                               "Sorry !! due to some problem we are unable to fetch the information from server."
                               " You can perform following steps to find the problem and then restart the services."
                               "<ul>"
                               "<li> Reload after 10 seconds</li>"
                               "<li> Restart again</li>"
                               "<li> Check the log of resource manager and node manager</li>"
                               "<li> make there is no problem in configuration file </li> "
                               "</ul>")
                service_master = obj.get_service_master()
                if service_master:
                    context["error_in_conf_file"] = True
                    context["master_ip"] = service_master["ip"]
                    context["master_id"] = service_master["id"]
                    context["client"] = client
                    return render(request, 'yarn/yarn.html', context)
        else:
            messages.error(request, "We have encountered some problems."
                                    "Please make sure following conditions are met"
                                    "<ul>"
                                    "<li> Client is installed on master node</li>"
                                    "<li> Environment variables for all services are set properly</li>"
                                    "<li> Restart agent on master node [url here]</li>")
            context["client"] = False
            return render(request, 'yarn/yarn.html', context)
    else:
        messages.error(request, "Seems like no client is installed")
        context["client"] = False
        return render(request, 'yarn/yarn.html', context)

    all_nodes = obj.get_all_nodes()
    cursor = connection.cursor()

    node_with_client = "select y.ip from yarn_yarn as y join administer_nodes as n on y.ip=n.ip "

    masters_sql = "select y.*,n.hostname,n.fqdn,n.name from yarn_yarn as y join administer_nodes as n on y.ip=n.ip where y.type=1"

    slave_with_client = "select y.*,ym.*,n.hostname,n.fqdn,n.name from yarn_yarn as y join administer_nodes as n on " \
                        "y.ip=n.ip join yarn_metrics as ym on y.id=ym.node_id " \
                        "where y.type=0 and ym.updated_at in (select max(updated_at) " \
                                                                       "from yarn_metrics limit 1)"

    slave_without_client = "select y.*,ym.* from yarn_yarn as y join yarn_metrics as ym on y.id=ym.node_id " \
                           "where y.type=0 and y.ip not in (" + node_with_client + ") and ym.updated_at in" \
                           " (select max(updated_at) from yarn_metrics limit 1)"


    alive_nodemanagers = []
    dead_nodemanagers = []
    standby_data=None
    active_data=None

    cursor.execute(masters_sql)
    masters = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    for node in masters:
        c = dict(zip(colnames, node))
        client_installed = True
        if c["ip"] not in all_nodes:
            client_installed = False

        if c["type"] == 1 and c["state"] == 1:
            active_data = c
        if c["type"] == 1 and c["state"] == 0:
            c["client_installed"] = client_installed
            standby_data = c
        if c["type"] == 1 and c["state"] == 2:
            c["client_installed"] = client_installed
            standby_data = c

    cursor.execute(slave_with_client)
    nodes_with_client = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    for node in nodes_with_client:
        c = dict(zip(colnames, node))
        client_installed = True
        if c["ip"] not in all_nodes:
            client_installed = False

        c["client_installed"] = client_installed
        if c["status"] == "RUNNING":
            alive_nodemanagers.append(c)
        else:
            dead_nodemanagers.append(c)

    print(alive_nodemanagers)

    cursor.execute(slave_without_client)
    nodes_without_client = cursor.fetchall()
    for node in nodes_without_client:
        c = dict(zip(colnames, node))
        client_installed = True
        if c["ip"] not in all_nodes:
            client_installed = False
        c["client_installed"] = client_installed

        if c["status"] == "RUNNING":
            alive_nodemanagers.append(c)
        else:
            dead_nodemanagers.append(c)

    print(alive_nodemanagers)

    service_object = Services.objects.get(name='yarn')
    restart_status_checks = Restart_after_configuration.objects.filter(service_id=service_object.id).exists()
    if restart_status_checks:
        restart_status_check = Restart_after_configuration.objects.get(service_id=service_object.id)
        restart_status = restart_status_check.status
    else:
        restart_status = 0


    context["alive_nodemanagers"] = alive_nodemanagers
    context["dead_nodemanagers"] = dead_nodemanagers
    context["restart_status"] = restart_status
    context['active_node'] = active_data
    context['standby_node'] = standby_data
    context['service_id'] = service_object.id

    return render(request, 'yarn/yarn.html', context)


def y_nm_restart(request):
    obj = helper(request)
    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the active namenode. Please hard refresh the page and try again"}
        return JsonResponse(data)

    try:
        node = obj.get_node_data(node_ip)
        url = 'http://%s:%s/yarn/nm/restart/' % (node_ip, node["port"])
        return JsonResponse(obj.restart_service(url))
    except Exception as e:
        data = {'success': False, 'msg': e}
        return JsonResponse(data)


def y_nm_stop(request):
    obj = helper(request)

    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the active namenode. Please hard refresh the page and try again"}
        return JsonResponse(data)

    try:
        node = obj.get_node_data(node_ip)
        url_stop = 'http://%s:%s/yarn/nm/stop/' % (node_ip, node["port"])
        return JsonResponse(obj.stop_service(url_stop))
    except Exception as e:
        data = {'success': False, 'msg': e}
        return JsonResponse(data)


def y_rm_restart(request):
    obj = helper(request)

    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the active namenode. Please hard refresh the page and try again"}
        return JsonResponse(data)

    try:
        node = obj.get_node_data(node_ip)
        url = 'http://%s:%s/yarn/rm/restart/' % (node_ip, node["port"])
        return JsonResponse(obj.restart_service(url))
    except Exception as e:
        data = {'success': False, 'msg': e}
        return JsonResponse(data)


def y_rm_stop(request):
    obj = helper(request)

    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the active namenode. Please hard refresh the page and try again"}
        return JsonResponse(data)

    try:
        node = obj.get_node_data(node_ip)
        url_stop = 'http://%s:%s/yarn/rm/stop/' % (node_ip, node["port"])
        return JsonResponse(obj.stop_service(url_stop))
    except Exception as e:
        data = {'success': False, 'msg': e}
        return JsonResponse(data)


def y_all_restart(request):

    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': False,
                'msg': "We are unable to get the IP of the active resource manager. Please hard refresh the page and try again"}
        return JsonResponse(data)

    obj = helper(request=request, model=Yarn)
    op_status = obj.restart_all("yarn/restart/", master_ip=node_ip)
    if op_status["success"]:
        Restart_after_configuration.objects.filter(service_id=obj.get_service_id("yarn")).update(status=0)
    return JsonResponse(op_status)


def y_all_stop(request):
    obj = helper(request=request, model=Yarn)
    return JsonResponse(obj.stop_all("yarn/stop/"))

def y_kill(request):
    obj = helper(request=request, model=Yarn)
    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the active namenode. Please hard refresh the page and try again"}
        return JsonResponse(data)

    if request.POST['node_id'] is not '':
        node_id = request.POST['node_id']
    else:
        data = {'success': 0,
                'msg': "We are unable to get the id of the active namenode. Please hard refresh the page and try again"}
        return JsonResponse(data)

    node = obj.get_node_data(node_ip)

    if request.POST['server_type'] is not '':
        server_type = request.POST['server_type']
        if server_type == 'rm':
            url_start = 'http://%s:%s/yarn/rm/start/' % (node_ip, node["port"])
        else :
            url_start = 'http://%s:%s/yarn/nm/start/' % (node_ip, node["port"])
    else:
        data = {'success': 0,
                'msg': "Sorry we didnot receive some of the required data. Please hard refresh the page and try again"}
        return JsonResponse(data)

    if request.POST['action_type'] is not '':
        action_type = request.POST['action_type']
    else:
        data = {'success': 0,
                'msg': "Sorry we didnot receive some of the required data. Please hard refresh the page and try again"}
        return JsonResponse(data)

    url = "http://%s:%s/command/kill/" % (node_ip, node["port"])
    try:
        payload = {"service_name": server_type,"node_id":node_id,"table_name":"yarn_yarn"}
        r = requests.post(url, headers={"API-KEY": helper.get_api_key()}, data=json.dumps(payload))
        if r.status_code != 200:
            return JsonResponse({'success': 0, 'msg': 'server threw status code ' + r.status_code})

        data = r.json()
        print(data)
        if data["success"] == 1:
            if action_type == "1":
                try:

                    r_start = requests.get(url_start, headers={"API-KEY": helper.get_api_key()},data=json.dumps({"cluster_id":int(obj.cluster_id)}))
                    print()
                    if r_start.status_code != 200:
                        return r_start.json()

                    if r_start.json()['success'] != 1:
                        return r_start.json()
                except Exception as e:
                    data = {'success': 0, 'msg': e.args}
                    return JsonResponse(data)
        else:
            return JsonResponse(data)
    except ConnectionError as e:
        data = {'success': 0, 'msg': e}
    return JsonResponse(data)
