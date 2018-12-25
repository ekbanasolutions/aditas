import datetime
import json
import os
import subprocess
import time
from multiprocessing.pool import ThreadPool

import requests

from Postgres_connection.connection import get_postgres_connection

from bigdata_logs.logger import getLoggingInstance
log = getLoggingInstance()

get_host_ip = "getent hosts "
get_status_cmd = "lsof -t -i:"

hadoop_bin=os.getenv("hadoop_bin_dir")

get_hdfs_master_cmd = "%shdfs haadmin -getAllServiceState" % hadoop_bin
get_service_state_cmd = "%shdfs haadmin -getServiceState " % hadoop_bin
get_service_name_cmd = "%shdfs getconf -confKey dfs.nameservices" % hadoop_bin
get_service_id_cmd = "%shdfs getconf -confKey dfs.ha.namenodes." % hadoop_bin
get_service_address_cmd = "%shdfs getconf -confKey dfs.namenode.https-address." % hadoop_bin

json_livenodes = None
json_deadnodes = None

master_id = None
master_ip = None
master_web_port = None
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


def get_ha_state(state):
    if state == 'active':
        return 1
    elif state == 'standby':
        return 0
    else:
        return 0


def execute_hdfs_sql(sql):
    conn = get_postgres_connection()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    id = (cur.fetchone())[0]
    cur.close()
    conn.close()
    return id


def hdfs_liveserver_update(livenode):
    cur = conn = None
    try:
        gb_value = 1073741824

        xferaddr = json_livenodes[livenode]['xferaddr']
        ip = xferaddr.split(":")[0]

        capacity = json_livenodes[livenode]['capacity']
        capacity = float(capacity / gb_value)

        nondfsusedspace = json_livenodes[livenode]['nonDfsUsedSpace']
        nondfsusedspace = float(nondfsusedspace / gb_value)

        numblocks = json_livenodes[livenode]['numBlocks']

        usedspace = json_livenodes[livenode]['usedSpace']
        usedspace = int(usedspace / gb_value)
        usedspace_oftotal = float(usedspace / capacity)

        conn = get_postgres_connection()
        cur = conn.cursor()
        sql = "select id from hdfs_hdfs where ip='%s' and type=0 and cluster_id='%s'" % (ip, cluster_id)
        cur.execute(sql)
        row = cur.fetchone()
        if row is None:
            sql = """INSERT INTO hdfs_hdfs (ip, type, status, state, cluster_id, updated_at, web_port, rpyc_port, safemode) VALUES('{0}', {1}, '{2}', {3}, {4}, {5}, {6}, {7}, {8}) RETURNING id;""" \
                .format(ip, 0, "RUNNING", 0, cluster_id, updated_at, 0, 0, 0)
        else:
            id = row[0]
            sql = """UPDATE hdfs_hdfs set type={0}, status='{1}', state={2}, updated_at={3} where id={4} RETURNING id;""" \
                .format(0, "RUNNING", 0, updated_at, id)

        node_id = execute_hdfs_sql(sql)
        metrics_sql = """INSERT INTO hdfs_metrics (capacity, non_dfs_used, num_blocks, used_space, decommissioned, 
        updated_at, node_id) VALUES({0}, {1}, {2}, {3}, {4}, {5}, {6}) RETURNING id;""".format(capacity,
                                                                                                 nondfsusedspace,
                                                                                                 numblocks,
                                                                                                 usedspace_oftotal,
                                                                                                 0,
                                                                                                 updated_at,
                                                                                                 node_id)
        execute_hdfs_sql(metrics_sql)
    except Exception as e:
        log.error(e)

    if cur is not None and conn is not None:
        cur.close()
        conn.close()


def hdfs_deadnode_update(deadnode):
    cur = conn = None
    try:
        xferaddr_deadnode = json_deadnodes[deadnode]['xferaddr']
        ip = xferaddr_deadnode.split(":")[0]

        conn = get_postgres_connection()
        cur = conn.cursor()
        sql = "select id from hdfs_hdfs where ip='%s' and type=0 and cluster_id='%s'" % (ip, cluster_id)
        cur.execute(sql)
        row = cur.fetchone()
        if row is None:
            sql = """INSERT INTO hdfs_hdfs (ip, type, status, state, cluster_id, updated_at, web_port, rpyc_port, safemode) VALUES('{0}', {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}) RETURNING id;""" \
                .format(ip, 0, "SHUTDOWN", 0, cluster_id, updated_at, 0, 0, 0)
        else:
            node_id = row[0]
            sql = """UPDATE hdfs_hdfs set status='{0}', updated_at={1} WHERE id={2} RETURNING id;""". \
                format("SHUTDOWN", updated_at, node_id)

        node_id = execute_hdfs_sql(sql)

        metrics_sql = """INSERT INTO hdfs_metrics (capacity, non_dfs_used, num_blocks, used_space, decommissioned, 
            updated_at, node_id) VALUES({0}, {1}, {2}, {3}, {4}, {5}, {6}) RETURNING id;""".format(0, 0, 0, 0, 0, updated_at, node_id)
        execute_hdfs_sql(metrics_sql)
    except Exception as e:
        log.error(e)

    if cur is not None and conn is not None:
        cur.close()
        conn.close()


def update_namenode_info(updated_at=None):
    cur = conn = None
    try:
        if updated_at is None:
            updated_at = int(str(time.time()).split(".")[0])

        result = subprocess.check_output(
            [get_hdfs_master_cmd], stderr=subprocess.STDOUT, shell=True).decode("utf-8")
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
            sql = "select id, cluster_id, ip, web_port from hdfs_hdfs where ip='%s' and type=1" % ip
            cur.execute(sql)
            row = cur.fetchone()

            global cluster_id
            global master_id
            global master_ip
            global master_web_port

            id = row[0]
            cluster_id = row[1]

            if state == "active":
                status = "RUNNING"
                master_ip = row[2]
                master_web_port = row[3]
                master_id = id
            elif state == "standby":
                status = "RUNNING"
            else:
                status = "SHUTDOWN"

            sql = """UPDATE hdfs_hdfs set status='{0}', state={1}, updated_at={2} WHERE id={3} RETURNING id;""". \
                format(status, get_ha_state(state),
                       updated_at,
                       id)

            execute_hdfs_sql(sql)

    except Exception as e:
        log.error(e)

    if cur is not None and conn is not None:
        cur.close()
        conn.close()

def get_hdfs():
    while True:
        global updated_at
        updated_at = int(str(time.time()).split(".")[0])

        # Updating Namenode Info
        update_namenode_info()

        beans = None
        try:
            url = "https://%s:%s/jmx?qry=Hadoop:service=NameNode,name=NameNodeInfo" % (master_ip, master_web_port)
            r = requests.get(url, verify=False)
            response_json = r.json()
            beans = response_json['beans']
            r.close()
        except Exception as e:
            log.error(e)

        try:
            if beans:
                for bean in beans:
                    safemode = bean['Safemode']
                    if safemode != "":
                        sql = """UPDATE hdfs_hdfs set safemode={0}, updated_at={1} WHERE id={2} RETURNING id;""". \
                            format(1, updated_at, master_id)
                        execute_hdfs_sql(sql)
                    else:
                        sql = """UPDATE hdfs_hdfs set safemode={0}, updated_at={1} WHERE id={2} RETURNING id;""". \
                            format(0, updated_at, master_id)
                        execute_hdfs_sql(sql)

                    decommissioning_nodes = bean['DecomNodes']
                    json_decomnodes = json.loads(decommissioning_nodes)
                    if json_decomnodes:
                        xferaddr = json_decomnodes[decommissioning_nodes]['xferaddr']
                        ip = xferaddr.split(":")[0]

                        conn = get_postgres_connection()
                        cur = conn.cursor()
                        sql = "select id from hdfs_metrics where ip='%s' and type=0 and cluster_id='%s'" % (ip, cluster_id)
                        cur.execute(sql)
                        row = cur.fetchone()
                        if row is None:
                            sql = """INSERT INTO hdfs_hdfs (ip, type, status, state, cluster_id, updated_at, web_port, rpyc_port, safemode) VALUES({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}) RETURNING id;""" \
                                .format(ip, 0, "SHUTDOWN", 0, cluster_id, updated_at, 0, 0, 0)
                            hdfs_id = execute_hdfs_sql(sql)
                        else:
                            hdfs_id = row[0]

                        metrics_sql = """INSERT INTO hdfs_metrics (decommissioned, updated_at, node_id) VALUES({0}, {1}, {2}) RETURNING id;""" \
                            .format(1, updated_at, hdfs_id)
                        execute_hdfs_sql(metrics_sql)
                        cur.close()
                        conn.close()

                    livenodes = bean['LiveNodes']
                    global json_livenodes
                    json_livenodes = json.loads(livenodes)

                    if json_livenodes:
                        no_of_livenodes_threadpool = int(len(json_livenodes) / 10) + 1

                        pool = ThreadPool(no_of_livenodes_threadpool)
                        pool.map(hdfs_liveserver_update, json_livenodes, 10)
                        pool.close()

                    deadnodes = bean['DeadNodes']
                    global json_deadnodes
                    json_deadnodes = json.loads(deadnodes)
                    if json_deadnodes:
                        no_of_deadnode_threadpool = int(len(json_deadnodes) / 10) + 1

                        pool = ThreadPool(no_of_deadnode_threadpool)
                        pool.map(hdfs_deadnode_update, json_deadnodes, 10)
                        pool.close()
        except Exception as e:
            log.error(e)

        time.sleep(10)