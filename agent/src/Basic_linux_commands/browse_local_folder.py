import json
import os
import subprocess

from bigdata_logs.logger import getLoggingInstance

log = getLoggingInstance()


def browse_local(path):
    '''
    Browse the given folder
    :param path: path to browse
    :return: Returns a json string of files and sub-folder if successful or success 0 with error message
    '''
    log.info("\nBrowsing  %s Directory\n" % path)
    if not path.endswith('/'):
        path = path + '/'
    try:
        details = get_file_details(path)
    except Exception as e:
        log.error("\nError While Browsing %s Directory\n" % path)
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e

    return json.dumps(details)


def cmd_result(cmd):
    '''
    :param cmd: command to be run in a subprocess
    :return: Returns a result of the command sent, if successful or success 0 with error message
    '''
    try:
        result = subprocess.check_output(
            [cmd], stderr=subprocess.STDOUT, shell=True).decode("utf-8")

    except subprocess.CalledProcessError as e:
        log.error("\nError while executing command: %s\n" % cmd)
        log.error(e.stdout)
        return '{"success": 0, "msg": ["%s"]}' % e

    return '%s' % result.strip()


def get_file_details(path):
    '''
    :param path: path to get details of
    :return: Details of folder given, such as name, owner, group, size, permission and type (file or directory)
    '''
    details = {}
    folder_details = []

    ls_command = "ls -lh %s | sed -e '1d'" % path

    result = cmd_result(ls_command)

    if not result == "":
        for rs in result.split('\n'):
            rs = rs.split()
            permission = rs[0]
            owner = rs[2]
            group = rs[3]
            size = rs[4]
            name = rs[8]

            if os.path.isdir(path + name):
                folder_details.append({"name": name, "owner": owner, "group": group, "size": size, "permission": permission,
                                       "type": "directory"})
            else:
                folder_details.append(
                    {"name": name, "owner": owner, "group": group, "size": size, "permission": permission,
                     "type": "file"})

    details["path"] = path
    details["folder_details"] = folder_details

    return details

