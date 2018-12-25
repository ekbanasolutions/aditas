import json
import os
import shutil
import time

from custom_requests import request

from API_KEYS.keys import check_apiKey
from Configuration import File_Parser
from Configuration.Configuration_Extension import Extension
from bigdata_logs.logger import getLoggingInstance

log = getLoggingInstance()


def config_home():
    '''
    Get configuration for hadoop services, and change it in required config locations
    :return: Returns success 1 if successful or success 0 with error message
    '''
    log.info("\nChanging Configuration\n")
    header_key = request.headers.get('API-KEY')
    api_status = check_apiKey(header_key)
    if api_status == 'success':
        try:
            loaded_json = json.loads(request.data.decode())
            for x in loaded_json:
                filename = x
                final_content = loaded_json[x]

                write_to_file(filename, final_content)

        except Exception as e:
            log.error("\nError while changing configuration\n")
            log.error(e)
            return '{"success": 0, "msg": ["%s"]}' % e

        log.info("\nSuccessfully changed configuration\n")
        return '{"success": 1}'
    else:
        return api_status


hadoop_conf_dir = os.getenv("hadoop_conf_dir")
hbase_conf_dir = os.getenv("hbase_conf_dir")
zookeeper_conf_dir = os.getenv("zookeeper_conf_dir")
spark_conf_dir = os.getenv("spark_conf_dir")
es_conf_dir = os.getenv("es_conf_dir")


def copy_old_configuration(backup_dir, copy_file_path):
    try:
        if copy_file_path.endswith('/'):
            copy_file_path = copy_file_path[:-1]

        shutil.copy(copy_file_path, backup_dir)
    except Exception as e:
        log.error(e)
        return False
    return True


def get_backup_dir_path(conf_dir, copy_in_dir):
    unique_id = str(time.time()).split('.')[0]
    copy_in_unique_dir = copy_in_dir + '_%s' % unique_id

    if not conf_dir.endswith('/'):
        conf_dir = conf_dir + '/'

    backup_dir_path = conf_dir + 'backup/%s/%s' % (copy_in_dir, copy_in_unique_dir)

    if not os.path.exists(backup_dir_path):
        os.makedirs(backup_dir_path)

    return backup_dir_path


def write_to_file(filename, final_content):
    '''
    :param filename: name of a file to be changed
    :param final_content: final json configuration
    :return: Returns success 0 with error message if some exception is caught
    '''
    # Creating an object of Extension class
    extension = Extension()

    hdfs_files_list = getattr(extension, 'hdfs_files_list')
    hbase_files_list = getattr(extension, 'hbase_files_list')
    zookeeper_files_list = getattr(extension, 'zookeeper_files_list')
    spark_files_list = getattr(extension, 'spark_files_list')
    es_files_list = getattr(extension, 'es_files_list')

    try:
        if hdfs_files_list.__contains__(filename):
            backup_dir = get_backup_dir_path(hadoop_conf_dir, filename)
            filename = getattr(extension, '%s' % filename)
            copy_file_path = hadoop_conf_dir + filename
            if os.path.exists(hadoop_conf_dir+filename):
                if copy_old_configuration(backup_dir, copy_file_path):
                    final_configuration = check_extension_get_final_configuration(filename.split(".")[-1], final_content)
                    write_configuration(filename, final_configuration, hadoop_conf_dir)
            else:
                final_configuration = check_extension_get_final_configuration(filename.split(".")[-1], final_content)
                write_configuration(filename, final_configuration, hadoop_conf_dir)

        elif hbase_files_list.__contains__(filename):
            backup_dir = get_backup_dir_path(hbase_conf_dir, filename)
            filename = getattr(extension, '%s' % filename)
            copy_file_path = hbase_conf_dir + filename
            if os.path.exists(hbase_conf_dir + filename):
                if copy_old_configuration(backup_dir, copy_file_path):
                    final_configuration = check_extension_get_final_configuration(filename.split(".")[-1], final_content)
                    write_configuration(filename, final_configuration, hbase_conf_dir)
            else:
                final_configuration = check_extension_get_final_configuration(filename.split(".")[-1], final_content)
                write_configuration(filename, final_configuration, hbase_conf_dir)

        elif zookeeper_files_list.__contains__(filename):
            backup_dir = get_backup_dir_path(zookeeper_conf_dir, filename)
            filename = getattr(extension, '%s' % filename)
            copy_file_path = zookeeper_conf_dir + filename
            if os.path.exists(zookeeper_conf_dir+filename):
                if copy_old_configuration(backup_dir, copy_file_path):
                    final_configuration = check_extension_get_final_configuration(filename.split(".")[-1], final_content)
                    write_configuration(filename, final_configuration, zookeeper_conf_dir)
            else:
                final_configuration = check_extension_get_final_configuration(filename.split(".")[-1], final_content)
                write_configuration(filename, final_configuration, hbase_conf_dir)

        elif spark_files_list.__contains__(filename):
            backup_dir = get_backup_dir_path(spark_conf_dir, filename)
            filename = getattr(extension, '%s' % filename)
            copy_file_path = spark_conf_dir + filename
            if os.path.exists(spark_conf_dir+filename):
                if copy_old_configuration(backup_dir, copy_file_path):
                    final_configuration = check_extension_get_final_configuration(filename.split(".")[-1], final_content)
                    write_configuration(filename, final_configuration, spark_conf_dir)
            else:
                final_configuration = check_extension_get_final_configuration(filename.split(".")[-1], final_content)
                write_configuration(filename, final_configuration, hbase_conf_dir)

        elif es_files_list.__contains__(filename):
            backup_dir = get_backup_dir_path(es_conf_dir, filename)
            filename = getattr(extension, '%s' % filename)
            copy_file_path = es_conf_dir + filename
            if os.path.exists(es_conf_dir+filename):
                if copy_old_configuration(backup_dir, copy_file_path):
                    final_configuration = check_extension_get_final_configuration(filename.split(".")[-1], final_content)
                    write_configuration(filename, final_configuration, es_conf_dir)
            else:
                final_configuration = check_extension_get_final_configuration(filename.split(".")[-1], final_content)
                write_configuration(filename, final_configuration, hbase_conf_dir)

        else:
            log.error("\nfilename %s not found\n" % filename)
            return '{"success": 0, "msg": ["%s filename not found"]}' % filename
    except Exception as e:
        log.error("\nError while writing to file (configuration)\n")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e


def check_extension_get_final_configuration(ext, final_content):
    '''
    :param ext: extension of a file
    :param final_content: final json configuration
    :return: final configuration either in xml, yml, ini etc
    '''
    if ext == 'xml':
        final_configuration = File_Parser.get_xml_configuration(final_content)
    elif ext == 'yml':
        final_configuration = File_Parser.get_yml_configuration(final_content)
    else:
        final_configuration = File_Parser.get_conf_cfg_sh_configuration(final_content)

    return final_configuration


def write_configuration(filename, final_configuration, conf_dir):
    '''
    :param filename: final filename with its extensions
    :param final_configuration: final configuration for the file
    :param conf_dir: configuration directory where file configuration needs to be changed
    :return: Returns success 1 if successful or success 0 with error message
    '''
    try:
        file = open(conf_dir + filename, "w+")
        file.write(final_configuration)
        file.close()
    except Exception as e:
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e

    return '{"success": 1}'

