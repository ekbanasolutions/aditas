import run_services
from bigdata_logs.logger import getLoggingInstance

log = getLoggingInstance()


def chown(file_path, user, group, user_pass):
    try:
        chown_cmd = "echo %s | sudo -S chown %s:%s %s" % (user_pass, user, group, file_path)
        result = run_services.run_basic_services(chown_cmd)
        if result != "success":
            return '{"success": 0, "msg": ["Error while changing the owner", %s]}' % result.strip()
        else:
            return '{"success": 1}'
    except Exception as e:
        log.error("Exception in chown_chmod.py ==> chown()")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e


def chmod(file_path, mode, user_pass):
    try:
        chmod_cmd = "echo %s | sudo -S chmod %d %s" %(user_pass, int(mode), file_path)
        result = run_services.run_basic_services(chmod_cmd)
        if result != "success":
            return '{"success": 0, "msg": ["Error while changing the owner", %s]}' % result.strip()
        else:
            return '{"success": 1}'
    except Exception as e:
        log.error("Exception in chown_chmod.py ==> chmod()")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e
