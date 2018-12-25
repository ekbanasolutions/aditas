from http.client import HTTPException

import requests, json
from django.shortcuts import render, redirect
from administer.models import Nodes
from django.db import connection
from administer import context_processors, helper
from hdfs.models import Hdfs
from django.http import JsonResponse
from django.contrib import messages
from requests.exceptions import ConnectionError

from security.models import Api_key
import hashlib


# Create your views here.

def browse_nodes(request, id):
    if 'user' not in request.session:
        return redirect('login')
    global cluster_id
    obj = helper.helper(request, Hdfs)
    context = context_processors.base_variables_all(request)
    cluster_id = str(request.session[str(request.session['user'])])

    node = Nodes.objects.get(id=id)
    url = "http://%s:%s/command/ls/" % (node.ip, node.port)
    data = {}

    if "browse" in request.GET:
        data["path"] = request.GET["browse"]
    else:
        data["path"] = "user"

    headers = {"API-KEY": obj.get_api_key()}
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        response_jsons = response.json()
        context["path"] = response_jsons["path"]
        print(response_jsons["path"])
        back_dir = back_browse(response_jsons["path"]) + '/'

    except ConnectionError as e:
        messages.error(request, "There is some problem with the connection.Please make sure your internet connection" \
                                " is working and client is up and running on " + node.ip)
        return render(request, "error/500.html", context)

    rows = directory_information(response_jsons)
    context["rows"] = rows
    context["node_ip"] = node.ip
    context["node_name"] = node.name
    context["id"] = id
    context["back_path"] = back_dir

    return render(request, 'browse/browse.html', context)


def back_browse(path):

    directory = path
    directory_list = directory.split('/')
    directory_list.pop(-1)
    directory_list.pop(-1)

    directory_str = "/".join(directory_list)

    if directory_str == '':
        directory = '/'
    else:
        directory = directory_str

    return directory


def directory_information(response_jsons):
    rows = []
    for response_json in response_jsons["folder_details"]:
        owner = response_json["owner"]
        group = response_json["group"]
        name = response_json["name"]
        type = response_json["type"]
        size = response_json["size"]
        permission = response_json["permission"]

        rows.append((permission, owner, group, size, name, type))

    return rows


def browse_directory_ajax(request):
    obj = helper.helper(request, Hdfs)
    node_id = request.GET['node_id']
    node = Nodes.objects.get(id=node_id)
    url = "http://%s:%s/command/ls/" % (node.ip, node.port)

    directory = request.GET['directory_name']

    if directory == "true":
        directory = "/"

    if directory == '':
        directory = 'user'

    data = {}
    data["path"] = directory
    headers = {"API-KEY": obj.get_api_key()}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    data = response.json()

    return JsonResponse(data)


def files_to_hdfs_ajax(request):
    obj = helper.helper(request, Hdfs)

    file_name = request.POST['file_name']
    root_folder = request.POST['root_folder']
    destination_folder = request.POST['destination_folder']
    node_id = request.POST['node_id']
    node = Nodes.objects.get(id=node_id)

    if (root_folder == ''):
        root_folder = '/'
    else:
        root_folder = root_folder + '/'

    if (destination_folder == ''):
        destination_folder = '/'
    to_hdfs = {}
    to_hdfs['file_name'] = file_name
    to_hdfs['root_folder'] = root_folder
    to_hdfs['destination'] = destination_folder

    url = "http://%s:%s/hdfs/write/" % (node.ip,node.port)
    headers = {"API-KEY": obj.get_api_key()}
    response = requests.post(url, data=json.dumps(to_hdfs), headers=headers)
    response_json = response.json()
    if response_json['success'] is 0:
        data = {
            'success': 0,
            'msg': response_json['msg']
        }
    else:
        data = {
            'success': 1,
        }
    return JsonResponse(data)


def back_with_ajax(request):
    obj = helper.helper(request, Hdfs)

    node_id = request.GET['node_id']
    directory = request.GET['directory_name']
    directory_list = directory.split('/')
    directory_list.pop(-1)
    directory_list.pop(-1)

    directory_str = "/".join(directory_list)

    if directory_str == '':
        directory = '/'
    else:
        directory = directory_str
    node = Nodes.objects.get(id=node_id)

    url = "http://%s:%s/command/ls/" % (node.ip,node.port)
    data = {}
    data["path"] = directory
    headers = {"API-KEY": obj.get_api_key()}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    data = response.json()
    data['back_directory'] = data["path"]
    return JsonResponse(data)


def browse_hdfs(request):
    if 'user' not in request.session:
        return redirect('login')
    obj = helper.helper(request, Hdfs)
    master_ip = ""
    client = True
    master = ""
    context = context_processors.base_variables_all(request)
    if obj.atleast_one_client_is_installed():
        if obj.clientIsInstalledOnMaster():
            master = obj.get_active_master()
            if master:
                master_ip = master["ip"]
                master_port = master["web_port"]
                context["client"] = client

            else:
                messages.error(request,
                               "Sorry there is some problem in your configuration file <h3>namenode is down</h3> ")
                context["error_in_conf_file"] = True
                return render(request, 'browse/browse_hdfs.html', context)
        else:
            messages.error(request, "Client is not installed on master node")
            context["client"] = False
            return render(request, 'browse/browse_hdfs.html', context)
    else:
        messages.error(request, "Seems like no client is installed")
        return render(request, 'browse/browse_hdfs.html', context)

    cluster_id = str(request.session[str(request.session['user'])])

    nodes_hdfs = Nodes.objects.all()

    try:
        url = "https://%s:%s/webhdfs/v1/?op=LISTSTATUS" % (master_ip,master_port)
        r = requests.get(url, verify=False)

        response_json = r.json()
        rows = response_json['FileStatuses']['FileStatus']
    except ConnectionError as e:
        messages.error(request, "There is some problem with the connection.Please make sure your internet connection" \
                                " is working and client is up and running on " + master_ip)
        return render(request, "error/500.html", context)

    context["rows"] = rows
    context["nodes_hdfs"] = nodes_hdfs
    context["master_ip"] = master_ip

    return render(request, 'browse/browse_hdfs.html', context)


def browse_hdfs_ajax(request):
    directory = request.GET['directory_name']
    client = True
    context = context_processors.base_variables_all(request)

    if directory == "":
        directory = "/"

    obj = helper.helper(request, Hdfs)
    master = obj.get_active_master()
    if master:
        master_ip = master["ip"]
        master_port = master["web_port"]

        url = "https://%s:%s/webhdfs/v1%s?op=LISTSTATUS" % (master_ip,master_port, directory)

        r = requests.get(url, verify=False)
        response_json = r.json()
        data = response_json['FileStatuses']
        return JsonResponse(data)

    else:
        data = ''
        messages.error(request, "client is not installed on the master node ")
        client = False
        context["client"] = client
        return JsonResponse(data)


def back_with_hdfs_ajax(request):
    directory = request.GET['directory_name']
    context = context_processors.base_variables_all(request)

    directory_list = directory.split('/')
    directory_list.pop(-1)
    directory_str = "/".join(directory_list)

    obj = helper.helper(request, Hdfs)
    master = obj.get_active_master()
    if master:
        master_ip = master["ip"]
        master_port = master["web_port"]

        if directory_str == "":
            url = "https://%s:%s/webhdfs/v1/%s?op=LISTSTATUS" % (master_ip, master_port, directory_str)
        else:
            url = "https://%s:%s/webhdfs/v1%s?op=LISTSTATUS" % (master_ip, master_port, directory_str)

        r = requests.get(url, verify=False)
        response_json = r.json()

        data = response_json['FileStatuses']

        data['back_directory'] = directory_str

        return JsonResponse(data)

    else:
        data = ''

        messages.error(request, "client is not installed on the master node ")
        client = False
        context["client"] = client
        return JsonResponse(data)


def create_dir_hdfs_ajax(request):
    root_folder = request.GET['root_folder']
    folder_name = request.GET['folder_name']

    context = context_processors.base_variables_all(request)
    cluster_id = str(request.session[str(request.session['user'])])

    obj = helper.helper(request, Hdfs)
    master = obj.get_active_master()
    if master:
        master_ip = master["ip"]
        master_port = master["web_port"]

        url = "https://%s:%s/webhdfs/v1%s/%s?op=MKDIRS&permission=711" % (master_ip, master_port, root_folder, folder_name)
        requests.put(url, verify=False)
        response = {
            'success': True
        }
        return JsonResponse(response)
    else:
        messages.error(request, "client is not installed on the master node ")
        client = False
        context["client"] = client
        response = {
            'success': False
        }
        return JsonResponse(response)

def get_node_datas(request):
    if 'user' not in request.session:
        return redirect('login')
    obj = helper.helper(request, Hdfs)

    node_ip = request.POST['node_ip']
    node_port = Nodes.objects.filter(ip=node_ip).values("port").first()["port"]
    url = "http://%s:%s/command/ls/" % (node_ip,node_port)

    data = {}
    data["path"] = "user"
    headers = {"API-KEY": obj.get_api_key()}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    response_jsons = response.json()
    row_external = []
    for response_json in response_jsons['folder_details']:
        owner = response_json["owner"]
        group = response_json["group"]
        name = response_json["name"]
        type = response_json["type"]
        size = response_json["size"]
        permission = response_json["permission"]

        row_external.append(
            {'permission': permission, 'owner': owner, 'group': group, 'size': size, 'name': name, 'type': type})

    data = {
        'row_external': row_external
    }

    return JsonResponse(data)


def browse_eachnode_directory_ajax(request):
    obj = helper.helper(request, Hdfs)
    node_ip = request.POST['node_ip']
    node_port = Nodes.objects.filter(ip=node_ip).values("port").first()["port"]
    directory = request.POST['directory_name']

    if directory == '':
        directory = 'user'

    url = "http://%s:%s/command/ls/" % (node_ip,node_port)
    data = {}
    data["path"] = directory
    headers = {"API-KEY": obj.get_api_key()}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    data = response.json()
    return JsonResponse(data)


def back_eachnode_with_ajax(request):
    obj = helper.helper(request, Hdfs)

    node_ip = request.POST['node_ip']
    node_port = Nodes.objects.filter(ip=node_ip).values("port").first()["port"]
    directory = request.POST['directory_name']
    directory_list = directory.split('/')
    directory_list.pop(-1)
    directory_list.pop(-1)
    directory_str = "/".join(directory_list)

    if directory_str == '':
        directory = '/'
    else:
        directory = directory_str

    url = "http://%s:%s/command/ls/" % (node_ip,node_port)
    data = {}
    data["path"] = directory
    headers = {"API-KEY": obj.get_api_key()}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    data = response.json()
    data['back_directory'] = directory_str
    return JsonResponse(data)


def files_to_local_ajax(request):
    obj = helper.helper(request, Hdfs)

    file_name = request.POST['file_name']
    root_folder = request.POST['root_folder']
    destination_folder = request.POST['destination_folder']
    node_ip = request.POST['node_ip']
    node_port = Nodes.objects.filter(ip=node_ip).values("port").first()["port"]
    nfs = request.POST['nfs']

    if (root_folder == ''):
        root_folder = '/'
    else:
        root_folder = root_folder + '/'

    if (destination_folder == ''):
        destination_folder = '/'
    to_local = {}
    to_local['file_name'] = file_name
    to_local['root_folder'] = root_folder
    to_local['destination'] = destination_folder
    to_local['nfs'] = nfs

    url = "http://%s:%s/hdfs/get/" % (node_ip, node_port)
    headers = {"API-KEY": obj.get_api_key()}
    response = requests.post(url, data=json.dumps(to_local), headers=headers)
    response_json = response.json()

    if response_json['success'] is 0:
        data = {
            'success': 0,
            'msg': response_json['msg']
        }
    else:
        data = {
            'success': 1,
        }
    return JsonResponse(data)


def create_dir_local_ajax(request):
    obj = helper.helper(request, Hdfs)

    root_folder = request.GET['root_folder']
    folder_name = request.GET['folder_name']
    node_ip = request.GET['node_ip']
    node_port = Nodes.objects.filter(ip=node_ip).values("port").first()["port"]
    if root_folder == "":
        root_folder = "user"
    else:
        root_folder = root_folder + '/'
    create_dir = {}

    create_dir["folder_name"] = folder_name
    create_dir["root_folder"] = root_folder

    url = "http://%s:%s/command/mkdir/" % (node_ip,node_port)
    headers = {"API-KEY": obj.get_api_key()}
    response = requests.post(url, data=json.dumps(create_dir), headers=headers)
    response_json = None
    try:
        response_json = json.loads(response.content)
    except TypeError:
        response_json = response.json()
    except Exception as e:
        print(e)
    # response_json = response.json()

    if response_json['success'] is 0:
        result = {
            'success': False,
            'msg': response_json['msg']
        }
    else:
        result = {
            'success': True,
        }

    return JsonResponse(result)


def archive_files_local(request):
    obj = helper.helper(request, Hdfs)

    file_name = request.POST['file_name']
    root_folder = request.POST['root_folder']
    zip_folder_name = request.POST['zip_folder_name']
    override = request.POST['override']
    node_id = request.POST['node_id']

    node = Nodes.objects.get(id=node_id)

    if (root_folder == ''):
        root_folder = 'user'
    else:
        root_folder = root_folder + '/'

    to_archive = {}
    to_archive["file_name"] = file_name
    to_archive["root_folder"] = root_folder
    to_archive["zip_folder_name"] = zip_folder_name
    to_archive["override"] = override

    url = "http://%s:%s/command/archive/" % (node.ip,node.port)

    headers = {"API-KEY": obj.get_api_key()}
    response = requests.post(url, data=json.dumps(to_archive), headers=headers)

    response_json = response.json()
    if response_json['success'] is 0:
        data = {
            'success': 0,
            'msg': response_json['msg']
        }
    else:
        data = {
            'success': 1,
        }
    return JsonResponse(data)


def extract_files_local(request):
    obj = helper.helper(request, Hdfs)

    file_name = request.POST['file_name']
    root_folder = request.POST['root_folder']
    override = request.POST['override']
    node_id = request.POST['node_id']
    node = Nodes.objects.get(id=node_id)

    if (root_folder == ''):
        root_folder = 'user'
    else:
        root_folder = root_folder + '/'

    to_extract = {}
    to_extract["file_name"] = file_name
    to_extract["root_folder"] = root_folder
    to_extract["override"] = override

    url = "http://%s:%s/command/extract/" % (node.ip, node.port)
    headers = {"API-KEY": obj.get_api_key()}
    response = requests.post(url, data=json.dumps(to_extract), headers=headers)
    response_json = response.json()
    if response_json['success'] is 0:
        data = {
            'success': 0,
            'msg': response_json['msg']
        }
    else:
        data = {
            'success': 1,
        }
    return JsonResponse(data)
