import ast
import json

from django.http import JsonResponse
from django.shortcuts import render
import requests
from administer.models import Nodes, Services
from django.db import connection
from django.contrib import messages
from administer import context_processors, helper
from configuration.models import Restart_after_configuration
from hbase.models import Hbase
from administer.helper import helper


def index(request):
    obj = helper(request, Hbase)
    master_ip = ""
    client = True
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
                               "<li> Check the log of Hmaster and RegionServers</li>"
                               "<li> Check the log of Namenode and Datanode</li>"
                               "<li> make there is no problem in configuration file </li> "
                               "</ul>")
                service_master = obj.get_service_master()
                if service_master:
                    context["error_in_conf_file"] = True
                    context["master_ip"] = service_master["ip"]
                    context["master_id"] = service_master["id"]
                    context["client"] = client
                    return render(request, 'hbase/hbase.html', context)
        else:
            messages.error(request, "We have encountered some problems."
                                    "Please make sure following conditions are met"
                                    "<ul>"
                                    "<li> Client is installed on master node</li>"
                                    "<li> Environment variables for all services are set properly</li>"
                                    "<li> Restart agent on master node [url here]</li>")
            context["client"] = False
            return render(request, 'hbase/hbase.html', context)
    else:
        messages.error(request, "Seems like no client is installed")
        context["client"] = False
        return render(request, 'hbase/hbase.html', context)

    all_nodes = obj.get_all_nodes()
    cursor = connection.cursor()

    node_with_client = "select hb.ip from hbase_hbase as hb join administer_nodes " \
                       "as n on hb.ip=n.ip"

    masters_sql = "select hb.*,n.hostname,n.fqdn,n.name from hbase_hbase as hb join administer_nodes " \
                  "as n on hb.ip=n.ip where hb.type=1"

    slave_with_client = "select h.*,hbm.*,n.hostname,n.fqdn,n.name from hbase_hbase as h join administer_nodes as n on " \
                        "h.ip=n.ip join hbase_metrics as hbm on h.id=hbm.node_id " \
                        "where h.type=0 and hbm.updated_at in (select max(updated_at) " \
                                                                       "from hbase_metrics limit 1)"

    slave_without_client = "select h.*,hbm.* from hbase_hbase as h join hbase_metrics as hbm on h.id=hbm.node_id " \
                           "where h.type=0 and h.ip not in (" + node_with_client + ") and hbm.updated_at in (select max(updated_at) from hbase_metrics limit 1)"

    live_regionservers_list = []
    dead_regionservers_list = []
    active_data = ""
    backup_data = ""

    cursor.execute(masters_sql)
    masters = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    for node in masters:
        print(node)
        c = dict(zip(colnames, node))
        client_installed = True
        if c["ip"] not in all_nodes:
            client_installed = False

        if c["type"] == 1 and c["state"] == 1:
            active_data = c
        if c["type"] == 1 and c["state"] == 0:
            c["client_installed"] = client_installed
            backup_data = c

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
            live_regionservers_list.append(c)
        else:
            dead_regionservers_list.append(c)

    cursor.execute(slave_without_client)
    nodes_without_client = cursor.fetchall()

    for node in nodes_without_client:
        c = dict(zip(colnames, node))
        client_installed = True
        if c["ip"] not in all_nodes:
            client_installed = False

        c["client_installed"] = client_installed
        if c["status"] == "RUNNING":
            live_regionservers_list.append(c)
        else:
            dead_regionservers_list.append(c)

    tst = {"k1": "v1", "k2": "v2", "k3": "v3"}
    # tst = 'bibek'

    service_object = Services.objects.get(name='hbase')
    restart_status_checks = Restart_after_configuration.objects.filter(service_id=service_object.id).exists()
    if restart_status_checks:
        restart_status_check = Restart_after_configuration.objects.get(service_id=service_object.id)
        restart_status = restart_status_check.status
    else:
        restart_status = 0

    context["live_regionservers"] = live_regionservers_list
    context["dead_regionservers"] = dead_regionservers_list
    context["active_master"] = active_data
    context["backup_master"] = backup_data
    context["restart_status"] = restart_status
    context["service_id"] = service_object.id

    return render(request, 'hbase/hbase.html', context)


def h_rs_restart(request):
    obj = helper(request=request, model=Hbase)
    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the active hmaster. Please hard refresh the page and try again"}
        return JsonResponse(data)
    try:
        node = obj.get_node_data(node_ip)
        # node_ip = request.POST['node_ip']
        url = 'http://%s:%s/hbase/regionserver/restart/' % (node_ip, node["port"])
        return JsonResponse(obj.restart_service(url))
    except Exception as e:
        data = {'success': False, 'msg': e}
        return JsonResponse(data)


def h_rs_stop(request):
    obj = helper(request=request, model=Hbase)
    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the active hmaster. Please hard refresh the page and try again"}
        return JsonResponse(data)
    try:
        node = obj.get_node_data(node_ip)
        # node_ip = request.POST['node_ip']
        url_stop = 'http://%s:%s/hbase/regionserver/stop/' % (node_ip, node["port"])
        return JsonResponse(obj.stop_service(url_stop))
    except Exception as e:
        data = {'success': False, 'msg': e}
        return JsonResponse(data)


def h_hm_restart(request):
    obj = helper(request=request, model=Hbase)
    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the active hmaster. Please hard refresh the page and try again"}
        return JsonResponse(data)
    try:
        node = obj.get_node_data(node_ip)
        # node_ip = request.POST['node_ip']
        url = 'http://%s:%s/hbase/master/restart/' % (node_ip, node["port"])
        return JsonResponse(obj.restart_service(url))
    except Exception as e:
        data = {'success': False, 'msg': e}
        return JsonResponse(data)


def h_hm_stop(request):
    obj = helper(request=request, model=Hbase)
    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']

    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the active namenode. Please hard refresh the page and try again"}
        return JsonResponse(data)
    try:
        node = obj.get_node_data(node_ip)
        url_stop = 'http://%s:%s/hbase/master/stop/' % (node_ip, node["port"])
        resp = obj.stop_service(url_stop)
        print(resp)
        return JsonResponse(resp)
    except Exception as e:
        data = {'success': False, 'msg': e}
        return JsonResponse(data)


def hb_all_restart(request):
    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': False,
                'msg': "We are unable to get the IP of the active namenode. Please hard refresh the page and try again"}
        return JsonResponse(data)
    obj = helper(request=request, model=Hbase)
    op_status = obj.restart_all("hbase/restart/", master_ip=node_ip)
    print(op_status)
    if op_status["success"]:
        Restart_after_configuration.objects.filter(service_id=obj.get_service_id("hbase")).update(status=0)
    return JsonResponse(op_status)


def hb_all_stop(request):
    obj = helper(request=request, model=Hbase)
    return JsonResponse(obj.stop_all("hbase/stop/"))


def h_kill(request):
    obj = helper(request=request, model=Hbase)
    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the active namenode. Please hard refresh the page and try again"}
        return JsonResponse(data)

    node = obj.get_node_data(node_ip)
    if request.POST['server_type'] is not '':
        server_type = request.POST['server_type']
        if server_type == 'HMaster':
            url_start = 'http://%s:%s/hbase/master/start/' % (node_ip, node["port"])
        else:
            url_start = 'http://%s:%s/hbase/regionserver/start/' % (node_ip, node["port"])
    else:
        data = {'success': 0,
                'msg': "Sorry we didnot receive some of the required data. Please hard refresh the page and try again"}
        return JsonResponse(data)

    if request.POST['node_id'] is not '':
        node_id = request.POST['node_id']
    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the active namenode. Please hard refresh the page and try again"}
        return JsonResponse(data)

    if request.POST['action_type'] is not '':
        action_type = request.POST['action_type']
        print(" 208 action type = %s " % action_type)
    else:
        data = {'success': 0,
                'msg': "Sorry we did not receive some of the required data. Please hard refresh the page and try again"}
        return JsonResponse(data)

    url = "http://%s:%s/command/kill/" % (node_ip, node["port"])
    try:
        payload = {"service_name": server_type, "node_id": node_id, "table_name": "hbase_hbase"}
        r = requests.post(url, headers={"API-KEY": helper.get_api_key()},
                          data=json.dumps(payload))
        if r.status_code != 200:
            return JsonResponse({'success': 0, 'msg': 'server threw status code ' + r.status_code})

        data = ast.literal_eval(r.content.decode())
        # data = r.json()
        if data["success"] == 1:
            if action_type == "1":
                try:
                    r_start = requests.post(url_start, headers={"API-KEY": helper.get_api_key()},
                                            data=json.dumps({"cluster_id": int(obj.cluster_id)}))
                    print(r_start.status_code)
                    if r_start.status_code != 200:
                        return JsonResponse(r_start.json())

                    if r_start.json()['success'] != 1:
                        return JsonResponse(r_start.json())

                except Exception as e:
                    data = {'success': 0, 'msg': e.args}
                    return JsonResponse(data)
        else:
            return JsonResponse(data, False)
    except ConnectionError as e:
        data = {'success': 0, 'msg': e}
    return JsonResponse(data)
