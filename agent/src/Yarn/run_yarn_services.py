import json
import os
import sys

import run_services
from API_KEYS.keys import check_apiKey
from Custom_JMX.yarn import update_rm_info
from Postgres_connection.connection import get_postgres_connection
from System_Info.hostname_info import get_system_ip
from bigdata_logs.logger import getLoggingInstance
from custom_requests import request

log = getLoggingInstance()

parent_dir = os.getenv("parent_dir")
sys.path.append(parent_dir)

hadoop_sbin = os.getenv("hadoop_sbin_dir")

yarn_start_cmd = '%sstart-yarn.sh' % hadoop_sbin
yarn_stop_cmd = '%sstop-yarn.sh' % hadoop_sbin
rm_start_cmd = '%syarn-daemon.sh start resourcemanager' % hadoop_sbin
rm_stop_cmd = '%syarn-daemon.sh stop resourcemanager' % hadoop_sbin
nm_start_cmd = '%syarn-daemon.sh start nodemanager' % hadoop_sbin
nm_stop_cmd = '%syarn-daemon.sh stop nodemanager' % hadoop_sbin


def yarn_home():
    '''
    :return: Returns Urls for Yarn services
    '''
    path = "Urls for Yarn services:\n\
            '/yarn/start/': 'yarn_start'\n\
            '/yarn/stop/': 'yarn_stop'\n\
            '/yarn/restart/': 'yarn_restart'\n\
            '/yarn/rm/start/': 'yarn_rm_start'\n\
            '/yarn/rm/stop/': 'yarn_rm_stop'\n\
            '/yarn/rm/restart/': 'yarn_rm_restart'\n\
            '/yarn/nm/start/': 'yarn_nm_start'\n\
            '/yarn/nm/stop/': 'yarn_nm_stop'\n\
            '/yarn/nm/restart/': 'yarn_nm_restart'"

    return path

def yarn_start():
    '''
    Starts yarn services (nodemanager, resourcemanager)
    :return: Returns success if yarn_start_cmd command executes successfully or error message is shown
    '''
    log.info("\nStarting Yarn\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        result = run_services.run_bigdata_services(yarn_start_cmd, 'Started Yarn Services',
                                                 'Error Starting Yarn Services')
        update_rm_info()
        return result
    else:
        return api_status


def yarn_stop():
    log.info("\nStopping Yarn\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        conn = get_postgres_connection()
        cur = conn.cursor()
        sql = "select status from yarn_yarn where type=1"
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        status_list = [' '.join(item) for item in rows]
        if "RUNNING" in status_list:
            result = run_services.run_bigdata_services(yarn_stop_cmd, 'Stopped Yarn Services', 'Error Stopping Yarn Services')
            if json.loads(result)["success"]:
                update_rm_info()
                return result
        else:
            return '{"success": 1}'
    else:
        return api_status


def yarn_restart():
    '''
    Restarts yarn services (nodemanager, resourcemanager)
    '''
    log.info("\nRestarting Yarn\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        stop = json.loads(yarn_stop())
        if stop["success"] == 1:
            start = json.loads(yarn_start())
            if start["success"]:
                # Updating Resource Manager Info before sending success response
                return '{"success": 1, "msg": ["Successfully Restarted Yarn Service"]}'
            else:
                return '{"success": 0, "msg": ["Error Restarting Yarn Services!!!"]}'
        elif stop["success"] == 2:
            return '{"success": 2, "msg": ["Error Restarting Yarn Services!!!"]}'
        else:
            return '{"success": 0, "msg": ["Error Restarting Yarn Services!!!"]}'
    else:
        return api_status


def resourcemanager_start():
    '''
    Starts resource manager
    :return: Returns success if rm_start_cmd command executes successfully or error message is shown
    '''
    log.info("\nStarting Resourcemanager\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        return rm_start(cluster_id)
    else:
        return api_status


def rm_start(cluster_id):
    ip = get_system_ip()
    sql = "select id, status, web_port, rpyc_port from yarn_yarn where ip='%s' and type=1 and cluster_id=%d" % (ip, cluster_id)
    rs = run_services.get_service_status(sql)
    id = rs[0]
    status = rs[1]
    web_port = rs[2]
    rpyc_port = rs[3]
    if status != "RUNNING":
        result = run_services.run_bigdata_services(rm_start_cmd, 'Resource manager Started',
                                                   'Error Starting Resource manager')
        update_rm_info()
        return run_services.confirm_start(result, "yarn_yarn", id, web_port, rpyc_port)
    else:
        return '{"success": 1, "msg": ["Resource Manager Already Running!!!"]}'


def resourcemanager_stop():
    '''
    Stops resource manager
    :return: Returns success if rm_stop_cmd command executes successfully or error message is shown
    '''
    log.info("\nStopping Resourcemanager\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        return rm_stop(cluster_id)
    else:
        return api_status


def rm_stop(cluster_id):
    ip = get_system_ip()
    sql = "select id, status, web_port, rpyc_port from yarn_yarn where ip='%s' and type=1 and cluster_id=%d" % (ip, cluster_id)
    rs = run_services.get_service_status(sql)
    id = rs[0]
    status = rs[1]
    web_port = rs[2]
    rpyc_port = rs[3]
    if status == "RUNNING":
        result = run_services.run_bigdata_services(rm_stop_cmd, 'Resource manager Stopped',
                                                   'Error Stopping Resource manager')
        update_rm_info()
        return run_services.confirm_stop(result, "yarn_yarn", id, web_port, rpyc_port)
    else:
        return '{"success": 1, "msg": ["Resource Manager Already Stopped!!!"]}'


def resourcemanager_restart():
    '''
    Restarts yarn resourcemanager
    '''
    log.info("\nRestarting Yarn Resource Manager\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        stop = json.loads(rm_stop(cluster_id))
        if stop["success"] == 1:
            start = json.loads(rm_start(cluster_id))
            if start["success"]:
                return '{"success": 1, "msg": ["Successfully Restarted Yarn ResourceManager"]}'
            else:
                return '{"success": 0, "msg": ["Error Restarting Yarn ResourceManager!!!"]}'
        elif stop["success"] == 2:
            return '{"success": 2, "msg": ["Error Restarting Yarn ResourceManager!!!"]}'
        else:
            return '{"success": 0, "msg": ["Error Restarting Yarn ResourceManager!!!"]}'
    else:
        return api_status


def nodemanager_start():
    '''
    Starts node manager
    :return: Returns success if nm_start_cmd command executes successfully or error message is shown
    '''
    log.info("\nStarting Nodemanager\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        return nm_start(cluster_id)
    else:
        return api_status


def nm_start(cluster_id):
    ip = get_system_ip()
    sql = "select id, status, web_port, rpyc_port from yarn_yarn where ip='%s' and type=0 and cluster_id=%d" % (ip, cluster_id)
    rs = run_services.get_service_status(sql)
    id = rs[0]
    status = rs[1]
    web_port = rs[2]
    rpyc_port = rs[3]
    if status != "RUNNING":
        result = run_services.run_bigdata_services(nm_start_cmd, 'Node manager Started',
                                                   'Error Starting Node manager')
        update_rm_info()
        return run_services.confirm_start(result, "yarn_yarn", id, web_port, rpyc_port)
    else:
        return '{"success": 1, "msg": ["Node Manager Already Running!!!"]}'


def nodemanager_stop():
    '''
    Stops node manager
    :return: Returns success if nm_start_cmd command executes successfully or error message is shown
    '''
    log.info("\nStopping Nodemanager\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        return nm_stop(cluster_id)
    else:
        return api_status


def nm_stop(cluster_id):
    ip = get_system_ip()
    sql = "select id, status, web_port, rpyc_port from yarn_yarn where ip='%s' and type=0 and cluster_id=%d" % (ip, cluster_id)
    rs = run_services.get_service_status(sql)
    id = rs[0]
    status = rs[1]
    web_port = rs[2]
    rpyc_port = rs[3]
    if status == "RUNNING":
        result = run_services.run_bigdata_services(nm_stop_cmd, 'Node manager Stopped',
                                                   'Error Stopping Node manager')
        update_rm_info()
        return run_services.confirm_stop(result, "yarn_yarn", id, web_port, rpyc_port)
    else:
        return '{"success": 1, "msg": ["Node Manager Already Stopped!!!"]}'


def nodemanager_restart():
    '''
    Restarts yarn nodemanager
    '''
    log.info("\nRestarting Yarn Node Manager\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        stop = json.loads(nm_stop(cluster_id))
        if stop["success"] == 1:
            start = json.loads(nm_start(cluster_id))
            if start["success"]:
                return '{"success": 1, "msg": ["Successfully Restarted Yarn NodeManager"]}'
            else:
                return '{"success": 0, "msg": ["Error Restarting Yarn NodeManager!!!"]}'
        elif stop["success"] == 2:
            return '{"success": 2, "msg": ["Error Restarting Yarn NodeManager!!!"]}'
        else:
            return '{"success": 0, "msg": ["Error Restarting Yarn NodeManager!!!"]}'
    else:
        return api_status
