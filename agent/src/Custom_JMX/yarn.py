import ast
import json
import os
import re
import subprocess
import time
from multiprocessing.pool import ThreadPool

from Postgres_connection.connection import get_postgres_connection

from bigdata_logs.logger import getLoggingInstance
log = getLoggingInstance()

hadoop_bin=os.getenv("hadoop_bin_dir")

get_yarn_cmd = "%syarn node -all -list" % hadoop_bin
get_node_info = "%syarn node -status " % hadoop_bin
get_yarn_master_cmd = "%syarn rmadmin -getAllServiceState" % hadoop_bin
get_nm_address_cmd = "%shdfs getconf -confKey yarn.nodemanager.address" % hadoop_bin
get_host_ip = "getent hosts "
get_status_cmd = "lsof -t -i:"
cluster_id = 0
rpyc_port = 0
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


def set_running_rpyc_port(result):
    for r in result:
        r = r.strip().split('\t')
        r = r[:-1]
        ipc_port = r[0].strip().split(':')[1]
        status = r[1].strip()
        if status == "RUNNING":
            global rpyc_port
            rpyc_port = ipc_port
            break


def get_yarn():
    try:
        while True:
            global updated_at
            updated_at = int(str(time.time()).split(".")[0])

            # Updating Resource Manager JMX
            update_rm_info()

            # Updating Node Manager JMX

            i = 0

            result = subprocess.check_output(
                [get_yarn_cmd], stderr=subprocess.STDOUT, shell=True).decode("utf-8")

            result = result.strip().splitlines()

            for index, value in enumerate(result):
                if value.__contains__("Node-Id"):
                    i = index + 1
                    break

            result = result[i:]

            set_running_rpyc_port(result)

            no_of_threadpool = int(len(result) / 10) + 1

            pool = ThreadPool(no_of_threadpool)
            pool.map(yarn_jmx_update, result, 10)
            pool.close()

            time.sleep(10)
    except Exception as e:
        log.error(e)


def yarn_jmx_update(r):
    cur = conn = None
    try:
        r = r.strip().split('\t')
        r = r[:-1]
        host = r[0].strip().split(':')[0]
        ip = get_ip(host)
        ipc_port = r[0].strip().split(':')[1]
        status = r[1].strip()
        web_port = r[2].strip().split(':')[1]

        if ipc_port == rpyc_port:
            node_info = get_yarn_info(host, rpyc_port)
            node_info = ast.literal_eval(node_info)
            insert_update_yarn(ip, node_info, rpyc_port, web_port)
        else:
            conn = get_postgres_connection()
            cur = conn.cursor()
            sql = "select id from yarn_yarn where ip='%s' and cluster_id=%d and type=0" % (ip, cluster_id)
            cur.execute(sql)
            row = cur.fetchone()
            if row is None:
                sql = """INSERT INTO yarn_yarn (ip, type, status, state, web_port, rpyc_port,
                                    cluster_id, updated_at) VALUES
                                    ('{0}', {1}, '{2}', {3}, {4}, {5}, {6}, {7}) RETURNING id;""".format(ip,
                                                                                                           0,
                                                                                                           status,
                                                                                                           0,
                                                                                                           web_port,
                                                                                                           ipc_port,
                                                                                                           cluster_id,
                                                                                                           updated_at)
            else:
                # Updating yarn_yarn table with yarn jmx values.
                id = row[0]

                sql = """UPDATE yarn_yarn set type={0}, status='{1}', state={2}, updated_at={3} where id={4} RETURNING id;""" \
                    .format(0, status, 0, updated_at, id)

            yarn_id = execute_yarn_sql(sql)

            metrics_sql = """INSERT INTO yarn_metrics (cpu_capacity, cpu_used, last_health_update, memory_capacity, memory_used, 
                    rack, updated_at, node_id) VALUES({0}, {1}, '{2}', {3}, {4}, '{5}', {6}, {7}) RETURNING id;""".format(0, 0, 0, 0, 0, 0, updated_at, yarn_id)
            execute_yarn_sql(metrics_sql)
    except Exception as e:
        log.error(e)

    if cur is not None and conn is not None:
        cur.close()
        conn.close()


def insert_update_yarn(ip, node_info, rpyc_port, web_port):
    cur = conn = None
    try:
        type = 0
        status = node_info.get("Node-State")
        state = 0
        cpu_capacity = float((node_info.get("CPU-Capacity")).split()[0])
        cpu_used = float((node_info.get("CPU-Used")).split()[0])
        last_health_update = node_info.get("Last-Health-Update")
        memory_capacity = [float(s) for s in re.findall(r'-?\d+\.?\d*', str(node_info.get("Memory-Capacity")))][0]
        memory_used = [float(s) for s in re.findall(r'-?\d+\.?\d*', str(node_info.get("Memory-Used")))][0]
        rack = node_info.get("Rack")
        conn = get_postgres_connection()
        cur = conn.cursor()
        sql = "select id from yarn_yarn where ip='%s' and cluster_id=%d and type=0" % (ip, cluster_id)
        cur.execute(sql)
        row = cur.fetchone()
        if row is None:
            # Inserting yarn_yarn table with yarn jmx values.

            sql = """INSERT INTO yarn_yarn (ip, type, status, state, web_port, rpyc_port,
                    cluster_id, updated_at) VALUES
                    ('{0}', {1}, '{2}', {3}, {4}, {5}, {6}, {7}) RETURNING id;""".format(ip,
                                                                              type,
                                                                              status,
                                                                              state,
                                                                              web_port,
                                                                              rpyc_port,
                                                                              cluster_id,
                                                                              updated_at)
        else:
            # Updating yarn_yarn table with yarn jmx values.
            id = row[0]

            sql = """UPDATE yarn_yarn set type={0}, status='{1}', state={2}, updated_at={3} where id={4} RETURNING id;""" \
                .format(type, status, state, updated_at, id)

        yarn_id = execute_yarn_sql(sql)
        
        metrics_sql = """INSERT INTO yarn_metrics (cpu_capacity, cpu_used, last_health_update, memory_capacity, memory_used, 
    rack, updated_at, node_id) VALUES({0}, {1}, '{2}', {3}, {4}, '{5}', {6}, {7}) RETURNING id;""".format(cpu_capacity,
                                                                                  cpu_used,
                                                                                  last_health_update,
                                                                                  memory_capacity,
                                                                                  memory_used,
                                                                                  rack,
                                                                                  updated_at,
                                                                                  yarn_id)
        execute_yarn_sql(metrics_sql)
    except Exception as e:
        log.error(e)

    if cur is not None and conn is not None:
        cur.close()
        conn.close()


def execute_yarn_sql(sql):
    cur = conn = None
    id = None
    try:
        conn = get_postgres_connection()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        id = (cur.fetchone())[0]
    except Exception as e:
        log.error(e)

    if cur is not None and conn is not None:
        cur.close()
        conn.close()

    return id


def get_yarn_info(host, port):
    try:
        node_info = {}
        cmd = get_node_info + "%s:%s | sed '1d'" % (host, port)
        result = subprocess.check_output(
            [cmd], stderr=subprocess.STDOUT, shell=True).decode("utf-8")
        result = result.strip().splitlines()
        result = result[1:]
        for r in result:
            r = r.strip().split(':', 1)
            key = r[0]
            value = r[1]
            key = key.strip()
            value = value.strip()
            node_info[key] = value
        return json.dumps(node_info)
    except Exception as e:
        log.error(e)


def get_rm_state(state):
    if state == 'active':
        return 1
    elif state == 'standby':
        return 0
    else:
        return 0


def update_rm_info(updated_at=None):
    cur = conn = None
    try:
        if updated_at is None:
            updated_at = int(str(time.time()).split(".")[0])

        result = subprocess.check_output(
            [get_yarn_master_cmd], stderr=subprocess.STDOUT, shell=True).decode("utf-8")
        result = result.strip().split("\n")

        [result.remove(result[i]) for i, s in enumerate(result) if 'Retrying connect to server' in s]

        result = result[-2:]
        for r in result:
            r = r.strip().split("                              ")
            host = ((r[0]).split(":")[0]).strip()
            state = (r[1]).strip()

            ip = get_ip(host)

            conn = get_postgres_connection()
            cur = conn.cursor()
            sql = "select id, cluster_id from yarn_yarn where ip='%s' and type=1" % ip
            cur.execute(sql)
            row = cur.fetchone()
            id = row[0]
            global cluster_id
            cluster_id = row[1]

            cur.close()
            conn.close()

            if state == "active" or state == "standby":
                status = "RUNNING"
            else:
                status = "SHUTDOWN"

            sql = """UPDATE yarn_yarn set status='{0}', state={1}, updated_at={2} WHERE id={3} RETURNING id;""". \
                format(status, get_rm_state(state),
                       updated_at,
                       id)

            execute_yarn_sql(sql)
    except Exception as e:
        log.error(e)

    if cur is not None and conn is not None:
        cur.close()
        conn.close()