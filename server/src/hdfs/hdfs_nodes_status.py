from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render
import requests
import json
from administer.models import Services, Nodes
from django.contrib import messages
from administer import context_processors

from configuration.models import Restart_after_configuration
from hdfs.models import Hdfs
from administer.helper import helper


def index(request):
    obj = helper(request, Hdfs)
    client = True
    context = context_processors.base_variables_all(request)
    if obj.atleast_one_client_is_installed():
        if obj.clientIsInstalledOnMaster():
            master = obj.get_active_master()
            if master:
                master_ip = master["ip"]
                context["master_ip"] = master_ip
                context["master_id"] = master["id"]
                port = master["web_port"]
                context["client"] = client
            else:
                messages.error(request,
                               "Sorry !! due to some problem we are unable to fetch the information from server."
                               " You can perform following steps to find the problem and then restart the services."
                               "<ul>"
                               "<li> Reload after 10 seconds</li>"
                               "<li> Restart again</li>"
                               "<li> Check the log of Namenode and Datanode</li>"
                               "<li> make there is no problem in configuration file </li> "
                               "</ul>")
                s_master = obj.get_service_master()
                if s_master:
                    context["master_ip"] = s_master["ip"]
                    context["master_id"] = s_master["id"]
                    context["error_in_conf_file"] = True
                    context["client"] = client
                    return render(request, 'hdfs/hdfs.html', context)
        else:
            messages.error(request, "We have encountered some problems."
                                    "Please make sure following conditions are met"
                                    "<ul>"
                                    "<li> Client is installed on master node</li>"
                                    "<li> Environment variables for all services are set properly</li>"
                                    "<li> Restart agent on master node [url here]</li>")
            context["client"] = False
            return render(request, 'hdfs/hdfs.html', context)
    else:
        messages.error(request, "Seems like no client is installed")
        context["client"] = False
        return render(request, 'hdfs/hdfs.html', context)

    all_nodes = obj.get_all_nodes()
    cursor = connection.cursor()

    node_with_client = "select h.ip from hdfs_hdfs as h join administer_nodes " \
                       "as n on h.ip=n.ip "

    masters_sql = "select h.*,n.hostname,n.fqdn,n.name from hdfs_hdfs as h left outer join administer_nodes " \
                  "as n on h.ip=n.ip where h.type=1"

    slave_with_client = "select h.*,hm.*,n.hostname,n.fqdn,n.name from hdfs_hdfs as h join administer_nodes as n on " \
                        "h.ip=n.ip join hdfs_metrics as hm on h.id=hm.node_id " \
                        "where h.type=0 and hm.updated_at in (select max(updated_at) " \
                                                                       "from hdfs_metrics limit 1)"

    slave_without_client = "select h.*,hm.* from hdfs_hdfs as h join hdfs_metrics as hm on h.id=hm.node_id " \
                           "where h.type=0 and h.ip not in (" + node_with_client + ") and hm.updated_at in " \
                                                                                   "(select max(updated_at) from hdfs_metrics limit 1)"

    name_livenodes = []
    name_deadnodes = []
    standby_data = {}

    cursor.execute(masters_sql)
    masters = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    for node in masters:
        c = dict(zip(colnames, node))
        print()
        print()
        print(c)
        client_installed = True
        if c["ip"] not in all_nodes:
            client_installed = False

        if c["type"] == 1 and c["state"] == 1:
            safemode = c["safemode"]
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
            name_livenodes.append(c)
        else:
            name_deadnodes.append(c)

    cursor.execute(slave_without_client)
    nodes_without_client = cursor.fetchall()
    for node in nodes_without_client:
        c = dict(zip(colnames, node))
        client_installed = True
        if c["ip"] not in all_nodes:
            client_installed = False

        c["client_installed"] = client_installed
        if c["status"] == "RUNNING":
            name_livenodes.append(c)
        else:
            name_deadnodes.append(c)

    service_object = Services.objects.get(name='hdfs')
    restart_status_checks = Restart_after_configuration.objects.filter(service_id=service_object.id).exists()
    if restart_status_checks:
        restart_status_check = Restart_after_configuration.objects.get(service_id=service_object.id)
        restart_status = restart_status_check.status
    else:
        restart_status = 0

    context['name_livenodes'] = name_livenodes
    context['name_deadnodes'] = name_deadnodes
    context['restart_status'] = restart_status
    context['active_node'] = active_data
    context['standby_node'] = standby_data
    context["safemode"] = safemode
    context["service_id"] = service_object.id

    return render(request, 'hdfs/hdfs.html', context)


# def prepare_alive_dead_node_list(colnames, lst, all_nodes):
#     alive = []
#     dead = []
#     for node in lst:
#         c = dict(zip(colnames, node))
#         client_installed = True
#         if c["ip"] not in all_nodes:
#             client_installed = False
#
#         c["client_installed"] = client_installed
#         if node[3] == "RUNNING":
#             name_livenodes.append(c)
#         else:
#             name_deadnodes.append(c)
#
#     return alive, dead


def dn_restart(request):
    obj = helper(request)
    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the datanode. Please hard refresh the page and try again"}
        return JsonResponse(data)
    try:
        node = obj.get_node_data(node_ip)
        url = 'http://%s:%s/hadoop/datanode/restart/' % (node_ip,node["port"])
        resp = obj.restart_service(url)
        return JsonResponse(resp)
    except Exception as e:
        data = {'success': 0, 'msg': e}
        return JsonResponse(data)


def dn_stop(request):
    obj = helper(request)
    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the datanode. Please hard refresh the page and try again"}
        return JsonResponse(data)
    try:
        node = obj.get_node_data(node_ip)
        url_stop = 'http://%s:%s/hadoop/datanode/stop/' % (node_ip,node["port"])
        return JsonResponse(obj.stop_service(url_stop))
    except Exception as e:
        data = {'success': 0, 'msg': e}
        return JsonResponse(data, safe=False)


def nn_restart(request):
    obj = helper(request)
    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the active namenode. Please hard refresh the page and try again"}
        return JsonResponse(data)
    try:
        node = obj.get_node_data(node_ip)
        url = 'http://%s:%s/hadoop/namenode/restart/' % (node_ip,node["port"])
        data = obj.restart_service(url)
        return JsonResponse(data)
    except Exception as e:
        data = {'success': 0, 'msg': e.args}
        return JsonResponse(data)


def nn_stop(request):
    obj = helper(request)
    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']

    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the active namenode. Please hard refresh the page and try again"}
        return JsonResponse(data)
    try:
        node = obj.get_node_data(node_ip)
        url_stop = 'http://%s:%s/hadoop/namenode/stop/' % (node_ip,node["port"])
        data = obj.stop_service(url_stop)
        return JsonResponse(data)
    except Exception as e:
        data = {'success': 0, 'msg': e}
        return JsonResponse(data, safe=False)


def h_all_restart(request):
    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the active namenode. Please hard refresh the page and try again"}
        return JsonResponse(data)

    obj = helper(request=request, model=Hdfs)
    op_status = obj.restart_all("hadoop/dfs/restart/", master_ip=node_ip)
    if op_status["success"]:
        Restart_after_configuration.objects.filter(service_id=obj.get_service_id("hdfs")).update(status=0)
    return JsonResponse(op_status)


def h_all_stop(request):
    obj = helper(request=request, model=Hdfs)
    return JsonResponse(obj.stop_all("hadoop/dfs/stop/"))


def h_kill(request):
    obj = helper(request=request, model=Hdfs)
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
                'msg': "We are unable to get the IP of the active namenode. Please hard refresh the page and try again"}
        return JsonResponse(data)
    node = obj.get_node_data(node_ip)
    if request.POST['server_type'] is not '':
        server_type = request.POST['server_type']
        if server_type == 'NameNode':

            url_start = 'http://%s:%s/hadoop/namenode/start/' % (node_ip,node["port"])
        else:
            url_start = 'http://%s:%s/hadoop/datanode/start/' % (node_ip,node["port"])
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

    url = "http://%s:%s/command/kill/" % (node_ip,node["port"])
    try:
        payload = {"service_name": server_type, "node_id": node_id, "table_name": "hdfs_hdfs"}
        r = requests.post(url, headers={"API-KEY": helper.get_api_key()}, data=json.dumps(payload))
        if r.status_code != 200:
            return JsonResponse({'success': 0, 'msg': 'server threw status code ' + r.status_code})

        data = r.json()
        if data["success"] == 1:
            if action_type == "1":
                try:

                    r_start = requests.get(url_start, headers={"API-KEY": helper.get_api_key()},
                                           data=json.dumps({"cluster_id": int(obj.cluster_id)}))
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
