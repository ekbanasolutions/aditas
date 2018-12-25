import datetime
import json
import time
from multiprocessing.pool import ThreadPool

import requests

from Postgres_connection.connection import get_postgres_connection

from bigdata_logs.logger import getLoggingInstance

log = getLoggingInstance()


def get_es_db_info():
    try:
        conn = get_postgres_connection()
        cur = conn.cursor()
        sql = "select ip, cluster_id, web_port from elastic_search_elastic_search " \
              "where type=1 and state=1"
        cur.execute(sql)
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row
    except Exception as e:
        log.error(e)


def get_es_db_standby():
    try:
        conn = get_postgres_connection()
        cur = conn.cursor()
        sql = "select ip, cluster_id, web_port from elastic_search_elastic_search " \
              "where type=1 and state=0"
        cur.execute(sql)
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row
    except Exception as e:
        log.error(e)


def drop_master(sql):
    try:
        conn = get_postgres_connection()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        log.error(e)


def es_jmx_update(a):
    roles = response_json[a]["roles"]
    cpu_percent = response_json[a]["os"]["cpu"]["percent"]
    ip = response_json[a]["ip"].split(":")[0]

    total_mem = response_json[a]["os"]["mem"]["total_in_bytes"] / (1024 * 1024)
    free_mem = response_json[a]["os"]["mem"]["free_percent"]
    used_mem = response_json[a]["os"]["mem"]["used_percent"]

    swap_total_mem = response_json[a]["os"]["swap"]["total_in_bytes"] / (1024 * 1024)
    swap_free_mem = response_json[a]["os"]["swap"]["free_in_bytes"] / (1024 * 1024)
    swap_used_mem = response_json[a]["os"]["swap"]["used_in_bytes"] / (1024 * 1024)

    conn = get_postgres_connection()
    cur = conn.cursor()

    if 'master' in roles:
        if master == ip:
            # master_state = "active"
            master_state = 1
        else:
            # master_state = "inactive"
            master_state = 0

        sql = "select id from elastic_search_elastic_search where ip='{0}' and type=1 and cluster_id={1}".format(ip, cluster_id)
        cur.execute(sql)
        row = cur.fetchone()

        if row is None:
            sql = """INSERT INTO elastic_search_elastic_search (ip, type, status, web_port, rpyc_port, state, cluster_id, updated_at) 
        VALUES ('{0}', {1}, '{2}', {3}, {4}, {5}, {6}, {7}) RETURNING id;""".format(ip,
                                                                                      1,
                                                                                      "RUNNING",
                                                                                      master_web_port,
                                                                                      master_web_port,
                                                                                      master_state,
                                                                                      cluster_id,
                                                                                      updated_at)
        else:
            id = row[0]
            sql = """UPDATE elastic_search_elastic_search set status='{0}', state={1}, updated_at={2} where id={3} RETURNING id;""" \
                .format("RUNNING", master_state, updated_at, id)

        execute_es_sql(sql)
    else:
        sql = "select id from elastic_search_elastic_search where ip='{0}' and type=0 and cluster_id={1}".format(ip, cluster_id)
        cur.execute(sql)
        row = cur.fetchone()
        if row is None:
            sql = """INSERT INTO elastic_search_elastic_search (ip, type, status, web_port, rpyc_port, state, cluster_id, updated_at) 
    VALUES ('{0}', {1}, '{2}', {3}, {4}, {5}, {6}, {7}) RETURNING id;""".format(ip,
                                                                                  0,
                                                                                  "RUNNING",
                                                                                  0,
                                                                                  0,
                                                                                  0,
                                                                                  cluster_id,
                                                                                  updated_at)
        else:
            id = row[0]
            sql = """UPDATE elastic_search_elastic_search set status='{0}', state={1}, updated_at={2} where id={3} RETURNING id;""" \
                .format("RUNNING", 0, updated_at, id)

        es_id = execute_es_sql(sql)
        metrics_sql = """INSERT INTO elastic_search_metrics (cpu_percent, total_memory, free_memory, used_memory, swap_total_memory, 
    swap_used_memory, swap_free_memory, updated_at, node_id) VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}) RETURNING id;""".format(cpu_percent,
                                                                                                                                            total_mem,
                                                                                                                                            free_mem,
                                                                                                                                            used_mem,
                                                                                                                                            swap_total_mem,
                                                                                                                                            swap_used_mem,
                                                                                                                                            swap_free_mem,
                                                                                                                                            updated_at,
                                                                                                                                            es_id)
        execute_es_sql(metrics_sql)
        cur.close()
        conn.close()


def get_fake_master_standby(db_master_ip, all_master_url):
    fake_masters = []
    try:
        db_standby_ip = get_es_db_standby()
        if db_standby_ip is not None:
            db_standby_ip = db_standby_ip[0]

        all_masters_stat = requests.get(all_master_url, verify=False)

        response = all_masters_stat.content.decode('utf-8')
        response = response.splitlines()
        masters = []

        for item in response:
            item1 = item.split(" ")
            str_list = list(filter(None, item1))
            if 'm' in str_list[7]:
                # master_name = str_list[-1]
                master_ip = str_list[0]
                masters.append(master_ip)

        if db_master_ip not in masters:
            fake_masters.append(db_master_ip)
        if db_standby_ip is not None:
            if db_standby_ip not in masters:
                fake_masters.append(db_standby_ip)

    except Exception as e:
        log.error(e)

    return fake_masters


def get_elastic_search():
    while True:
        global updated_at
        updated_at = int(str(time.time()).split(".")[0])

        global cluster_id
        global master_web_port
        es_info = get_es_db_info()
        if es_info:
            master_ip = es_info[0]
            cluster_id = es_info[1]
            master_web_port = es_info[2]
            if master_ip is None:
                log.warn("Master ip of es is None")
            else:
                try:
                    node_url = "http://%s:%s/_nodes/stats/os" % (master_ip, master_web_port)
                    master_url = "http://%s:%s/_cat/master" % (master_ip, master_web_port)
                    get_all_masters_url = "http://%s:%s/_cat/nodes" % (master_ip, master_web_port)

                    node_stat = requests.get(node_url, verify=False)
                    master_stat = requests.get(master_url, verify=False)
                    fake_masters = get_fake_master_standby(master_ip, get_all_masters_url)

                    global response_json

                    response_json = json.loads(node_stat.content.decode('utf-8'))["nodes"]
                    master_data = master_stat.content.decode('utf-8')

                    global master
                    master = master_data.split(" ")[2]

                    no_of_threadpool = int(len(response_json) / 10) + 1

                    pool = ThreadPool(no_of_threadpool)
                    pool.map(es_jmx_update, response_json, 10)
                    pool.close()

                    node_stat.close()
                    master_stat.close()

                    if fake_masters:
                        for master_ip in fake_masters:
                            sql = "DELETE FROM elastic_search_elastic_search WHERE ip='%s' and type=1" % master_ip
                            drop_master(sql)

                except Exception as e:
                    sql = """UPDATE elastic_search_elastic_search set status='SHUTDOWN', updated_at={0} 
                                where type=1 and  state=1 and cluster_id={1} RETURNING id;""".format(updated_at,
                                                                                                     cluster_id)
                    es_id = execute_es_sql(sql)
                    metrics_sql = """INSERT INTO elastic_search_metrics (cpu_percent, total_memory, free_memory, used_memory, swap_total_memory, 
                        swap_used_memory, swap_free_memory, updated_at, node_id) VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}) RETURNING id;""".format(
                        0, 0, 0, 0, 0, 0, 0, updated_at, es_id)
                    execute_es_sql(metrics_sql)
        else:
            try:
                sql = """UPDATE elastic_search_elastic_search set status='SHUTDOWN', updated_at={0} 
                where type=1 and  state=1 and cluster_id={1} RETURNING id;""".format(updated_at, cluster_id)
                es_id = execute_es_sql(sql)
                metrics_sql = """INSERT INTO elastic_search_metrics (cpu_percent, total_memory, free_memory, used_memory, swap_total_memory, 
                                        swap_used_memory, swap_free_memory, updated_at, node_id) VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}) RETURNING id;""".format(
                    0, 0, 0, 0, 0, 0, 0, updated_at, es_id)
                execute_es_sql(metrics_sql)
            except Exception as e:
                log.error("check database if es info is available")
                log.error(e)

        time.sleep(10)


def execute_es_sql(sql):
    conn = get_postgres_connection()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    id = (cur.fetchone())[0]
    cur.close()
    conn.close()
    return id
