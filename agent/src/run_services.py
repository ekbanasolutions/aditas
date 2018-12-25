import json
import os
import subprocess
import sys
import time

from bigdata_logs.logger import getLoggingInstance

log = getLoggingInstance()

parent_dir = os.getenv("parent_dir")
sys.path.append(parent_dir)

from Postgres_connection.connection import get_postgres_connection


def run_bigdata_services(cmd, success_msg, error_msg):
    '''
    :param cmd: command to execute
    :param err_msg: message if error is occured
    :return: result of the command after execution
    '''
    result = None
    success_msg = success_msg.strip()
    try:
        result = subprocess.check_output(
            [cmd], stderr=subprocess.STDOUT, shell=True).decode("utf-8")
        result = result.strip().replace("\n", ", ")
    except subprocess.CalledProcessError as e:
        log.error("Error while executing command: %s" % cmd)
        log.error(e.stdout)
        return '{"success": 0, "msg": ["%s"]}' % result

    log.info("%s" % success_msg)

    return '{"success": 1, "msg": ["%s"]}' % success_msg


def run_basic_services(cmd):
    '''
    :param cmd: command to execute
    :param err_msg: message if error is occured
    :return: result of the command after execution
    '''
    try:
        subprocess.check_output(
            cmd, stderr=subprocess.STDOUT, shell=True,
            universal_newlines=True)
    except subprocess.CalledProcessError as exc:
        log.error("\nError while executing command: %s\n" % cmd)
        log.error(exc.stdout)
        return exc.output
    else:
        return "success"


def change_to_ip(dns):
    '''
    Changes dns name to its corresponding ip address
    :param dns: dns name
    :return: ip address of the dns name
    '''
    try:
        dns_result = subprocess.check_output(
            ["getent hosts " + dns + " | awk '{ print $1 }'"], shell=True).decode("utf-8")

    except subprocess.CalledProcessError as e:
        log.error("\nError while chaning dns to ip\n")
        log.error(e.stdout)
        return 'Error changing dns to ip'

    log.info("\nSuccessully changed dns to its corresponding ip\n")
    return str(dns_result).strip()


# Command to check if a service port is running
get_status_cmd = "lsof -t -i:"
get_es_status_cmd = "netstat -tulpn | grep "


def check_status(web_port, ipc_port):
    ipc_cmd = get_es_status_cmd + "%d" % int(ipc_port)
    web_cmd = get_es_status_cmd + "%d" % int(web_port)
    try:
        subprocess.check_output(web_cmd, shell=True).decode("utf-8")
        web_status = True
    except subprocess.CalledProcessError as e:
        web_status = False

    try:
        subprocess.check_output(ipc_cmd, shell=True).decode("utf-8")
        ipc_status = True
    except subprocess.CalledProcessError as e:
        ipc_status = False

    if not web_status or not ipc_status:
        return False
    else:
        return True


def check_yarn_status(web_port, ipc_port):
    ipc_cmd = get_es_status_cmd + "%d" % int(ipc_port)
    web_cmd = get_es_status_cmd + "%d" % int(web_port)
    try:
        subprocess.check_output(web_cmd, shell=True).decode("utf-8")
        web_status = True
    except subprocess.CalledProcessError as e:
        web_status = False

    try:
        subprocess.check_output(ipc_cmd, shell=True).decode("utf-8")
        ipc_status = True
    except subprocess.CalledProcessError as e:
        ipc_status = False

    if not web_status and not ipc_status:
        return False
    else:
        return True


def change_service_status(table_name, status, id):
    updated_at = int(str(time.time()).split(".")[0])
    try:
        conn = get_postgres_connection()
        cur = conn.cursor()
        sql = """UPDATE {0} set status='{1}', updated_at={2} WHERE id={3}""".format(table_name, status, updated_at, id)
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        log.error(e)


def confirm_stop(result, table_name, id, web_port, rpyc_port):
    try:
        check_result = json.loads(result)
        if check_result["success"]:
            count = 1
            while count <= 20:
                if table_name == "yarn_yarn":
                    c_status = check_yarn_status(web_port, rpyc_port)
                else:
                    c_status = check_status(web_port, rpyc_port)

                if c_status:
                    if count == 20:
                        check_result["success"] = 2
                        return json.dumps(check_result)
                else:
                    check_result["success"] = 1
                    change_service_status(table_name, "SHUTDOWN", id)
                    return json.dumps(check_result)
                count = count + 1
                time.sleep(1)
        else:
            return json.dumps(check_result)
    except Exception as e:
        log.error(e)


def confirm_start(result, table_name, id, web_port, rpyc_port):
    try:
        check_result = json.loads(result)
        if check_result["success"]:
            count = 1
            while count <= 20:
                if table_name == "yarn_yarn":
                    c_status = check_yarn_status(web_port, rpyc_port)
                else:
                    c_status = check_status(web_port, rpyc_port)

                if c_status:
                    check_result["success"] = 1
                    change_service_status(table_name, "RUNNING", id)
                    return json.dumps(check_result)
                else:
                    if count == 20:
                        check_result["success"] = 0
                        check_result["msg"] = ["Error detecting if service is started successfully, check manually!!!"]
                        return json.dumps(check_result)
                count = count + 1
                time.sleep(1)
        else:
            return json.dumps(check_result)
    except Exception as e:
        log.error(e)


def get_service_status(sql):
    try:
        conn = get_postgres_connection()
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row
    except Exception as e:
        log.error(e)


