import os
import time

import run_services
from Basic_linux_commands.chown_chmod import chown
from bigdata_logs.logger import getLoggingInstance

log = getLoggingInstance()

username = os.getenv("user")
groupname = username


def copy(src, file_list, dest, user_pass, *args):
    log.info("\nCopying\n")

    try:
        file_not_exists = []
        if src.endswith('/'):
            src = src[:-1]
        if dest.endswith('/'):
            dest = dest[:-1]

        if not os.path.exists(dest):
            os.makedirs(dest)

        for file in file_list:
            file_to_copy = src + '/%s' % file

            if not os.path.exists(file_to_copy):
                file_not_exists.append(file_to_copy)
            else:
                if os.path.isdir(file_to_copy):
                    unique_id = str(time.time()).split('.')[0]
                    copied_file = dest + '/%s_%s' % (file, unique_id)
                    run_services.run_basic_services("echo %s | sudo -S cp -r %s %s" % (user_pass, file_to_copy, copied_file))
                    chown(copied_file, username, groupname, user_pass)
                else:
                    unique_id = str(time.time()).split('.')[0]
                    copied_file = dest + '/%s_%s' % (file, unique_id)
                    run_services.run_basic_services("echo %s | sudo -S cp %s %s" % (user_pass, file_to_copy, copied_file))
                    chown(copied_file, username, groupname, user_pass)

        if file_not_exists:
            return '{"success": 0, "msg": ["%s", file does not exists!!!]}' % file_not_exists
        return '{"success": 1}'
    except Exception as e:
        log.error("Exception in copy_move_delete ==> copy()")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e


def move_rename(src, file_list, dest, user_pass):
    try:
        file_not_exists = []
        existing_file_list = []
        if src.endswith('/'):
            src = src[:-1]
        if dest.endswith('/'):
            dest = dest[:-1]

        for file in file_list:
            file_to_move = src+ '/%s' % file
            dest_path = dest + '/%s' % file
            if os.path.exists(dest_path):
                existing_file_list.append(dest_path)
                continue
            if not os.path.exists(file_to_move):
                file_not_exists.append(file_to_move)
            else:
                run_services.run_basic_services("echo %s | sudo -S mv %s %s" % (user_pass, file_to_move, dest))

        if file_not_exists:
            return '{"success": 0, "msg": ["%s", file does not exists!!!]}' % file_not_exists
        elif existing_file_list:
            return '{"success": 0, "msg": ["%s", file already exists!!!]}' % existing_file_list
        return '{"success": 1}'
    except Exception as e:
        log.error("Exception in copy_move_delete ==> move()")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e


def delete(src, files, user_pass):
    try:
        file_not_exists = []
        if src.endswith('/'):
            src = src[:-1]

        for file in files:
            file_path = src + '/%s' % file
            if not os.path.exists(file_path):
                file_not_exists.append(file_path)

            run_services.run_basic_services("echo %s | sudo -S rm -rf %s" % (user_pass, file_path))

        if file_not_exists:
            return '{"success": 0, "msg": ["%s", file does not exists!!!]}' % file_not_exists

        return '{"success": 1}'
    except Exception as e:
        log.error("Exception in copy_move_delete ==> move()")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e



