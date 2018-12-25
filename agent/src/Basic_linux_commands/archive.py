import ast
import os
import zipfile

import run_services
from Basic_linux_commands.chown_chmod import chown
from bigdata_logs.logger import getLoggingInstance

log = getLoggingInstance()

username = os.getenv("user")
groupname = username


def create_archive(zip_folder_name, file_name_list, root_folder, override, user_pass):
    '''
    Creates archive (.zip) of the given folder or files, sent from a post request.
    :return: Returns success 1 if successful or success 0 with error message
    '''
    log.info("\nCreating an archive file\n")

    if '.zip' in zip_folder_name:
        zip_folder_name = zip_folder_name.replace('.zip', '')

    zip_folder_name = zip_folder_name + '.zip'

    if file_name_list:
        try:
            os.chdir(root_folder)
            if os.path.exists(root_folder+zip_folder_name):
                if override == "true":
                    os.remove(root_folder+zip_folder_name)
                else:
                    return '{"success": 0, "msg": "exists"}'

            lst = " ".join(str(x) for x in file_name_list)
            archive_cmd = "echo %s | sudo -S zip %s %s" % (user_pass, zip_folder_name, lst)
            run_services.run_basic_services(archive_cmd)
            chown(zip_folder_name, username, groupname, user_pass)
        except Exception as e:
            log.error("Exception while creating an archive file")
            log.error(e)
            return '{"success": 0, "msg": ["%s"]}' % e

    else:
        log.error("List of files and folders to archive is empty")
        return '{"success": 0, "msg": ["Empty folder list"]}'

    log.info("successfully created an archive file\n")
    return '{"success": 1}'


def extract_archive(file_name, root_folder, override, user_pass):
    '''
    Extracts .zip file
    :return: Returns success 1 if successful or success 0 with error message
    '''
    log.info("\nExtracting archived file\n")
    file_name = ast.literal_eval(file_name)

    if not file_name:
        log.error("File to extract is None")
        return '{"success": 0, "msg": ["Empty File list"]}'

    file_name = file_name[0]

    try:
        if '.zip' not in file_name:
            log.error("%s is not a zip file" % file_name)
            return '{"success": 0, "msg": ["%s not a zip file"]}' % file_name

        if not os.path.exists(root_folder+file_name):
            log.error("%s file does not exists!!!" % file_name)
            return '{"success": 0, "msg": ["%s file does not exists!!!"]}' % file_name

        if os.path.isfile(root_folder+file_name):
            zip_folder_name = file_name.strip().split('.')[0]

            if os.path.exists(root_folder+zip_folder_name):
                if override == "true":
                    zip_file_path = root_folder + zip_folder_name
                    run_services.run_basic_services("echo %s | sudo -S rm -rf %s" % (user_pass, zip_file_path))
                else:
                    log.error("File already exists, set override to true!!!")
                    return '{"success": 0, "msg": "exists"}'

            zip_file_path = root_folder + file_name

            zipf = zipfile.ZipFile(zip_file_path)
            zipf.extractall(root_folder+zip_folder_name)
            zipf.close()
            chown(root_folder+zip_folder_name, username, groupname, user_pass)

        else:
            log.error("%s is not a file" % file_name)
            return '{"success": 0, "msg": ["%s is not a file"]}' % file_name

    except Exception as e:
        log.error("Error while extracting an archived file")
        log.error(e)
        return '{"success": 0, "msg": ["%s"]}' % e

    log.info("Successfully extracted archived file\n")
    return '{"success": 1}'
