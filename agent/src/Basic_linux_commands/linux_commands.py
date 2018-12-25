import ast
import json
import os
import time

from custom_requests import request

from API_KEYS.keys import check_apiKey
from Basic_linux_commands.archive import create_archive, extract_archive
from Basic_linux_commands.browse_local_folder import browse_local
from Basic_linux_commands.chown_chmod import chown, chmod
from Basic_linux_commands.copy_move_delete import copy, move_rename, delete
from Basic_linux_commands.head_tail import file_read_from_head, file_read_from_tail
from Basic_linux_commands.kill_service import kill_service
from Basic_linux_commands.make_folder import make_directory
from Postgres_connection.connection import get_postgres_connection
from bigdata_logs.logger import getLoggingInstance

log = getLoggingInstance()

username = os.getenv("user")
user_pass = os.getenv("user_pass")
nlines = int(os.getenv("file_read_lines"))


def cmd_home():
    '''
    :return: Urls for Basic Linux Commands
    '''
    path = "Urls for Basic Linux Commands:\n\
        '/ls/': 'to list dir',\n\
        '/mkdir/': 'to make dir',\n\
        '/archive/': 'to archive',\n\
        '/extract/': 'to extract',\n\
        '/kill/': 'to forceful kill',\n\
        '/copy/': 'to copy files',\n\
        '/move/': 'to move files',\n\
        '/remove/': 'to remove files',\n\
        'chown/': 'to change owner',\n\
        '/chmod/': 'to change mode',\n\
        '/head/': 'head 100 lines from top',\n\
        '/tail/': 'tail 100 lines from bottom',\n"

    return path


def list_dir():
    try:
        header_key = request.headers.get('API-KEY')
        api_status = check_apiKey(header_key)
        if api_status == 'success':
            loaded_json = json.loads(request.data.decode())
            path = loaded_json['path']
            if path == 'user':
                path = '/home/%s' % username

            return browse_local(path)
        else:
            return api_status
    except Exception as e:
        log.error("Error in list_dir()")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e


def make_dir():
    try:
        header_key = request.headers.get('API-KEY')
        api_status = check_apiKey(header_key)
        if api_status == 'success':
            loaded_json = json.loads(request.data.decode())
            root_folder = loaded_json['root_folder']
            folder_name = loaded_json['folder_name']

            if not root_folder.endswith('/'):
                root_folder = root_folder + '/'

            folder_to_create = '%s%s' % (root_folder, folder_name)
            return make_directory(folder_to_create, user_pass)
        else:
            return api_status
    except Exception as e:
        log.error("Error in mkdir_dir()")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e


def archive():
    try:
        header_key = request.headers.get('API-KEY')
        api_status = check_apiKey(header_key)
        if api_status == 'success':
            loaded_json = json.loads(request.data.decode())
            root_folder = loaded_json['root_folder']
            zip_folder_name = loaded_json['zip_folder_name']
            file_name_list = loaded_json['file_name']
            override = loaded_json['override']
            file_name_list = ast.literal_eval(file_name_list)

            if not root_folder.endswith('/'):
                root_folder = root_folder + '/'

            return create_archive(zip_folder_name, file_name_list, root_folder, override, user_pass)
        else:
            return api_status
    except Exception as e:
        log.error("Error in archive()")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e


def extract():
    try:
        header_key = request.headers.get('API-KEY')
        api_status = check_apiKey(header_key)
        if api_status == 'success':
            loaded_json = json.loads(request.data.decode())
            root_folder = loaded_json['root_folder']
            file_name = loaded_json['file_name']
            override = loaded_json['override']

            if not root_folder.endswith('/'):
                root_folder = root_folder + '/'

            return extract_archive(file_name, root_folder, override, user_pass)
        else:
            return api_status
    except Exception as e:
        log.error("Error in extract()")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e


def kill():
    try:
        updated_at = int(str(time.time()).split(".")[0])
        header_key = request.headers.get('API-KEY')
        api_status = check_apiKey(header_key)
        if api_status == 'success':
            conn = get_postgres_connection()
            cur = conn.cursor()
            loaded_json = json.loads(request.data.decode())
            service_name = loaded_json['service_name']
            node_id = loaded_json['node_id']
            table_name = loaded_json['table_name']
            kill_result = kill_service(service_name, user_pass)
            kill_result = json.loads(kill_result)
            if kill_result["success"]:
                sql = """UPDATE %s set status='SHUTDOWN', updated_at=%d where id=%d;""" % (table_name, updated_at, int(node_id))
                cur.execute(sql)
                conn.commit()
                cur.close()
                conn.close()
                return '{"success": 1, "msg": ["%s killed forcefully"]}' % service_name
            else:
                sql = """UPDATE %s set status='RUNNING' where id=%d;""" % (table_name, int(node_id))
                cur.execute(sql)
                conn.commit()
                cur.close()
                conn.close()
                return '{"success": 0, "msg": ["Error killing %s forcefully"]}' % service_name
        else:
            return api_status
    except Exception as e:
        log.error("Error in kill()")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e


def copy_files():
    try:
        header_key = request.headers.get('API-KEY')
        api_status = check_apiKey(header_key)
        if api_status == 'success':
            loaded_json = json.loads(request.data.decode())
            src = loaded_json['source']
            file_list = ast.literal_eval(loaded_json['file_list'])
            dest = loaded_json['destination']

            return copy(src, file_list, dest, user_pass)
        else:
            return api_status
    except Exception as e:
        log.error("Error in copy_files()")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e


def move_files():
    try:
        header_key = request.headers.get('API-KEY')
        api_status = check_apiKey(header_key)
        if api_status == 'success':
            loaded_json = json.loads(request.data.decode())
            src = loaded_json['source']
            dest = loaded_json['destination']
            file_list = ast.literal_eval(loaded_json['file_list'])

            return move_rename(src, file_list, dest, user_pass)
        else:
            return api_status
    except Exception as e:
        log.error("Error in move_files()")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e


def remove_files():
    try:
        header_key = request.headers.get('API-KEY')
        api_status = check_apiKey(header_key)
        if api_status == 'success':
            loaded_json = json.loads(request.data.decode())
            src = loaded_json['source']
            files = ast.literal_eval(loaded_json['files'])

            return delete(src, files, user_pass)
        else:
            return api_status
    except Exception as e:
        log.error("Error in remove_files()")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e


def change_owner():
    try:
        header_key = request.headers.get('API-KEY')
        api_status = check_apiKey(header_key)
        if api_status == 'success':
            loaded_json = json.loads(request.data.decode())
            file_path = loaded_json['file_path']
            user = loaded_json['user']
            group = loaded_json['group']

            return chown(file_path, user, group, user_pass)
        else:
            return api_status
    except Exception as e:
        log.error("Error in change_owner()")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e


def change_mode():
    try:
        header_key = request.headers.get('API-KEY')
        api_status = check_apiKey(header_key)
        if api_status == 'success':
            loaded_json = json.loads(request.data.decode())
            file_path = loaded_json['file_path']
            mode = loaded_json['mode']

            return chmod(file_path, mode, user_pass)
        else:
            return api_status
    except Exception as e:
        log.error("Error in change_mode()")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e


def head():
    try:
        header_key = request.headers.get('API-KEY')
        api_status = check_apiKey(header_key)
        if api_status == 'success':
            loaded_json = json.loads(request.data.decode())
            file_path = loaded_json['file_path']

            return file_read_from_head(file_path, nlines, user_pass)
        else:
            return api_status
    except Exception as e:
        log.error("Error in head_view()")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e


def tail():
    try:
        header_key = request.headers.get('API-KEY')
        api_status = check_apiKey(header_key)
        if api_status == 'success':
            loaded_json = json.loads(request.data.decode())
            file_path = loaded_json['file_path']

            return file_read_from_tail(file_path, nlines, user_pass)
        else:
            return api_status
    except Exception as e:
        log.error("Error in tail_view()")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e
