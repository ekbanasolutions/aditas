import ast
import csv
import json
import os
import time
from datetime import date, timedelta, datetime

import psutil
from custom_requests import request

from API_KEYS.keys import check_apiKey
# from Basic_linux_commands.make_folder import make_directory
from bigdata_logs.logger import getLoggingInstance

log = getLoggingInstance()

parent_dir = os.getenv("parent_dir")
user_pass = os.getenv("user_pass")


def get_total_memory():
    memory_info = psutil.virtual_memory()
    total_memory = memory_info.total / (1000 * 1000 * 1000)
    return total_memory


def get_total_disk():
    disk_info = psutil.disk_usage('/')
    total_disk = disk_info.total / (1000 * 1000 * 1000)
    return total_disk


def system_home():
    '''
    :return: Url of system statistics
    '''
    return '<h3>System Statistics Urls</h3>' + \
           'To get total memory & total disk: <font color="green">/system/total/space/</font> </br>' \
           'To get system statistics: <font color="green">/system/statistics/</font>'


def get_total_space():
    log.info("\nGetting Total Memory and Disk space\n")
    try:
        header_key = request.headers.get('API-KEY')
        api_status = check_apiKey(header_key)
        if api_status == 'success':
            total_memory = get_total_memory()
            total_disk = get_total_disk()
            # log.info("Total Memory: %d GB && Total Disk: %d GB" % (total_memory, total_disk))
            return '{"total_memory": %d, "total_disk": %d}' % (total_memory, total_disk)
        else:
            return api_status
    except Exception as e:
        log.error("Error in list_dir()")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e


def get_memory_usage():
    """
    Return statistics about system memory usage as a namedtuple including the following fields, expressed in bytes:

         - total:
           total physical memory available.

         - available:
           the memory that can be given instantly to processes without the
           system going into swap.
           This is calculated by summing different memory values depending
           on the platform and it is supposed to be used to monitor actual
           memory usage in a cross platform fashion.

         - percent:
           the percentage usage calculated as (total - available) / total * 100

         - used:
            memory used, calculated differently depending on the platform and
            designed for informational purposes only:
            macOS: active + inactive + wired
            BSD: active + wired + cached
            Linux: total - free

         - free:
           memory not being used at all (zeroed) that is readily available;
           note that this doesn't reflect the actual memory available
           (use 'available' instead)

        ######################################################################################

    Return system swap memory statistics as a namedtuple including the following fields:

     - total:   total swap memory in bytes
     - used:    used swap memory in bytes
     - free:    free swap memory in bytes
     - percent: the percentage usage

    """

    virtual_memory_info = psutil.virtual_memory()
    v_total = virtual_memory_info.total / (1000 * 1000 * 1000)
    v_available = virtual_memory_info.available / (1000 * 1000 * 1000)
    v_used = virtual_memory_info.used / (1000 * 1000 * 1000)
    v_free = virtual_memory_info.free / (1000 * 1000 * 1000)
    v_buffer = virtual_memory_info.buffers / (1000 * 1000 * 1000)
    v_cached = virtual_memory_info.cached / (1000 * 1000 * 1000)
    v_shared = virtual_memory_info.shared / (1000 * 1000 * 1000)

    v_memory_info = {"total": v_total, "available": v_available, "used": v_used, "free": v_free,
                     "buffer": v_buffer, "cached": v_cached, "shared": v_shared}

    swap_memory_info = psutil.swap_memory()
    s_total = swap_memory_info.total / (1000 * 1000 * 1000)
    s_used = swap_memory_info.used / (1000 * 1000 * 1000)
    s_free = swap_memory_info.free / (1000 * 1000 * 1000)

    s_memory_info = {"total": s_total, "used": s_used, "free": s_free}

    return json.dumps({"virtual_memory_usage": v_memory_info, "swap_memory_usage": s_memory_info})


def get_cpu_usage():
    """Return a float representing the current system-wide CPU
        utilization as a percentage.
    """

    cpu_info = psutil.cpu_percent(interval=None, percpu=True)

    return json.dumps(cpu_info)


def get_disk_usage():
    """Return disk usage statistics about the given *path* as a
        namedtuple including total, used and free space expressed in bytes
        plus the percentage usage.
    """

    disk_info = psutil.disk_usage("/")
    total = disk_info.total / (1000 * 1000 * 1000)
    used = disk_info.used / (1000 * 1000 * 1000)
    free = disk_info.free / (1000 * 1000 * 1000)
    percentage = disk_info.percent

    final_disk_info = {"disk_total": total, "disk_used": used, "disk_free": free, "disk_percentage": percentage}
    return json.dumps(final_disk_info)


def get_network_bandwidth():
    """Return network I/O statistics as a namedtuple including
        the following fields:

         - bytes_sent:   number of bytes sent
         - bytes_recv:   number of bytes received
         - packets_sent: number of packets sent
         - packets_recv: number of packets received
    """

    network_bandwidth_list = []
    network_info = psutil.net_io_counters(pernic=True, nowrap=False)

    for k, v in network_info.items():
        bytes_sent = v.bytes_sent
        bytes_recv = v.bytes_recv
        packets_sent = v.packets_sent
        packetes_recv = v.packets_recv

        value = {"bytes_sent": bytes_sent, "bytes_recv": bytes_recv, "packets_sent": packets_sent, "packets_recv": packetes_recv}
        network_bandwidth_list.append({k: value})

    return json.dumps(network_bandwidth_list)


def get_disk_io():
    """Return system disk I/O statistics as a namedtuple including
        the following fields:

         - read_count:  number of reads
         - write_count: number of writes
         - read_bytes:  number of bytes read
         - write_bytes: number of bytes written
         - read_time:   time spent reading from disk (in ms)
         - write_time:  time spent writing to disk (in ms)
    """

    disk_io_info = psutil.disk_io_counters()
    read_count = disk_io_info.read_count
    write_count = disk_io_info.write_count
    read_bytes = disk_io_info.read_bytes
    write_bytes = disk_io_info.write_bytes
    read_time = disk_io_info.read_time
    write_time = disk_io_info.write_time

    final_disk_io_info = {"read_count": read_count, "write_count": write_count, "read_bytes": read_bytes,
                          "write_bytes": write_bytes, "read_time": read_time, "write_time": write_time}

    return json.dumps(final_disk_io_info)


def get_system_statistics():
    log.info("\nGetting System Statistics\n")
    try:
        header_key = request.headers.get('API-KEY')
        api_status = check_apiKey(header_key)
        if api_status == 'success':
            return system_stats()
        else:
            return api_status
    except Exception as e:
        log.error("Error in list_dir()")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e


def get_system_running_processes():
    processes = []
    for proc in psutil.process_iter(attrs=['cmdline', 'name', 'cpu_percent', 'memory_percent', 'io_counters']):
        processes.append(json.dumps(proc.info))
    return processes


def system_stats():
    memory_usage = get_memory_usage()
    cpu_usage = get_cpu_usage()
    disk_usage = get_disk_usage()
    disk_io = get_disk_io()
    network_bandwidth = get_network_bandwidth()
    processes = get_system_running_processes()
    # log.info('{"memory_usage": %s, "cpu_usage": %s, "disk_usage": %s, "network_bandwidth": %s, "processes": %s}'
    #          % (memory_usage, cpu_usage, disk_usage, network_bandwidth, processes))

    return '{"memory_usage": %s, "cpu_usage": %s, "disk_usage": %s, "disk_io": %s, "network_bandwidth": %s, "processes": %s}' \
           % (memory_usage, cpu_usage, disk_usage, disk_io, network_bandwidth, processes)


def write_system_statistics_history():
    try:
        if not parent_dir.endswith('/'):
            history_dir = parent_dir + '/system_statistics_history/'
        else:
            history_dir = parent_dir + 'system_statistics_history/'

        if not os.path.exists(history_dir):
            os.mkdir(history_dir)
            # make_directory(history_dir, user_pass)

        todays_date = str(date.today())
        todays_history = open("%s.bin" % (history_dir + todays_date), "a+")

        system_statistics_data = system_stats()
        current_unix_time = str(time.time()).split(".")[0]

        data_to_write = bin(int.from_bytes(('{"time": %s, "data": %s}'
                                           % (current_unix_time, system_statistics_data)).encode(), 'big'))
        todays_history.write(data_to_write)
        todays_history.write("\n")
        todays_history.close()

    except Exception as e:
        log.error("Error while saving system statistics")
        log.error(e)


def get_system_statistics_history():
    try:
        header_key = request.headers.get('API-KEY')
        api_status = check_apiKey(header_key)
        if api_status == 'success':
            if not parent_dir.endswith('/'):
                history_dir = parent_dir + '/system_statistics_history/'
            else:
                history_dir = parent_dir + 'system_statistics_history/'

            system_data = []


            loaded_json = json.loads(request.data.decode())
            key = list(loaded_json.keys())[0]

            current_time = datetime.utcfromtimestamp(time.time())

            if key == 'time':
                requested_hour = int(loaded_json["time"])
                requested_time = current_time - timedelta(hours=requested_hour)

            elif key == 'days':
                days = int(loaded_json["days"])
                requested_time = current_time - timedelta(days=days)
            else:
                return 'No such key "%s" found!!!' % key

            while requested_time <= current_time:
                requested_date = requested_time.strftime('%Y-%m-%d')

                if not os.path.exists("%s.bin" % (history_dir + requested_date)):
                    if key == 'time':
                        requested_time = requested_time + timedelta(hours=requested_hour)
                    elif key == 'days':
                        requested_time = requested_time + timedelta(days=1)
                    continue
                with open("%s.bin" % (history_dir + requested_date), "r") as history_file:
                    contents = history_file.read()
                    contents = contents.strip().split("\n")
                    for content in contents:
                        content = int(content, 2)
                        content = content.to_bytes((content.bit_length() + 7) // 8, 'big').decode()
                        content_dict = ast.literal_eval(content)
                        system_data.append(content_dict)
                requested_time = requested_time + timedelta(days=1)

            return '{\'final_data\': %s}' % system_data

        else:
            return api_status
    except Exception as e:
        log.error("Error in list_dir()")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e

