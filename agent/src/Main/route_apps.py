#!/etc/aditas/aditasenv/bin/python

import json
import os
import subprocess
import sys
import threading
import time
import datetime
from multiprocessing import Process

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv(filename='/etc/aditas/agent/conf/agent.env'), override=True)
parent_dir = os.getenv("parent_dir")

sys.path.append(parent_dir)

from bigdata_logs.logger import getLoggingInstance
log = getLoggingInstance()

from API_KEYS.keys import check_apiKey
from Custom_JMX.hdfs import get_hdfs
from Custom_JMX.yarn import get_yarn
from Custom_JMX.hbase import get_hbase
from Custom_JMX.spark import get_spark
from Custom_JMX.elasticsearch import get_elastic_search

from System_Info.hostname_info import get_system_ip
from Postgres_connection.connection import get_postgres_connection

from Linux_service_management.system_statistics import write_system_statistics_history

import custom_app
from custom_requests import request

service_list = []
my_service_process = []

system_ip = get_system_ip()

def home():
    '''
    :return: Urls used for all services
    '''
    path = "Urls used for all services:\n\
            '/kill/service/': 'to kill running service'\n\
            '/hadoop/': 'hadoop urls'\n\
            '/yarn/': 'yarn urls'\n\
            '/hbase/': 'hbase urls'\n\
            '/spark/': 'spark urls'\n\
            '/config': 'config urls'\n\
            '/hdfs/': 'hdfs urls'\n\
            '/es/': 'es urls'\n\
            '/command/': 'basic linux command urls'\n\
            '/system/': 'system urls'"

    return path


def kill_running_service():
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        table_name = loaded_json['table_name']
        if any(table_name in a for a in my_service_process):
            service_tuple = next((i, d) for i, d in enumerate(my_service_process) if '%s' % table_name in d)
            service_index = service_tuple[0]
            value = service_tuple[1][table_name]
            result = kill_service_process(service_index, value)
            return result
    else:
        return api_status


def activate_job():

    def run_job():
        while True:
            check_master_ip()
            time.sleep(15)

    def write_system_statistics():
        while True:
            write_system_statistics_history()
            time.sleep(300)

    def delete_stat():
        try:
            today_date = datetime.date.today()
            if today_date.day > 25:
                today_date += datetime.timedelta(7)
            first_day_of_month = str(today_date.replace(day=1))
            if str(today_date) == first_day_of_month:
                date_to_delete = str(today_date - datetime.timedelta(days=30))
                stat_file_path = parent_dir + '/system_statistics_history/%s.bin' % date_to_delete
                if os.path.exists(stat_file_path):
                    os.remove(stat_file_path)

            tomorrow = datetime.datetime.replace(datetime.datetime.now() + datetime.timedelta(days=1), hour=0, minute=0, second=0)
            delta = tomorrow - datetime.datetime.now()
            time.sleep(delta.seconds)

        except Exception as e:
            log.error(e)

    thread = threading.Thread(target=run_job)
    thread.start()

    system_stat_thread = threading.Thread(target=write_system_statistics)
    system_stat_thread.start()

    delete_one_day_stat = threading.Thread(target=delete_stat)
    delete_one_day_stat.start()


def start_services(table_name):
    try:
        if table_name in service_list:
            method_name = 'get_' + table_name.split("_", 2)[-1]
            possibles = globals().copy()
            possibles.update(locals())
            method = possibles.get(method_name)
            p = Process(target=method)
            p.start()
            my_service_process.append({table_name: p})

        # if "yarn_yarn" in service_list:
        #     p = Process(target=get_yarn)
        #     p.start()
        #     my_service_process.append({'yarn_yarn': p})
    except Exception as e:
        log.error(e)


def check_master_ip():
    try:
        sql = "select st.table_name from administer_services as s join service_table_ref as st " \
              "on s.id=st.service_id join administer_service_cluster_reference as ads " \
              "on s.id=ads.service_id"
        service_table_name = execute_psql(sql)

        service_table_name = [' '.join(item) for item in service_table_name]

        for table_name in service_table_name:
            sql = "select ip from %s where type=1 and state=1" % table_name
            ip_tuple_list = execute_psql(sql)
            ip_list = [' '.join(item) for item in ip_tuple_list]
            if system_ip in ip_list:
                if not any(table_name in a for a in my_service_process):
                    service_list.append(table_name)
                    start_services(table_name)
        for t in service_list:
            if not t in service_table_name:
                service_tuple = next((i, d) for i, d in enumerate(my_service_process) if '%s' % t in d)
                service_index = service_tuple[0]
                value = service_tuple[1][t]
                kill_service_process(service_index, value)

    except Exception as e:
        log.error(e)


def kill_service_process(service_index, value):
    try:
        value.terminate()
        my_service_process.pop(service_index)
        return '{"success": 0, "msg": ["It is success but sending 0!!!"]}'
    except Exception as e:
        return '{"success": 0, "msg": ["service not killed successfully!!!"]}'


def execute_psql(sql):
    conn = get_postgres_connection()
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def check_running_port(port):
    cmd = "netstat -tulpn | grep %d" % int(port)
    try:
        subprocess.check_output(cmd, shell=True).decode("utf-8")
        exists = True
    except subprocess.CalledProcessError as e:
        exists = False

    if not exists:
        return False
    else:
        return True


if __name__ == '__main__':
    '''
    Will run flask app from the main module at localhost with port 11605
    '''
    try:
        service_thread = threading.Thread(target=activate_job)
        service_thread.start()

        port = 11605
        while check_running_port(port):
            port = port + 1

        update_port_sql = """UPDATE administer_nodes set port={0} where ip='{1}' RETURNING id;""" \
                .format(port, system_ip)

        conn = get_postgres_connection()
        cur = conn.cursor()
        cur.execute(update_port_sql)
        conn.commit()
        cur.close()
        conn.close()

        custom_app.run(host='0.0.0.0', port=port)
        # app.run(debug=True, host='0.0.0.0', port=11605)
    except Exception as e:
        log.error(e)

