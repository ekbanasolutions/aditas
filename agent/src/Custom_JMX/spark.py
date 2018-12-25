import subprocess
import time
from multiprocessing.pool import ThreadPool

import requests

from Postgres_connection.connection import get_postgres_connection

from bigdata_logs.logger import getLoggingInstance
log = getLoggingInstance()

get_host_ip = "getent hosts "
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


def execute_spark_sql(sql):
    conn = get_postgres_connection()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    id = (cur.fetchone())[0]
    cur.close()
    conn.close()
    return id


def get_spark_db_info():
    cur = conn = None
    try:
        conn = get_postgres_connection()
        cur = conn.cursor()
        sql = "select ip, cluster_id, web_port from spark_spark where type=1 and state=1"
        cur.execute(sql)
        row = cur.fetchone()
        return row
    except Exception as e:
        log.error(e)

    if cur is not None and conn is not None:
        cur.close()
        conn.close()


def spark_jmx_update(worker):
    cur = conn = None
    try:
        worker_host = worker['host']
        worker_state = worker['state']
        if worker_state == 'ALIVE':
            worker_status = "RUNNING"
        elif worker_state == 'DEAD':
            worker_status = "DEAD"
        else:
            worker_status = "SHUTDOWN"
        worker_cores = float(worker['cores'])
        worker_coresused = float(worker['coresused'])
        worker_coresfree = float(worker['coresfree'])
        worker_memory = float(worker['memory'] / 1024)
        worker_memoryused = float(worker['memoryused'])
        worker_lastheartbeat = worker['lastheartbeat']
        rpyc_port = int(worker['port'])
        web_port = int((worker['webuiaddress']).split(":")[-1])

        conn = get_postgres_connection()
        cur = conn.cursor()
        sql = "select id from spark_spark where ip='{0}' and type=0 and cluster_id={1}".format(worker_host, cluster_id)
        cur.execute(sql)
        row = cur.fetchone()
        if row is None:
            sql = """INSERT INTO spark_spark (ip, type, status, web_port, rpyc_port, state, cluster_id, updated_at) 
    VALUES ('{0}', {1}, '{2}', {3}, {4}, {5}, {6}, {7}) RETURNING id;""".format(worker_host, 0, worker_status, web_port,
                                                                                  rpyc_port, 0, cluster_id,
                                                                                  updated_at)
        else:
            id = row[0]
            sql = """UPDATE spark_spark set status='{0}', state={1}, updated_at={2} where id={3} RETURNING id;""".format(
                worker_status, 0,
                updated_at, id)

        spark_id = execute_spark_sql(sql)
        if worker_status is not 'DEAD':
            metrics_sql = """INSERT INTO spark_metrics (cores_free, cores_used, last_heartbeat, memory_used, total_cores, updated_at, total_memory, node_id) 
        VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}) RETURNING id;""".format(worker_coresfree, worker_coresused,
                                                                                  worker_lastheartbeat, worker_memoryused,
                                                                                  worker_cores,
                                                                                  updated_at,
                                                                                  worker_memory, spark_id)
            execute_spark_sql(metrics_sql)
    except Exception as e:
        log.error(e)

    if cur is not None and conn is not None:
        cur.close()
        conn.close()


def get_spark():
    while True:
        global updated_at
        updated_at = int(str(time.time()).split(".")[0])

        r = None
        global cluster_id
        try:
            workers = None
            spark_info = get_spark_db_info()
            if spark_info:
                master_ip = spark_info[0]
                cluster_id = spark_info[1]
                master_web_port = spark_info[2]
                if master_ip is None:
                    log.info("Spark master ip is None")
                else:
                    url = "http://%s:%s/json/" % (master_ip, master_web_port)
                    r = requests.get(url, verify=False)

                response_json = r.json()
                r.close()

                sql = """UPDATE spark_spark set status='RUNNING', updated_at={0} 
                where type=1 and  state=1 and cluster_id={1} RETURNING id;""".format(updated_at, cluster_id)
                execute_spark_sql(sql)

                if 'workers' not in response_json:
                    if 'masterwebuiurl' in response_json:
                        master_web_url = response_json['masterwebuiurl']
                        master_web_url = master_web_url.replace("//", "").split(":")
                        master_host = master_web_url[1]
                        master_ip = get_ip(master_host)
                        master_web_port = master_web_url[2]
                        url = "http://%s:%d/json" % (master_ip, master_web_port)
                        r = requests.get(url, verify=False)

                        response_json = r.json()
                        r.close()
                        workers = response_json['workers']
                    else:
                        log.error("spark url not working")
                else:
                    workers = response_json['workers']

                no_of_threadpool = int(len(workers) / 10) + 1

                pool = ThreadPool(no_of_threadpool)
                pool.map(spark_jmx_update, workers, 10)
                pool.close()
            else:
                sql = """UPDATE spark_spark set status='SHUTDOWN', updated_at={0} 
where type=1 and  state=1 and cluster_id={1} RETURNING id;""".format(updated_at, cluster_id)
                spark_id = execute_spark_sql(sql)

                metrics_sql = """INSERT INTO spark_metrics (cores_free, cores_used, last_heartbeat, memory_used, total_cores, updated_at, total_memory, node_id) 
                VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}) RETURNING id;""".format(0, 0, 0, 0, 0, updated_at, 0, spark_id)
                execute_spark_sql(metrics_sql)

        except Exception as e:
            sql = """UPDATE spark_spark set status='SHUTDOWN', updated_at={0} 
            where type=1 and  state=1 and cluster_id={1} RETURNING id;""".format(updated_at, cluster_id)
            spark_id = execute_spark_sql(sql)
            metrics_sql = """INSERT INTO spark_metrics (cores_free, cores_used, last_heartbeat, memory_used, total_cores, updated_at, total_memory, node_id) 
                            VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}) RETURNING id;""".format(0, 0, 0, 0, 0, updated_at, 0, spark_id)
            execute_spark_sql(metrics_sql)

        time.sleep(10)
