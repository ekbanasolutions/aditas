import json
import os

import run_services
from Basic_linux_commands.chown_chmod import chown
from bigdata_logs.logger import getLoggingInstance

log = getLoggingInstance()

username = os.getenv("user")
groupname = username


def make_directory(folder_to_create, user_pass):
    '''
    Creates a new directory in remote server
    :return: Returns success 1 if successful or success 0 with error message
    '''
    log.info("\nMaking a new Directory\n")
    count = 0
    inner_dict = {}

    mkdir_cmd = "echo %s | sudo -S mkdir -p %s" % (user_pass, folder_to_create)
    result = run_services.run_basic_services(mkdir_cmd)

    if result != "success":
        # count is set to 1 if any one file returns error
        count = 1
        success_value = result.strip().split(":")
        inner_dict[folder_to_create] = success_value[-1].strip()

    if count == 0:
        log.info("\nSuccessfully created a new Directory\n")
        chown(folder_to_create, username, groupname, user_pass)
        return '{"success": 1}'
    else:
        log.error("\nError while creating a new Directory\n")
        return '{"success": 0, "msg": [%s]}' % json.dumps(inner_dict)


