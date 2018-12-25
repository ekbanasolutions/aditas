from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render
import requests

from configuration.models import Restart_after_configuration
from .models import Spark
from administer.models import Services
from django.contrib import messages
from administer import context_processors,helper
from administer.helper import helper
from requests.exceptions import ConnectionError


def index(request):
    obj = helper(request, Spark)
    master_ip = ""
    client = True
    master=""
    context = context_processors.base_variables_all(request)
    if obj.atleast_one_client_is_installed():
        if obj.clientIsInstalledOnMaster():
            master = obj.get_active_master()
            if master:
                master_ip = master["ip"]
                context["client"] = client
            else:
                messages.error(request,
                               "Sorry !! due to some problem we are unable to fetch the information from server."
                               " You can perform following steps to find the problem and then restart the services."
                               "<ul>"
                               "<li> Reload after 10 seconds</li>"
                               "<li> Restart again</li>"
                               "<li> Check the log of spark master and spark worker</li>"
                               "<li> make there is no problem in configuration file </li> ")
                context["error_in_conf_file"] = True
                s_master = obj.get_service_master()
                if s_master:
                    context["master_ip"] = s_master["ip"]
                    context["client"] = client
                    return render(request, 'spark/spark.html', context)
        else:
            messages.error(request, "We have encountered some problems."
                                    "Please make sure following conditions are met"
                                    "<ul>"
                                    "<li> Client is installed on master node</li>"
                                    "<li> Environment variables for all services are set properly</li>"
                                    "<li> Restart agent on master node [url here]</li>")
            context["client"] = False
            return render(request, 'spark/spark.html', context)
    else:
        messages.error(request, "Seems like no client is installed")
        context["client"] = False
        return render(request, 'spark/spark.html', context)

    all_nodes = obj.get_all_nodes()
    cursor = connection.cursor()

    node_with_client = "select s.ip from spark_spark as s join administer_nodes " \
                       "as n on s.ip=n.ip"

    masters_sql = "select s.*,n.hostname,n.fqdn,n.name from spark_spark as s join administer_nodes " \
                  "as n on s.ip=n.ip where s.type=1"

    slave_with_client = "select s.*,sm.*,n.hostname,n.fqdn,n.name from spark_spark as s join administer_nodes as n on " \
                        "s.ip=n.ip join spark_metrics as sm on s.id=sm.node_id " \
                        " where s.type=0 and sm.updated_at in (select max(updated_at) " \
                                                                       "from spark_metrics limit 1)"

    slave_without_client = "select s.*,sm.* from spark_spark as s join spark_metrics as sm on s.id=sm.node_id " \
                           "where s.type=0 and s.ip not in (" + node_with_client + ") and sm.updated_at in" \
                           " (select max(updated_at) from spark_metrics limit 1)"

    alive_workers_list = []
    dead_workers_list = []

    cursor.execute(masters_sql)
    masters = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    for node in masters:
        c = dict(zip(colnames, node))
        client_installed = True
        if c["ip"] not in all_nodes:
            client_installed = False

        if c["type"] == 1 and c["state"] == 1:
            master = c
        if c["type"] == 1 == 1 and c["state"] == 0:
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
            alive_workers_list.append(c)
        else:
            dead_workers_list.append(c)

    cursor.execute(slave_without_client)
    nodes_without_client = cursor.fetchall()

    for node in nodes_without_client:
        c = dict(zip(colnames, node))
        client_installed = True
        if c["ip"] not in all_nodes:
            client_installed = False

        c["client_installed"] = client_installed
        if c["status"] == "RUNNING":
            alive_workers_list.append(c)
        else:
            dead_workers_list.append(c)

    service_object = Services.objects.get(name='spark')
    restart_status_checks = Restart_after_configuration.objects.filter(service_id=service_object.id).exists()
    if restart_status_checks:
        restart_status_check = Restart_after_configuration.objects.get(service_id=service_object.id)
        restart_status = restart_status_check.status
    else:
        restart_status = 0

    context["alive_spark_workers"]=alive_workers_list
    context["dead_spark_workers"]=dead_workers_list
    context["restart_status"]=restart_status
    context["spark_master"]=master
    context["master_ip"] = master_ip
    context["service_id"] = service_object.id
    return render(request, 'spark/spark.html', context)


def sw_restart(request):
    obj = helper(request=request, model=Spark)
    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the active namenode. Please hard refresh the page and try again"}
        return JsonResponse(data)
    try:
        node = obj.get_node_data(node_ip)
        url = 'http://%s:%s/spark/slave/restart/' % (node_ip,node["port"])
        return JsonResponse(obj.restart_special_service(url))
    except Exception as e:
        data = {'success': False, 'msg': e}
        return JsonResponse(data)


def sw_stop(request):
    obj = helper(request=request, model=Spark)
    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the active namenode. Please hard refresh the page and try again"}
        return JsonResponse(data)

    try:
        node = obj.get_node_data(node_ip)
        url_stop = 'http://%s:%s/spark/slave/stop/' % (node_ip,node["port"])
        return JsonResponse(obj.stop_special_service(url_stop))
    except Exception as e:
        data = {'success': False, 'msg': e}
        return JsonResponse(data)


def sm_restart(request):
    obj = helper(request=request, model=Spark)
    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the active namenode. Please hard refresh the page and try again"}
        return JsonResponse(data)

    try:
        node = obj.get_node_data(node_ip)
        url_stop = 'http://%s:%s/spark/master/stop/' % (node_ip,node["port"])
        url_start = 'http://%s:%s/spark/master/start/' % (node_ip,node["port"])
        return JsonResponse(obj.restart_special_service(url_stop, url_start))
    except Exception as e:
        data = {'success': False, 'msg': e}
        return JsonResponse(data)


def sm_stop(request):
    obj = helper(request=request, model=Spark)
    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': 0,
                'msg': "We are unable to get the IP of the active namenode. Please hard refresh the page and try again"}
        return JsonResponse(data)

    try:
        node = obj.get_node_data(node_ip)
        url_stop = 'http://%s:%s/spark/master/stop/' % (node_ip,node["port"])
        return JsonResponse(obj.stop_special_service(url_stop))
    except Exception as e:
        data = {'success': False, 'msg': e}
        return JsonResponse(data)


def s_all_restart(request):
    if request.POST['node_ip'] is not '':
        node_ip = request.POST['node_ip']
    else:
        data = {'success': False, 'msg': "We are unable to get the IP of the active namenode. Please hard refresh the page and try again"}
        return JsonResponse(data)
    obj = helper(request=request, model=Spark)
    op_status = obj.restart_all("spark/restart/",master_ip=node_ip)
    if op_status["success"]:
        Restart_after_configuration.objects.filter(service_id=obj.get_service_id("spark")).update(status=0)
    return JsonResponse(op_status)


def s_all_stop(request):
    obj = helper(request=request, model=Spark)
    return JsonResponse(obj.stop_all("spark/stop/"))

