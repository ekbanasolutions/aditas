import ast
import json
import os

from API_KEYS.keys import check_apiKey
from bigdata_logs.logger import getLoggingInstance
from custom_requests import request

log = getLoggingInstance()

hadoop_bin=os.getenv("hadoop_bin_dir")

import run_services


def hdfs_read_write_home():
    '''
    :return: Returns Urls to get from and write to hdfs
    '''
    return '<h3>HDFS Read Write Service Urls</h3>' + \
           'To read from HDFS: <font color="green">/hdfs/get/</font> </br>' + \
           'To write to HDFS: <font color="green">/hdfs/write/</font> </br>'


def hdfs_get():
    '''
    Gets files or directories from hdfs to local
    :return: Returns success 1 if successful or success 0 with error message
    '''
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        root_folder = loaded_json['root_folder']
        destination = loaded_json['destination']
        file_name_list = loaded_json['file_name']
        file_name_list = ast.literal_eval(file_name_list)

        count = 0
        inner_dict = {}
        for file_name in file_name_list:
            file_name = '%s%s' % (root_folder, file_name)
            hdfs_get_cmd = '%shadoop fs -get %s %s' % (hadoop_bin, file_name, destination)

            result = run_services.run_basic_services(hdfs_get_cmd)

            if result != "success":
                # count is set to 1 if any one file returns error
                count = 1
                success_value = result.strip().split(":")
                inner_dict[file_name] = success_value[-1].strip()

        if count == 0:
            log.info("\nSuccessfully Retrived file from HDFS\n")
            return '{"success": 1}'
        else:
            log.error("\nError retriving file from HDFS\n")
            return '{"success": 0, "msg": [%s]}' % json.dumps(inner_dict)
    else:
        return api_status


def hdfs_write():
    '''
    Writes to hdfs from local/remote server
    :return: Returns success 1 if successful or success 0 with error message
    '''
    log.info("\nWriting to HDFS\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        loaded_json = json.loads(request.data.decode())
        root_folder = loaded_json['root_folder']
        destination = loaded_json['destination']
        file_name_list = loaded_json['file_name']
        file_name_list = ast.literal_eval(file_name_list)

        count = 0
        inner_dict = {}
        for file_name in file_name_list:
            file_name = '%s%s' % (root_folder, file_name)
            hdfs_write_cmd = '%shadoop fs -put %s %s' % (hadoop_bin, file_name, destination)
            result = run_services.run_basic_services(hdfs_write_cmd)

            if result != "success":
                # count is set to 1 if any one file returns error
                count = 1
                success_value = result.strip().split(":")
                inner_dict[file_name] = success_value[-1].strip()

        if count == 0:
            log.info("\nSuccessfully written in HDFS\n")
            return '{"success": 1}'
        else:
            log.error("\nError writing files in HDFS\n")
            return '{"success": 0, "msg": [%s]}' % json.dumps(inner_dict)
    else:
        return api_status
