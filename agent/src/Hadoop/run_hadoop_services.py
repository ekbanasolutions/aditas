import json
import os
import sys

import run_services
from API_KEYS.keys import check_apiKey
from Custom_JMX.hdfs import update_namenode_info
from Postgres_connection.connection import get_postgres_connection
from bigdata_logs.logger import getLoggingInstance
from custom_requests import request

log = getLoggingInstance()

parent_dir = os.getenv("parent_dir")
sys.path.append(parent_dir)

from System_Info.hostname_info import get_system_ip

hadoop_bin=os.getenv("hadoop_bin_dir")
hadoop_sbin=os.getenv("hadoop_sbin_dir")

dfs_start_cmd = '%sstart-dfs.sh' % hadoop_sbin
dfs_stop_cmd = '%sstop-dfs.sh' % hadoop_sbin
namenode_start_cmd = '%shadoop-daemon.sh start namenode' % hadoop_sbin
namenode_stop_cmd = '%shadoop-daemon.sh stop namenode' % hadoop_sbin
datanode_start_cmd = '%shadoop-daemon.sh start datanode' % hadoop_sbin
datanode_stop_cmd = '%shadoop-daemon.sh stop datanode' % hadoop_sbin
change_hamaster_cmd = '%shdfs haadmin -failover ' % hadoop_bin


def hadoop_home():
    '''
    :return: Returns Urls for hdfs services
    '''
    path = "Urls for Hadoop services:\n\
            '/hadoop/dfs/start/': 'dfs_start'\n\
            '/hadoop/dfs/stop/': 'dfs_stop'\n\
            '/hadoop/dfs/restart/': 'dfs_restart'\n\
            '/hadoop/namenode/start/': 'namenode_start'\n\
            '/hadoop/namenode/stop/': 'namenode_stop'\n\
            '/hadoop/namenode/restart/': 'namenode_restart'\n\
            '/hadoop/datanode/start/': 'datanode_start'\n\
            '/hadoop/datanode/stop/': 'datanode_stop'\n\
            '/hadoop/datanode/restart/': 'datanode_restart'"

    return path


def dfs_start():
    '''
    Starts dfs services (namenode, datanode, zkfc, journalnode)
    :return: success if dfs_start_cmd runs successfully else error message is shown
    '''
    log.info("\nStarting DFS Services\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        result = run_services.run_bigdata_services(dfs_start_cmd, 'Started DFS Service', 'Error Starting DFS Services')
        update_namenode_info()
        return result
    else:
        return api_status


def dfs_stop():
    '''
    Stops dfs services (namenode, datanode, zkfc, journalnode)
    :return: success if dfs_stop_cmd runs successfully else error message is shown
    '''
    log.info("\nStopping DFS Services\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        conn = get_postgres_connection()
        cur = conn.cursor()
        sql = "select status from hdfs_hdfs where type=1"
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        status_list = [' '.join(item) for item in rows]
        if "RUNNING" in status_list:
            result = run_services.run_bigdata_services(dfs_stop_cmd, 'Stopped DFS Services', 'Error Stopping DFS Services')
            if json.loads(result)["success"]:
                update_namenode_info()
                return result
        else:
            update_namenode_info()
            return '{"success": 1}'
    else:
        return api_status


def dfs_restart():
    '''
    Stops dfs services and starts them again
    '''
    log.info("\nRestarting DFS Services\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        stop = json.loads(dfs_stop())
        if stop["success"]:
            start = json.loads(dfs_start())
            if start["success"]:
                return '{"success": 1, "msg": ["Successfully restarted dfs service"]}'
            else:
                return '{"success": 0, "msg": ["Error restarting dfs services!!!"]}'
        else:
            return '{"success": 0, "msg": ["Error restarting dfs services!!!"]}'

    else:
        return api_status


def namenode_start():
    '''
    Starts namenode service
    :return: success if namenode_start_cmd runs successfully else error message is shown
    '''
    log.info("\nStarting Name node\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        return nn_start(cluster_id)
    else:
        return api_status


def nn_start(cluster_id):
    ip = get_system_ip()
    sql = "select id, status, web_port, rpyc_port from hdfs_hdfs where ip='%s' and type=1 and cluster_id=%d" % (ip, cluster_id)
    rs = run_services.get_service_status(sql)
    id = rs[0]
    status = rs[1]
    web_port = rs[2]
    rpyc_port = rs[3]
    if status != "RUNNING":
        result = run_services.run_bigdata_services(namenode_start_cmd, 'Namenode Started', 'Error Starting Namenode')
        update_namenode_info()
        return run_services.confirm_start(result, "hdfs_hdfs", id, web_port, rpyc_port)
    else:
        return '{"success": 1, "msg": ["Namenode Already Running!!!"]}'


def namenode_stop():
    '''
    Stops namenode service
    :return: success if namenode_stop_cmd runs successfully else error message is shown
    '''
    log.info("\nStopping Name node\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        return nn_stop(cluster_id)
    else:
        return api_status


def nn_stop(cluster_id):
    ip = get_system_ip()
    sql = "select id, status, web_port, rpyc_port from hdfs_hdfs where ip='%s' and type=1 and cluster_id=%d" % (ip, cluster_id)
    rs = run_services.get_service_status(sql)
    id = rs[0]
    status = rs[1]
    web_port = rs[2]
    rpyc_port = rs[3]
    if status == "RUNNING":
        result = run_services.run_bigdata_services(namenode_stop_cmd, 'Namenode Stopped', 'Error Stopping Namenode')
        update_namenode_info()
        return run_services.confirm_stop(result, "hdfs_hdfs", id, web_port, rpyc_port)
    else:
        return '{"success": 1, "msg": ["Namenode Already Stopped!!!"]}'


def namenode_restart():
    '''
    Restarts Namenode
    '''
    log.info("\nRestarting Namenode\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        stop = json.loads(nn_stop(cluster_id))
        if stop["success"] == 1:
            start = json.loads(nn_start(cluster_id))
            if start["success"]:
                return '{"success": 1, "msg": ["Successfully Restarted Namenode"]}'
            else:
                return '{"success": 0, "msg": ["Error Restarting Namenode!!!"]}'
        elif stop["success"] == 2:
            return '{"success": 2, "msg": ["Error Restarting Namenode!!!"]}'
        else:
            return '{"success": 0, "msg": ["Error Restarting Namenode!!!"]}'
    else:
        return api_status


def datanode_start():
    '''
    Starts datanode service
    :return: success if datanode_start_cmd runs successfully else error message is shown
    '''
    log.info("\nStarting Datanode\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        return dn_start(cluster_id)
    else:
        return api_status


def dn_start(cluster_id):
    ip = get_system_ip()
    sql = "select id, status, web_port, rpyc_port from hdfs_hdfs where ip='%s' and type=0 and cluster_id=%d" % (ip, cluster_id)
    rs = run_services.get_service_status(sql)
    id = rs[0]
    status = rs[1]
    web_port = rs[2]
    rpyc_port = rs[3]
    if status != "RUNNING":
        result = run_services.run_bigdata_services(datanode_start_cmd, 'Datanode Started', 'Error Starting Datanode')
        return run_services.confirm_start(result, "hdfs_hdfs", id, web_port, rpyc_port)
    else:
        return '{"success": 1, "msg": ["Datanode Already Running!!!"]}'


def datanode_stop():
    '''
    Stops datanode service
    :return: success if datanode_stop_cmd runs successfully else error message is shown
    '''
    log.info("\nStopping Datanode\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        return dn_stop(cluster_id)
    else:
        return api_status


def dn_stop(cluster_id):
    ip = get_system_ip()
    sql = "select id, status, web_port, rpyc_port from hdfs_hdfs where ip='%s' and type=0 and cluster_id=%d" % (ip, cluster_id)
    rs = run_services.get_service_status(sql)
    id = rs[0]
    status = rs[1]
    web_port = rs[2]
    rpyc_port = rs[3]
    if status == "RUNNING":
        result = run_services.run_bigdata_services(datanode_stop_cmd, 'Datanode Stopped', 'Error Stopping Datanode')
        return run_services.confirm_stop(result, "hdfs_hdfs", id, web_port, rpyc_port)
    else:
        return '{"success": 1, "msg": ["Datanode Already Stopped!!!"]}'


def datanode_restart():
    '''
    Restarts Datanode
    '''
    log.info("\nRestarting Datanode\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        stop = json.loads(dn_stop(cluster_id))
        if stop["success"] == 1:
            start = json.loads(dn_start(cluster_id))
            if start["success"]:
                return '{"success": 1, "msg": ["Successfully Restarted Datanode"]}'
            else:
                return '{"success": 0, "msg": ["Error Restarting Datanode!!!"]}'
        elif stop["success"] == 2:
            return '{"success": 2, "msg": ["Error Restarting Datanode!!!"]}'
        else:
            return '{"success": 0, "msg": ["Error Restarting Datanode!!!"]}'
    else:
        return api_status