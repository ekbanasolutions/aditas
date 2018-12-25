import subprocess

from bigdata_logs.logger import getLoggingInstance

log = getLoggingInstance()


def kill_service(service_name, user_pass):
    '''
    kills a given service forcefully using kill -9
    :return: success if service is killed forcefully
    '''
    log.info("\nForceful kill\n")
    get_pid_cmd = 'echo $(pgrep -f %s)' % service_name

    try:
        result = execute_subcommand(get_pid_cmd)
        process_ids = result.split()
        for pid in process_ids:
            kill_pid_cmd = 'echo %s | sudo -S kill -9 %s' % (user_pass, pid)
            execute_subcommand(kill_pid_cmd)
    except Exception as e:
        return '{"success": 0, "msg": ["%s"]}' % e
        
    return '{"success": 1, "msg": ["%s killed forcefully"]}' % service_name


def execute_subcommand(cmd):
    try:
        result = subprocess.check_output(
            [cmd], stderr=subprocess.STDOUT, shell=True).decode("utf-8")
    except subprocess.CalledProcessError as e:
        return '{"success": 0, "msg": ["%s"]}' % e

    return result
