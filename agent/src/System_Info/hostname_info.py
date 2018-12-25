import subprocess
from bigdata_logs.logger import getLoggingInstance
log = getLoggingInstance()

def get_system_ip():
    try:
        ip = subprocess.check_output(
            ["hostname -i"], stderr=subprocess.STDOUT, shell=True).decode("utf-8")
        ip = ip.strip()
        return ip
    except Exception as e:
        log.error(e)


def get_system_fqdn():
    try:
        fqdn = subprocess.check_output(
            ["hostname -f"], stderr=subprocess.STDOUT, shell=True).decode("utf-8")
        fqdn = fqdn.strip()
        return fqdn
    except Exception as e:
        log.error(e)


def get_system_hostname():
    try:
        hostname = subprocess.check_output(
            ["hostname"], stderr=subprocess.STDOUT, shell=True).decode("utf-8")
        hostname = hostname.strip()
        return hostname
    except Exception as e:
        log.error(e)
