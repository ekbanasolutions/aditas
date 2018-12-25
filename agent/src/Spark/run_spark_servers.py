import json
import os

import run_services
from API_KEYS.keys import check_apiKey
from Postgres_connection.connection import get_postgres_connection
from System_Info.hostname_info import get_system_ip
from bigdata_logs.logger import getLoggingInstance
from custom_requests import request

log = getLoggingInstance()

spark_sbin_dir = os.getenv("spark_sbin_dir")
spark_stop_cmd = spark_sbin_dir + "stop-all.sh"
spark_start_cmd = spark_sbin_dir + "start-all.sh"
start_spark_master_cmd = spark_sbin_dir + "start-master.sh"
start_spark_slave_cmd = spark_sbin_dir + "start-slave.sh spark://"
stop_spark_master_cmd = spark_sbin_dir + "stop-master.sh"
stop_spark_slave_cmd = spark_sbin_dir + "stop-slave.sh"


def spark_home():
    '''
    :return: Returns Urls for spark services
    '''
    path = "Urls for Spark services:\n\
            '/spark/start/': 'spark_start'\n\
            '/spark/stop/': 'spark_stop'\n\
            '/spark/restart/': 'spark_restart'\n\
            '/spark/master/start/': 'spark_master_start'\n\
            '/spark/master/stop/': 'spark_master_stop'\n\
            '/spark/master/restart/': 'spark_master_restart'\n\
            '/spark/slave/start/': 'spark_slave_start'\n\
            '/spark/slave/stop/': 'spark_slave_stop'\n\
            '/spark/slave/restart/': 'spark_slave_restart'"

    return path

def start_spark():
    '''
    Starts spark
    :return: Returns success if spark_start command executes successfully or error message is shown
    '''
    log.info("\nStarting spark\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        # return run_services.run_bigdata_services(spark_start_cmd, 'spark Started', 'Error Starting spark')
        conn = get_postgres_connection()
        cur = conn.cursor()
        sql = "select status from spark_spark where type=1 and state=1"
        cur.execute(sql)
        rows = cur.fetchall()
        status_list = [' '.join(item) for item in rows]
        if "SHUTDOWN" in status_list:
            result = run_services.run_bigdata_services(spark_start_cmd, 'spark Started', 'Error Starting spark')
            if json.loads(result)["success"]:
                sql = """UPDATE spark_spark set status='RUNNING' where type=1 and state=1;"""
                cur.execute(sql)
                conn.commit()
                cur.close()
                conn.close()
                return result
        else:
            cur.close()
            conn.close()
            return '{"success": 1}'
    else:
        return api_status


def stop_spark():
    '''
    Stops spark
    :return: Returns success if spark_stop command executes successfully or error message is shown
    '''
    log.info("\nStopping spark\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        conn = get_postgres_connection()
        cur = conn.cursor()
        sql = "select status from spark_spark where type=1"
        cur.execute(sql)
        rows = cur.fetchall()
        status_list = [' '.join(item) for item in rows]
        if "RUNNING" in status_list:
            result = run_services.run_bigdata_services(spark_stop_cmd, 'spark Stopped', 'Error Stopping spark')
            if json.loads(result)["success"]:
                sql = """UPDATE spark_spark set status='SHUTDOWN' where type=1 and state=1;"""
                cur.execute(sql)
                conn.commit()
                cur.close()
                conn.close()
                return result
        else:
            cur.close()
            conn.close()
            return '{"success": 1}'
    else:
        return api_status


def restart_spark():
    '''
    Restarts spark
    :return: Returns success if spark_restart command executes successfully or error message is shown
    '''
    log.info("\nRestarting spark\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        stop = json.loads(stop_spark())
        if stop["success"]:
            start = json.loads(start_spark())
            if start["success"]:
                return '{"success": 1, "msg": ["Successfully restarted spark service"]}'
            else:
                return '{"success": 0, "msg": ["Error restarting spark services!!!"]}'
        else:
            return '{"success": 0, "msg": ["Error restarting spark services!!!"]}'

    else:
        return api_status


def start_spark_master():
    '''
    Starts spark master
    :return: Returns success if start_spark_master command executes successfully or error message is shown
    '''
    log.info("\nStarting spark master\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        return spm_start(cluster_id)
    else:
        return api_status


def spm_start(cluster_id):
    ip = get_system_ip()
    sql = "select id, status, web_port, rpyc_port from spark_spark where ip='%s' and type=1 and cluster_id=%d" % (ip, cluster_id)
    rs = run_services.get_service_status(sql)
    id = rs[0]
    status = rs[1]
    web_port = rs[2]
    rpyc_port = rs[3]
    if status != "RUNNING":
        result = run_services.run_bigdata_services(start_spark_master_cmd, 'spark master started', 'Error Starting Spark Master')
        return run_services.confirm_start(result, "spark_spark", id, web_port, rpyc_port)
    else:
        return '{"success": 1, "msg": ["Spark Master Already Running!!!"]}'


def stop_spark_master():
    '''
    Stops spark master
    :return: Returns success if stop_spark_master command executes successfully or error message is shown
    '''
    log.info("\nStopping spark master\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        return spm_stop(cluster_id)
    else:
        return api_status


def spm_stop(cluster_id):
    ip = get_system_ip()
    sql = "select id, status, web_port, rpyc_port from spark_spark where ip='%s' and type=1 and cluster_id=%d" % (ip, cluster_id)
    rs = run_services.get_service_status(sql)
    id = rs[0]
    status = rs[1]
    web_port = rs[2]
    rpyc_port = rs[3]
    if status == "RUNNING":
        result = run_services.run_bigdata_services(stop_spark_master_cmd, 'spark master stopped', 'Error Stopping Spark Master')
        return run_services.confirm_stop(result, "spark_spark", id, web_port, rpyc_port)
    else:
        return '{"success": 1, "msg": ["Spark Master Already Stopped!!!"]}'


def spark_master_restart():
    '''
    Restarts spark master
    '''
    log.info("\nRestarting Spark Master\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        stop = json.loads(spm_stop(cluster_id))
        if stop["success"]:
            start = json.loads(spm_start(cluster_id))
            if start["success"]:
                return '{"success": 1, "msg": ["Successfully Restarted Spark Master"]}'
            else:
                return '{"success": 0, "msg": ["Error Restarting Spark Master!!!"]}'
        else:
            return '{"success": 0, "msg": ["Error Restarting Spark Master!!!"]}'
    else:
        return api_status


def start_spark_slave():
    '''
    Starts spark slave
    :return: Returns success if start_spark_slave command executes successfully or error message is shown
    '''
    log.info("\nStarting spark slave\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        master_ip = loaded_json['ip']
        port = loaded_json['port']
        return sps_start(cluster_id, master_ip, port)
    else:
        return api_status


def sps_start(cluster_id, master_ip, port):
    ip = get_system_ip()
    sql = "select id, status, web_port, rpyc_port from spark_spark where ip='%s' and type=0 and cluster_id=%d" % (ip, cluster_id)
    rs = run_services.get_service_status(sql)
    id = rs[0]
    status = rs[1]
    web_port = rs[2]
    rpyc_port = rs[3]
    if status != "RUNNING":
        spark_slave_cmd = start_spark_slave_cmd + '%s:%s' % (master_ip, port)
        result = run_services.run_bigdata_services(spark_slave_cmd, 'spark slave started', 'Error Starting Spark Slave')
        return run_services.confirm_start(result, "spark_spark", id, web_port, rpyc_port)
    else:
        return '{"success": 1, "msg": ["Spark Slave Already Running!!!"]}'


def stop_spark_slave():
    '''
    Stops spark slave
    :return: Returns success if stop_spark_slave command executes successfully or error message is shown
    '''
    log.info("\nStopping spark slave\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        return sps_stop(cluster_id)
    else:
        return api_status


def sps_stop(cluster_id):
    ip = get_system_ip()
    sql = "select id, status, web_port, rpyc_port from spark_spark where ip='%s' and type=0 and cluster_id=%d" % (ip, cluster_id)
    rs = run_services.get_service_status(sql)
    id = rs[0]
    status = rs[1]
    web_port = rs[2]
    rpyc_port = rs[3]
    if status == "RUNNING":
        result = run_services.run_bigdata_services(stop_spark_slave_cmd, 'spark slave stopped', 'Error Stopping Spark Slave')
        return run_services.confirm_stop(result, "spark_spark", id, web_port, rpyc_port)
    else:
        return '{"success": 1, "msg": ["Spark Slave Already Stopped!!!"]}'


def spark_slave_restart():
    '''
    Restarts spark slave
    '''
    log.info("\nRestarting Spark Slave\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        master_ip = loaded_json['ip']
        port = loaded_json['port']
        stop = json.loads(sps_stop(cluster_id))
        if stop["success"]:
            start = json.loads(sps_start(cluster_id, master_ip, port))
            if start["success"]:
                return '{"success": 1, "msg": ["Successfully Restarted Spark Slave"]}'
            else:
                return '{"success": 0, "msg": ["Error Restarting Spark Slave!!!"]}'
        else:
            return '{"success": 0, "msg": ["Error Restarting Spark Slave!!!"]}'
    else:
        return api_status
