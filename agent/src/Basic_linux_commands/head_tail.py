import json
import subprocess

from bigdata_logs.logger import getLoggingInstance

log = getLoggingInstance()


def head_tail_service(cmd):
    '''
    :param cmd: command to execute
    :param err_msg: message if error is occured
    :return: result of the command after execution
    '''
    try:
        result = subprocess.check_output(
            cmd, stderr=subprocess.STDOUT, shell=True,
            universal_newlines=True)
    except subprocess.CalledProcessError as exc:
        log.error("\nError while executing command: %s\n" % cmd)
        log.error(exc.stdout)
        error_restult = exc.output
        return '{"success": 0, "msg": "%s"}' % error_restult

    return result


def file_read_from_head(file_path, nlines, user_pass):
    if file_path.endswith('/'):
        file_path = file_path[:-1]

    result = head_tail_service("echo %s | sudo -S head -n %d %s" % (user_pass, nlines, file_path))
    final_result = '{"success": 1, "head_result": %s}' % json.dumps(result)
    return final_result


def file_read_from_tail(file_path, nlines, user_pass):
    result = head_tail_service("echo %s | sudo -S tail -%d %s" % (user_pass, nlines, file_path))
    final_result = '{"success": 1, "tail_result": %s}' % json.dumps(result)
    return final_result


