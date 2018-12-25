import json
import os
import sys


import run_services
from API_KEYS.keys import check_apiKey
from Basic_linux_commands.kill_service import kill_service
from System_Info.hostname_info import get_system_ip
from bigdata_logs.logger import getLoggingInstance
from custom_requests import request

log = getLoggingInstance()

parent_dir = os.getenv("parent_dir")
sys.path.append(parent_dir)

user_pass = os.getenv("user_pass")

es_bin_dir = os.getenv("es_bin_dir")

es_status_systemd_cmd = "echo %s | sudo -S systemctl status elasticsearch" % user_pass
es_start_systemd_cmd = "echo %s | sudo -S systemctl start elasticsearch" % user_pass
es_stop_systemd_cmd = "echo %s | sudo -S systemctl stop elasticsearch" % user_pass

es_status_sysvinit_cmd = "echo %s | sudo -S service elasticsearch status" % user_pass
es_start_sysvinit_cmd = "echo %s | sudo -S service elasticsearch start" % user_pass
es_stop_sysvinit_cmd = "echo %s | sudo -S service elasticsearch stop" % user_pass

es_start_bin_cmd = "cd %s ./elasticsearch &>/dev/null &" % es_bin_dir


def es_home():
    '''
    :return: Returns Urls for ElasticSearch services
    '''
    path = "Urls for ElasticSearch services:\n\
            '/start/': 'elasticsearch_start'\n\
            '/stop/': 'elasticsearch_stop'\n\
            '/restart/': 'elasticsearch_restart'"

    return path


def check_es_exists(cmd):
    result = None
    try:
        result = os.popen(cmd)
        result = (result.read()).split("\n")
        for r in result:
            if r.__contains__("Loaded"):
                status = r.split(":")
                if (status[1]).__contains__("not-found"):
                    return False
                else:
                    return True
    except Exception as e:
        log.error("Error while checking if es exists!!!")
        log.error(result, e)


def get_es_process_name():
    if check_es_exists(es_status_systemd_cmd):
        return "systemd"
    elif check_es_exists(es_status_sysvinit_cmd):
        return "sysv_init"
    else:
        return "bin"


def elasticsearch_start():
    '''
    Starts 
    :return: Returns success if es_start_cmd command executes successfully or error message is shown
    '''
    log.info("\nStarting elasticsearch\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        return es_start(cluster_id)
    else:
        return api_status


def es_start(cluster_id):
    ip = get_system_ip()
    sql = "select id, status, web_port, rpyc_port from elastic_search_elastic_search where ip='%s' and cluster_id=%d" % (ip, cluster_id)
    rs = run_services.get_service_status(sql)
    id = rs[0]
    status = rs[1]
    web_port = rs[2]
    rpyc_port = rs[3]
    if status != "RUNNING":
        es_process_name = get_es_process_name()
        es_start_cmd = es_start_systemd_cmd if es_process_name == "systemd" else es_start_sysvinit_cmd if es_process_name == "sysv_init" else es_start_bin_cmd
        result = run_services.run_bigdata_services(es_start_cmd, 'ES Started',
                                                   'Error Starting ES')
        return run_services.confirm_start(result, "elastic_search_elastic_search", id, web_port, rpyc_port)
    else:
        return '{"success": 1, "msg": ["ES Already Running!!!"]}'


def elasticsearch_stop():
    '''
    Stops
    :return: Returns success if es_stop_cmd command executes successfully or error message is shown
    '''
    log.info("\nStopping elasticsearch\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        return es_stop(cluster_id)
    else:
        return api_status


def es_stop(cluster_id):
    ip = get_system_ip()
    sql = "select id, status, web_port, rpyc_port from elastic_search_elastic_search where ip='%s' and cluster_id=%d" % (ip, cluster_id)
    rs = run_services.get_service_status(sql)
    id = rs[0]
    status = rs[1]
    web_port = rs[2]
    rpyc_port = rs[3]
    if status == "RUNNING":
        es_process_name = get_es_process_name()
        es_stop_cmd = es_stop_systemd_cmd if es_process_name == "systemd" else es_stop_sysvinit_cmd if es_process_name == "sysv_init" else "bin_stop_cmd"
        if es_stop_cmd == "bin_stop_cmd":
            result = kill_service("elasticsearch")
        else:
            result = run_services.run_bigdata_services(es_stop_cmd, 'ES Stopped',
                                                       'Error Stopping ES')

        return run_services.confirm_stop(result, "elastic_search_elastic_search", id, web_port, rpyc_port)
    else:
        return '{"success": 1, "msg": [" Already Stopped!!!"]}'


def elasticsearch_restart():
    '''
    Restarts elasticsearch
    '''
    log.info("\nRestarting ES\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        stop = json.loads(es_stop(cluster_id))
        if stop["success"]:
            start = json.loads(es_start(cluster_id))
            if start["success"]:
                return '{"success": 1, "msg": ["Successfully Restarted Elasticsearch"]}'
            else:
                return '{"success": 0, "msg": ["Error Restarting Elasticsearch!!!"]}'
        else:
            return '{"success": 0, "msg": ["Error Restarting Elasticsearch!!!"]}'
    else:
        return api_status

