import os
import os
import subprocess
import time
from multiprocessing.pool import ThreadPool

from Postgres_connection.connection import get_postgres_connection
from System_Info.hostname_info import get_system_ip
from bigdata_logs.logger import getLoggingInstance

log = getLoggingInstance()

hbase_bin = os.getenv("hbase_bin_dir")
get_hbase_status = "echo \"status 'simple'\" | %shbase shell | sed '1,5d'" % hbase_bin
get_host_ip = "getent hosts "
get_status_cmd = "lsof -t -i:"
updated_at = ""


def get_ip(host):
    try:
        cmd = get_host_ip + '%s' % host
        result = subprocess.check_output([cmd], stderr=subprocess.STDOUT, shell=True).decode("utf-8")
        result = result.split()
        host_ip = result[0]
        return host_ip
    except Exception as e:
        log.error(e)


def check_status(web_port, ipc_port):
    web_status = ipc_status = None
    ipc_cmd = get_status_cmd + '%s' % ipc_port
    web_cmd = get_status_cmd + '%s' % web_port
    try:
        web_status = subprocess.check_output(
            [web_cmd], stderr=subprocess.STDOUT, shell=True).decode("utf-8")
        web_status = web_status.strip().split()
        ipc_status = subprocess.check_output(
            [ipc_cmd], stderr=subprocess.STDOUT, shell=True).decode("utf-8")
        ipc_status = ipc_status.strip().split()
    except Exception as e:
        pass

    if not web_status or not ipc_status:
        return 0
    else:
        return 1


def get_hbase_db_info(ip):
    conn = get_postgres_connection()
    cur = conn.cursor()
    sql = "select id, cluster_id from hbase_hbase where ip='%s' and type=1" % ip

    cur.execute(sql)
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row


def hbase_liveserver_update(value):
    cur = conn = None
    try:
        data = value.split("=")

        if len(data) == 22:
            live_region_data = {
                data[1].split(", ")[1]: data[2].split(", ")[0],
                data[2].split(", ")[1]: data[3].split(", ")[0],
                data[3].split(", ")[1]: data[4].split(", ")[0],
                data[4].split(", ")[1]: data[5].split(", ")[0],
                data[5].split(", ")[1]: data[6].split(", ")[0],
                data[7].split(", ")[1]: data[8].split(", ")[0],
                data[9].split(", ")[1]: data[10].split(", ")[0],
                data[11].split(", ")[1]: data[12].split(", ")[0],
                data[12].split(", ")[1]: data[13].split(", ")[0],
                data[20].split(", ")[-1]: data[21],
            }
        else:
            live_region_data = {
                data[1].split(", ")[1]: data[2].split(", ")[0],
                data[2].split(", ")[1]: data[3].split(", ")[0],
                data[3].split(", ")[1]: data[4].split(", ")[0],
                data[4].split(", ")[1]: data[5].split(", ")[0],
                data[5].split(", ")[1]: data[6].split(", ")[0],
                data[7].split(", ")[1]: data[8].split(", ")[0],
                data[8].split(", ")[1]: data[9].split(", ")[0],
                data[10].split(", ")[1]: data[11].split(", ")[0],
                data[11].split(", ")[1]: data[12].split(", ")[0],
                data[19].split(", ")[-1]: data[20]
            }

        ip = (live_region_data.get("ip")).split(":")[0]
        rpyc_port = int((live_region_data.get("ip")).split(":")[1])
        web_port = 0
        status = "RUNNING"
        state = 0
        type = 0
        maxHeapMB = float(live_region_data.get("maxHeapMB"))
        memstoreSizeMB = float(live_region_data.get("memstoreSizeMB"))
        numberOfOnlineRegions = float(live_region_data.get("numberOfOnlineRegions"))
        readRequestsCount = float(live_region_data.get("readRequestsCount"))
        numberOfStorefiles = float(live_region_data.get("numberOfStorefiles"))
        numberOfStores = float(live_region_data.get("numberOfStores"))
        usedHeapMB = float(live_region_data.get("usedHeapMB"))
        writeRequestsCount = float(live_region_data.get("writeRequestsCount"))
        storefileSizeMB = float(live_region_data.get("storefileSizeMB"))

        conn = get_postgres_connection()
        cur = conn.cursor()
        sql = "select id from hbase_hbase where ip='{0}' and cluster_id={1} and type=0".format(ip, cluster_id)
        cur.execute(sql)
        row = cur.fetchone()
        if row is None:
            # Inserting hbase_hbase table with hbase jmx values.

            sql = """INSERT INTO hbase_hbase (ip, type, status, state, web_port, rpyc_port, cluster_id, updated_at) VALUES
                    ('{0}', {1}, '{2}', {3}, {4}, {5}, {6}, {7}) RETURNING id;""".format(
                ip,
                type,
                status,
                state,
                web_port,
                rpyc_port,
                cluster_id,
                updated_at)
        else:
            # Updating hbase_hbase table with hbase jmx values.
            id = row[0]

            sql = """UPDATE hbase_hbase set status='{0}', updated_at={1} where id={2} RETURNING id;""".format(status,
                                                                                                                updated_at,
                                                                                                                id)
        hbase_id = execute_hbase_sql(sql)
        metrics_sql = """INSERT INTO hbase_metrics (max_heap, mem_store_size, online_region, read_request, no_store_files, 
    no_stores, updated_at, used_heap, write_request, store_file_size, node_id) VALUES
                        ('{0}', {1}, '{2}', {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}) RETURNING id;""".format(
            maxHeapMB,
            memstoreSizeMB,
            numberOfOnlineRegions,
            readRequestsCount,
            numberOfStorefiles,
            numberOfStores,
            updated_at,
            usedHeapMB,
            writeRequestsCount,
            storefileSizeMB,
            hbase_id)
        execute_hbase_sql(metrics_sql)
    except Exception as e:
        log.error(e)

    if cur is not None and conn is not None:
        cur.close()
        conn.close()


def get_hbase():
    global final_hbase_data
    final_hbase_data = {}
    try:
        while True:
            global updated_at
            updated_at = int(str(time.time()).split(".")[0])
            live_server_info = []
            dead_server_info = []
            global cluster_id

            result = subprocess.check_output([get_hbase_status], stderr=subprocess.STDOUT, shell=True).decode("utf-8")

            result = result.strip().split('\n')
            index = [i for i, s in enumerate(result) if 'active master' in s][0]
            result = result[index:]

            active = (result[0]).strip().split(":", 1)[0]
            if active != "active master":
                cluster_id = get_hbase_db_info(get_system_ip())[1]

                sql = """UPDATE hbase_hbase set status='{0}', state={1}, updated_at={2} WHERE type={3} 
and cluster_id={4} RETURNING id;""".format("SHUTDOWN", 0, updated_at, 1, cluster_id)

                execute_hbase_sql(sql)

                final_hbase_data = {'active': 0}
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

                    no_of_live_servers = int(result[3].split()[0])
                    i = 4
                else:
                    sql = """UPDATE hbase_hbase set status='{0}', state={1}, updated_at={2} where type=1 and cluster_id={3} and 
ip <> '{4}' RETURNING id;""".format("SHUTDOWN", 0, updated_at, cluster_id, active_master_ip)
                    execute_hbase_sql(sql)

                    no_of_live_servers = int(result[2].split()[0])
                    i = 3

                no_of_threadpool = 0
                if no_of_live_servers > 0:

                    no_of_threadpool = int(no_of_live_servers / 10) + 1
                    while no_of_live_servers > 0:
                        key_index = i
                        value_index = i + 1

                        key = (result[key_index]).strip().split()[0]
                        value = (result[value_index]).strip()

                        value = value + ', ip=%s:%s' % (get_ip(key.split(":")[0]), key.split(":")[1])

                        live_server_info.append(value)

                        i = i + 2
                        no_of_live_servers = no_of_live_servers - 1

                if live_server_info:
                    pool = ThreadPool(no_of_threadpool)
                    pool.map(hbase_liveserver_update, live_server_info, 10)
                    pool.close()

                no_of_dead_servers = int((result[i]).split()[0])

                if no_of_dead_servers > 0:
                    while no_of_dead_servers > 0:
                        dead_server = (result[i + 1]).strip().split(",")[0]
                        dead_server_ip = get_ip(dead_server)

                        sql = """UPDATE hbase_hbase set status='{0}', state={1}, updated_at={2} where type=0 
and cluster_id={3} and ip='{4}' RETURNING id;""".format("SHUTDOWN", 0, updated_at,
                                                         cluster_id, dead_server_ip)

                        hbase_id = execute_hbase_sql(sql)

                        metrics_sql = """INSERT INTO hbase_metrics (max_heap, mem_store_size, online_region, read_request, no_store_files, 
                        no_stores, updated_at, used_heap, write_request, store_file_size, node_id) VALUES
                                            ('{0}', {1}, '{2}', {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}) RETURNING id;""".format(
                            0.0, 0.0, 0.0, 0.0, 0.0, 0.0, updated_at, 0.0, 0.0, 0.0, hbase_id)
                        execute_hbase_sql(metrics_sql)

                        dead_server_info.append(dead_server_ip)
                        i = i + 1
                        no_of_dead_servers = no_of_dead_servers - 1

            time.sleep(10)
    except Exception as e:
        log.error(e)


def execute_hbase_sql(sql):
    conn = get_postgres_connection()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    id = (cur.fetchone())[0]
    cur.close()
    conn.close()
    return id
