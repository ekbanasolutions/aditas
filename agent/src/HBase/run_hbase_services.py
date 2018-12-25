import datetime
import json
import os
import subprocess
import sys
import time
from multiprocessing import Pool

import run_services
from API_KEYS.keys import check_apiKey
from Custom_JMX.hbase import get_hbase_db_info, execute_hbase_sql, get_ip
from Postgres_connection.connection import get_postgres_connection
from bigdata_logs.logger import getLoggingInstance
from custom_requests import request

log = getLoggingInstance()

parent_dir = os.getenv("parent_dir")
sys.path.append(parent_dir)

from System_Info.hostname_info import get_system_ip

hbase_bin=os.getenv("hbase_bin_dir")

hbase_start_cmd = '%sstart-hbase.sh' % hbase_bin
hbase_stop_cmd = '%sstop-hbase.sh' % hbase_bin
hmaster_start_cmd = '%shbase-daemon.sh start master' % hbase_bin
hmaster_stop_cmd = '%shbase-daemon.sh stop master' % hbase_bin
hregionserver_start_cmd = '%shbase-daemon.sh start regionserver' % hbase_bin
hregionserver_stop_cmd = '%shbase-daemon.sh stop regionserver' % hbase_bin

get_hbase_status = "echo \"status 'simple'\" | %shbase shell | sed '1,5d'" % hbase_bin


def hbase_home():
    '''
    :return: Returns Urls for hbase services
    '''
    path = "Urls for HBase services:\n\
            '/hbase/start/': 'hbase_start'\n\
            '/hbase/stop/': 'hbae_stop'\n\
            '/hbase/restart/': 'hbase_restart'\n\
            '/hbase/master/start/': 'hbase_master_start'\n\
            '/hbase/master/stop/': 'hbase_master_stop'\n\
            '/hbase/master/restart/': 'hbase_master_restart'\n\
            '/hbase/regionserver/start/': 'hbase_regionserver_start'\n\
            '/hbase/regionserver/stop/': 'hbase_regionserver_stop'\n\
            '/hbase/regionserver/restart/': 'hbase_regionserver_restart'"

    return path


def hbase_start():
    '''
    Starts hbase services (hbase master, hbase regionserver)
    :return: success if hbase_start_cmd runs successfully else error message is shown
    '''
    log.info("\nStarting HBase\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        result = run_services.run_bigdata_services(hbase_start_cmd, 'HBase Services Started',
                                                 'Error Starting HBase Services')
        up_status = update_hbase_master()
        if up_status is not None:
            if up_status["success"] == 0:
                return json.dumps(up_status)
        return result
    else:
        return api_status


def hbase_stop():
    '''
    Stops hbase services (hbase master, hbase regionserver)
    :return: success if hbase_stop_cmd runs successfully else error message is shown
    '''
    log.info("\nStopping HBase\n")
    with Pool(processes=1) as pool:
        mul_pool = pool.apply_async(stop_all_hbase)
        try:
            result = mul_pool.get(timeout=120)
            return result
        except Exception as e:
            pool.terminate()
            return '{"success": 2, "msg": ["Took more than 2 minutes to stop all hbase service!!!"]}'


def stop_all_hbase():
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        conn = get_postgres_connection()
        cur = conn.cursor()
        sql = "select status from hbase_hbase where type=1"
        cur.execute(sql)
        rows = cur.fetchall()
        status_list = [' '.join(item) for item in rows]
        if "RUNNING" in status_list:
            result = run_services.run_bigdata_services(hbase_stop_cmd, 'HBase Service Stopped',
                                                 'Error Stopping HBase Services')
            update_hbase_master()
            if json.loads(result)["success"]:
                cur.execute(sql)
                rows = cur.fetchall()
                status_list = [' '.join(item) for item in rows]
                if "RUNNING" in status_list:
                    cur.close()
                    conn.close()
                    return '{"success": 2, "msg": ["HBase Service not Stopped!!!"]}'
                else:
                    cur.close()
                    conn.close()
                    return result
            else:
                cur.close()
                conn.close()
                return result
        else:
            return '{"success": 1}'
    else:
        return api_status


def hbase_restart():
    '''
    Stops hbase services and starts them again
    '''
    log.info("\nRestarting HBase Services\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        stop = json.loads(hbase_stop())

        if stop["success"] == 1:
            start = json.loads(hbase_start())
            if start["success"]:
                return '{"success": 1, "msg": ["Successfully restarted hbase service"]}'
            else:
                return '%s' % json.dumps(stop)
        elif stop["success"] == 2:
            stop["success"] = 2
            return '%s' % json.dumps(stop)
        else:
            return '%s' % json.dumps(stop)

    else:
        return api_status



def hmaster_start():
    '''
    Starts hbase master
    :return: success if hmaster_start_cmd runs successfully else error message is shown
    '''
    log.info("\nStarting HMaster\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        return master_start(cluster_id)
    else:
        return api_status


def master_start(cluster_id):
    ip = get_system_ip()
    sql = "select id, status, web_port, rpyc_port from hbase_hbase where ip='%s' and type=1 and cluster_id=%d" % (
    ip, cluster_id)
    rs = run_services.get_service_status(sql)
    id = rs[0]
    status = rs[1]
    web_port = rs[2]
    rpyc_port = rs[3]
    if status != "RUNNING":
        result = run_services.run_bigdata_services(hmaster_start_cmd, 'HMaster Started', 'Error Starting HBase Master')
        update_hbase_master()
        return run_services.confirm_start(result, "hbase_hbase", id, web_port, rpyc_port)
    else:
        return '{"success": 1, "msg": ["HMaster Already Running!!!"]}'


def hmaster_stop():
    '''
    Stops hbase master
    :return: success if hmaster_stop_cmd runs successfully else error message is shown
    '''
    log.info("\nStopping HMaster\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        with Pool(processes=1) as pool:
            loaded_json = json.loads(request.data.decode())
            cluster_id = loaded_json['cluster_id']
            mul_pool = pool.apply_async(master_stop, args=[cluster_id])
            try:
                result = mul_pool.get(timeout=20)
                return result
            except Exception as e:
                pool.terminate()
                return '{"success": 2, "msg": ["Took more than 20 seconds to stop hbase!!!"]}'
    else:
        return api_status


def master_stop(cluster_id):
    ip = get_system_ip()
    sql = "select id, status, web_port, rpyc_port from hbase_hbase where ip='%s' and type=1 and cluster_id=%d" % (
        ip, cluster_id)
    rs = run_services.get_service_status(sql)
    id = rs[0]
    status = rs[1]
    web_port = rs[2]
    rpyc_port = rs[3]
    if status == "RUNNING":
        result = run_services.run_bigdata_services(hmaster_stop_cmd, 'HMaster Stopped', 'Error Stopping HBase Master')
        update_hbase_master()
        return run_services.confirm_stop(result, "hbase_hbase", id, web_port, rpyc_port)
    else:
        return '{"success": 1, "msg": ["HMaster Already Stopped!!!"]}'


def hmaster_restart():
    '''
    Restarts hbase master
    '''
    log.info("\nRestarting Hbase Master\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        with Pool(processes=1) as pool:
            loaded_json = json.loads(request.data.decode())
            cluster_id = loaded_json['cluster_id']

            mul_pool = pool.apply_async(master_stop, args=[cluster_id])
            try:
                result = mul_pool.get(timeout=20)
                stop = json.loads(result)
                if stop["success"] == 1:
                    start = json.loads(master_start(cluster_id))
                    if start["success"]:
                        return '{"success": 1, "msg": ["Successfully Restarted HMaster"]}'
                    else:
                        return start
                elif stop["success"] == 2:
                    stop["success"] = 2
                    return stop
                else:
                    return stop
            except Exception as e:
                pool.terminate()
                return '{"success": 2, "msg": ["Took more than 20 seconds to restart hmaster!!!"]}'
    else:
        return api_status


def hregionserver_start():
    '''
    Starts hbase regionserver
    :return: success if hregionserver_start_cmd runs successfully else error message is shown
    '''
    log.info("\nStarting HRegionserver\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        cluster_id = loaded_json['cluster_id']
        return regionserver_start(cluster_id)
    else:
        return api_status


def regionserver_start(cluster_id):
    ip = get_system_ip()
    sql = "select id, status, web_port, rpyc_port from hbase_hbase where ip='%s' and type=0 and cluster_id=%d" % (
    ip, cluster_id)
    rs = run_services.get_service_status(sql)
    id = rs[0]
    status = rs[1]
    web_port = rs[2]
    rpyc_port = rs[3]
    if status != "RUNNING":
        result = run_services.run_bigdata_services(hregionserver_start_cmd, 'Regionserver Started',
                                                   'Error Starting Regionserver')
        update_hbase_master()
        return run_services.confirm_start(result, "hbase_hbase", id, web_port, rpyc_port)
    else:
        return '{"success": 1, "msg": ["Regionserver Already Running!!!"]}'


def hregionserver_stop():
    '''
    Stops hbase regionserver
    :return: success if hregionserver_stop_cmd runs successfully else error message is shown
    '''
    log.info("\nStopping HRegionserver\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        with Pool(processes=1) as pool:
            loaded_json = json.loads(request.data.decode())
            cluster_id = loaded_json['cluster_id']
            mul_pool = pool.apply_async(regionserver_stop, args=[cluster_id])
            try:
                result = mul_pool.get(timeout=20)
                return result
            except Exception as e:
                pool.terminate()
                return '{"success": 2, "msg": ["Took more than 20 seconds to stop regionserver!!!"]}'
    else:
        return api_status


def regionserver_stop(cluster_id):
    ip = get_system_ip()
    sql = "select id, status, web_port, rpyc_port from hbase_hbase where ip='%s' and type=0 and cluster_id=%d" % (
        ip, cluster_id)
    rs = run_services.get_service_status(sql)
    id = rs[0]
    status = rs[1]
    web_port = rs[2]
    rpyc_port = rs[3]
    if status == "RUNNING":
        result = run_services.run_bigdata_services(hregionserver_stop_cmd, 'Regionserver Stopped',
                                                   'Error Stopping Regionserver')
        update_hbase_master()
        return run_services.confirm_stop(result, "hbase_hbase", id, web_port, rpyc_port)
    else:
        return '{"success": 1, "msg": ["Regionserver Already Stopped!!!"]}'


def hregionserver_restart():
    '''
    Restarts hbase regionserver
    '''
    log.info("\nRestarting Hbase Regionserver\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        with Pool(processes=1) as pool:
            loaded_json = json.loads(request.data.decode())
            cluster_id = loaded_json['cluster_id']

            mul_pool = pool.apply_async(regionserver_stop, args=[cluster_id])
            try:
                result = mul_pool.get(timeout=20)
                stop = json.loads(result)
                if stop["success"] == 1:
                    start = json.loads(regionserver_start(cluster_id))
                    if start["success"]:
                        return '{"success": 1, "msg": ["Successfully Restarted HBase Regionserver"]}'
                    else:
                        return start
                elif stop["success"] == 2:
                    stop["success"] = 2
                    return stop
                else:
                    return stop
            except Exception as e:
                pool.terminate()
                return '{"success": 2, "msg": ["Took more than 20 seconds to restart regionserver!!!"]}'
    else:
        return api_status


def update_hbase_master():
    try:
        updated_at = int(str(time.time()).split(".")[0])

        result = subprocess.check_output([get_hbase_status], stderr=subprocess.STDOUT, shell=True).decode("utf-8")

        result = result.strip().split('\n')

        index = None
        count = 0
        while index is None:
            result = subprocess.check_output([get_hbase_status], stderr=subprocess.STDOUT, shell=True).decode("utf-8")
            result = result.strip().split('\n')

            try:
                index = [i for i, s in enumerate(result) if 'active master' in s][0]
            except Exception as e:
                log.error(e)

            if index is not None:
                break
            time.sleep(1)
            count = count + 1
            if count == 5:
                return {"success": 0, "msg": ["Could not get master status, please check your log and restart again!!!"]}

        result = result[index:]

        active = (result[0]).strip().split(":", 1)[0]
        if active != "active master":
            cluster_id = get_hbase_db_info(get_system_ip())[1]

            sql = """UPDATE hbase_hbase set status='{0}', state={1}, updated_at={2} WHERE type={3} 
        and cluster_id={4} RETURNING id;""".format("SHUTDOWN", 0, updated_at, 1, cluster_id)

            execute_hbase_sql(sql)
        else:
            active_master = ((result[0]).strip().split(":", 1)[1]).strip().split()[0]
            active_master_ip = get_ip(active_master.split(":")[0])

            active_id = get_hbase_db_info(active_master_ip)[0]
            cluster_id = get_hbase_db_info(active_master_ip)[1]

            sql = """UPDATE hbase_hbase set status='{0}', state={1}, updated_at={2} WHERE id={3} RETURNING id;""".format(
                "RUNNING", 1, updated_at, active_id)

            execute_hbase_sql(sql)

            no_of_backup_master = int((result[1]).split()[0])
            if no_of_backup_master > 0:
                backup_master = (result[2]).strip().split()[0]
                backup_master_ip = get_ip(backup_master.split(":")[0])

                sql = """UPDATE hbase_hbase set status='{0}', state={1}, updated_at={2} where type=1 and 
        cluster_id={3} and ip='{4}' RETURNING id;""".format("RUNNING", 0, updated_at, cluster_id, backup_master_ip)

                execute_hbase_sql(sql)

            else:
                sql = """UPDATE hbase_hbase set status='{0}', state={1}, updated_at={2} where type=1 and cluster_id={3} and 
        ip <> '{4}' RETURNING id;""".format("SHUTDOWN", 0, updated_at, cluster_id, active_master_ip)

                execute_hbase_sql(sql)
    except Exception as e:
        log.error(e)
