from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render
import requests
import json
from administer.models import Services
from configuration.models import Restart_after_configuration
from .models import Elastic_search
from django.contrib import messages
from administer import context_processors, helper
from administer.helper import helper
import concurrent.futures

def index(request):
    obj = helper(request, Elastic_search)
    client = True
    context = context_processors.base_variables_all(request)

    if obj.atleast_one_client_is_installed():
        if obj.clientIsInstalledOnMaster():
            master = obj.get_active_master()
            if master:
                master_ip = master["ip"]
                port = master["web_port"]
                context["master_ip"] = master_ip
                context["client"] = client
            else:
                messages.error(request,
                               "Sorry !! due to some problem we are unable to fetch the information from server."
                               " You can perform following steps to find the problem and then restart the services."
                               "<ul>"
                               "<li> Reload after 10 seconds</li>"
                               "<li> Restart again</li>"
                               "<li> Check the log of master node</li>"
                               "<li> make there is no problem in configuration file </li> ")
                s_master = obj.get_service_master()
                if s_master:
                    context["error_in_conf_file"] = True
                    context["master_ip"] = s_master["ip"]
                    context["client"] = client
                    return render(request, 'elasticsearch/elasticsearch.html', context)
        else:
            messages.error(request, "We have encountered some problems."
                                    "Please make sure following conditions are met"
                                    "<ul>"
                                    "<li> Client is installed on master node</li>"
                                    "<li> Environment variables for all services are set properly</li>"
                                    "<li> Restart agent on master node [url here]</li>")
            context["client"] = False
            return render(request, 'elasticsearch/elasticsearch.html', context)
    else:
        messages.error(request, "Seems like no client is installed")
        context["client"] = False
        return render(request, 'elasticsearch/elasticsearch.html', context)

    all_nodes = obj.get_all_nodes()
    cursor = connection.cursor()

    node_with_client = "select e.ip from elastic_search_elastic_search as e join administer_nodes " \
                       "as n on e.ip=n.ip"

    masters_sql = "select e.*,n.hostname,n.fqdn,n.name from elastic_search_elastic_search as e join administer_nodes " \
                  "as n on e.ip=n.ip  where e.type=1"

    active_slave_with_client = "select e.*,em.*,n.hostname,n.fqdn,n.name from elastic_search_elastic_search as e join administer_nodes as n on " \
                               "e.ip=n.ip join elastic_search_metrics as em on e.id=em.node_id " \
                               "where e.type=0 and em.updated_at in (select max(updated_at) from elastic_search_metrics limit 1)"

    inactive_slave_with_client = "select e.*,n.hostname,n.fqdn,n.name from elastic_search_elastic_search as e join administer_nodes as n on " \
                                 "e.ip=n.ip where e.type=0"

    active_slave_without_client = "select e.*,em.* from elastic_search_elastic_search as e join elastic_search_metrics " \
                                  "as em on e.id=em.node_id where e.ip not in (" + node_with_client + ") " \
                                   "and e.type=0 and e.status='RUNNING' and em.updated_at in (select max(updated_at) from elastic_search_metrics limit 1)"

    inactive_slave_without_client = "select * from elastic_search_elastic_search where ip not in (" + node_with_client + ") " \
                                                                                                                         "and type=0 and status='SHUTDOWN'"

    backup_masters_list = []
    alive_datanode_list = []
    dead_datanode_list = []
    cursor.execute(masters_sql)
    masters = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    for node in masters:
        c = dict(zip(colnames, node))
        client_installed = True
        if c["ip"] not in all_nodes:
            client_installed = False

        if c["type"] == 1 and c["state"] == 1 and c["status"] == "RUNNING":
            master = c
        if c["type"] == 1 and c["state"] == 0:
            c["client_installed"] = client_installed
            backup_masters_list.append(c)

    cursor.execute(active_slave_with_client)
    nodes_with_client = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    for node in nodes_with_client:
        print(node)
        c = dict(zip(colnames, node))
        client_installed = True
        if c["ip"] not in all_nodes:
            client_installed = False
        c["client_installed"] = client_installed

        alive_datanode_list.append(c)

    # cursor.execute(inactive_slave_with_client)
    # inactive_nodes_with_client = cursor.fetchall()
    # colnames = [desc[0] for desc in cursor.description]
    # for node in inactive_nodes_with_client:
    #     c = dict(zip(colnames, node))
    #     client_installed = True
    #     if c["ip"] not in all_nodes:
    #         client_installed = False
    #     c["client_installed"] = client_installed
    #     dead_datanode_list.append(c)

    cursor.execute(active_slave_without_client)
    active_nodes_without_client = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    for node in active_nodes_without_client:
        # print(node)
        c = dict(zip(colnames, node))
        client_installed = True
        if c["ip"] not in all_nodes:
            client_installed = False
        c["client_installed"] = client_installed
        alive_datanode_list.append(c)

    # cursor.execute(inactive_slave_without_client)
    # inactive_nodes_without_client = cursor.fetchall()
    # colnames = [desc[0] for desc in cursor.description]
    # for node in inactive_nodes_without_client:
    #     c = dict(zip(colnames, node))
    #     client_installed = True
    #     if c["ip"] not in all_nodes:
    #         client_installed = False
    #
    #     c["client_installed"] = client_installed
    #     dead_datanode_list.append(c)

    service_object = Services.objects.get(name='elasticsearch')
    restart_status_checks = Restart_after_configuration.objects.filter(service_id=service_object.id).exists()
    if restart_status_checks:
        restart_status_check = Restart_after_configuration.objects.get(service_id=service_object.id)
        restart_status = restart_status_check.status
    else:
        restart_status = 0

    context["master"] = master
    context["backup_masters"] = backup_masters_list
    context["alive_datanode"] = alive_datanode_list
    context["dead_datanode"] = dead_datanode_list
    context["restart_status"] = restart_status
    context["service_id"] = service_object.id

    return render(request, 'elasticsearch/elasticsearch.html', context)


def es_stop(request, node_ip=None):
    obj = helper(request)

    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the active namenode. Please hard refresh the page and try again"}
        return JsonResponse(data)

    try:
        node = obj.get_node_data(node_ip)
        url_stop = 'http://%s:%s/es/stop/' % (node_ip, node["port"])
        return JsonResponse(obj.stop_service(url_stop))
    except Exception as e:
        data = {'success': False, 'msg': e}
        return JsonResponse(data)


def es_restart(request, node_ip=None):
    obj = helper(request)
    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the active namenode. Please hard refresh the page and try again"}
        return JsonResponse(data)
    try:
        node = obj.get_node_data(node_ip)
        url = 'http://%s:%s/es/restart/' % (node_ip, node["port"])
        data = obj.restart_service(url)
        print(data)
        return JsonResponse(data)
    except Exception as e:
        data = {'success': False, 'msg': e}
        return JsonResponse(data)


def es_all_restart(request):
    obj = helper(request, Elastic_search)
    cursor = connection.cursor()
    nodes_sql = "select e.ip,n.port from elastic_search_elastic_search as e join administer_nodes as n on " \
                "e.ip=n.ip where n.node_cluster_id='" + obj.cluster_id + "'"
    url_list=[]
    cursor.execute(nodes_sql)
    active_nodes_without_client = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    for node in active_nodes_without_client:
        c = dict(zip(colnames, node))
        url_list.append('http://%s:%s/es/restart/' % (c["ip"],c["port"]))

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:

        future_to_url = {executor.submit(requests.post(url, headers={"API-KEY": helper.get_api_key()},
                           data=json.dumps({"cluster_id": int(obj.cluster_id)})), url, 10): url for url in url_list}
        for future in concurrent.futures.as_completed(future_to_url):
            future_to_url[future]
            try:
                future.result()
            except Exception as e:
                print(e)

    Restart_after_configuration.objects.filter(service_id=obj.get_service_id("elasticsearch")).update(status=0)
    return JsonResponse({"success":1,"msg":["successfully restarted ES nodes"]})


def es_all_stop(request):
    obj = helper(request, Elastic_search)
    cursor = connection.cursor()
    nodes_sql = "select e.ip,n.port from elastic_search_elastic_search as e join administer_nodes as n on " \
                "e.ip=n.ip where n.node_cluster_id='" + obj.cluster_id + "'"

    url_list = []

    cursor.execute(nodes_sql)
    active_nodes_without_client = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    for node in active_nodes_without_client:
        c = dict(zip(colnames, node))
        url_list.append('http://%s:%s/es/stop/' % (c["ip"],c["port"]))

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:

        future_to_url = {executor.submit(requests.post(url, headers={"API-KEY": helper.get_api_key()},
                           data=json.dumps({"cluster_id": int(obj.cluster_id)})), url, 10): url for url in url_list}
        for future in concurrent.futures.as_completed(future_to_url):
            future_to_url[future]
            try:
                future.result()
            except Exception as e:
                print(e)


    data = {'success': 1, 'msg': ["successfully restarted all ES nodes"]}
    return JsonResponse(data)

