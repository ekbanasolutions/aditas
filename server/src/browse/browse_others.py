import sys

import requests, json
from django.shortcuts import render, redirect
from administer.models import Nodes
from django.db import connection
from administer import context_processors, helper
from django.http import JsonResponse

from django.contrib import messages
from requests.exceptions import ConnectionError

def copy_on_nodes(request):
    if 'user' not in request.session:
        return redirect('login')
    obj = helper.helper(request)

    source = request.POST['source']
    if source == "":
        source = "/"

    destination = request.POST['destination']
    if destination == "":
        destination = "/"

    files = request.POST['files']
    node_id = request.POST['node_id']
    node = Nodes.objects.get(id=node_id)

    url = "http://%s:%s/command/copy/" % (node.ip, node.port)
    data_copy = {}
    data_copy['source'] = source
    data_copy['file_list'] = files
    data_copy['destination'] = destination

    headers = {"API-KEY": obj.get_api_key()}
    response = requests.post(url, data=json.dumps(data_copy), headers=headers)
    response_json = None
    try:
        response_json = json.loads(response.content)
    except TypeError:
        response_json = response.json()
    except Exception as e:
        print(e)
    # response_json = response.json()

    if response_json['success'] == 0:
        # print(response_json['msg'])
        data = {
            'success': 0,
            'msg': response_json['msg']
        }
    else:
        data = {
            'success': 1,
        }
    return JsonResponse(data)

def move_on_nodes(request):
    obj = helper.helper(request)

    source = request.POST['source']
    if source == "":
        source = "/"

    destination = request.POST['destination']
    if destination == "":
        destination = "/"

    files = request.POST['files']
    node_id = request.POST['node_id']
    node = Nodes.objects.get(id=node_id)

    url = "http://%s:%s/command/move/" % (node.ip, node.port)
    data_copy = {}
    data_copy['source'] = source
    data_copy['file_list'] = files
    data_copy['destination'] = destination

    headers = {"API-KEY": obj.get_api_key()}
    response = requests.post(url, data=json.dumps(data_copy), headers=headers)
    response_json = None
    try:
        response_json = json.loads(response.content)
    except TypeError:
        response_json = response.json()
    except Exception as e:
        print(e)
    # response_json = response.json()
    if response_json['success'] == 0:
        data = {
            'success': 0,
            'msg': response_json['msg']
        }
    else:
        data = {
            'success': 1,
        }
    return JsonResponse(data)

def rename_file(request):
    obj = helper.helper(request)

    source = request.POST['source']
    if source == "":
        source = "/"

    files = request.POST['files']
    new_name = request.POST['new_name']
    node_id = request.POST['node_id']
    node = Nodes.objects.get(id=node_id)

    url = "http://%s:%s/command/move/" % (node.ip, node.port)
    data_copy = {}
    data_copy['source'] = source
    data_copy['file_list'] = files
    data_copy['destination'] = source + "/" + new_name

    headers = {"API-KEY": obj.get_api_key()}

    response = requests.post(url, data=json.dumps(data_copy), headers=headers)
    response_json = None
    try:
        response_json = json.loads(response.content)
    except TypeError:
        response_json = response.json()
    except Exception as e:
        print(e)
    # response_json = response.json()

    if response_json['success'] is 0:
        # print(response_json['msg'])
        data = {
            'success': 0,
            'msg': response_json['msg']
        }
    else:
        data = {
            'success': 1,
        }
    return JsonResponse(data)


def delete_files(request):
    obj = helper.helper(request)

    source = request.POST['source']
    if source == "":
        source = "/"

    files = request.POST['files']
    node_id = request.POST['node_id']
    node = Nodes.objects.get(id=node_id)

    data_copy = {}
    data_copy['source'] = source
    data_copy['files'] = files

    url = "http://%s:%s/command/remove/" % (node.ip, node.port)
    print(url)
    print(json.dumps(data_copy))

    headers = {"API-KEY": obj.get_api_key()}
    response = requests.post(url, data=json.dumps(data_copy), headers=headers)
    response_json = None
    try:
        response_json = json.loads(response.content)
    except TypeError:
        response_json = response.json()
    except Exception as e:
        print(e)
    # response_json = response.json()
    if response_json['success'] == 0:
        data = {
            'success': 0,
            'msg': response_json['msg']
        }
    else:
        data = {
            'success': 1,

        }
    return JsonResponse(data)

def head_file(request):
    obj = helper.helper(request)
    file_name = request.POST['file_name']
    source = request.POST['source'] + "/" + file_name
    node_id = request.POST['node_id']
    node = Nodes.objects.get(id=node_id)
    data_copy = {}
    data_copy['file_path'] = source
    # sys.exit(0)
    url = "http://%s:%s/command/head/" % (node.ip, node.port)

    headers = {"API-KEY": obj.get_api_key()}
    response = requests.post(url, data=json.dumps(data_copy), headers=headers)
    response_json = None
    try:
        response_json = json.loads(response.content)
    except TypeError:
        response_json = response.json()
    except Exception as e:
        print(e)

    # response_json = json.loads(response.content)

    # head_result1 = head_result.replace('\t', ' ')
    # print(type(head_result))

    if response_json['success'] is 0:
        data = {
            'success': 0,
            'msg': response_json['msg']
        }
    else:
        result = response_json['head_result'].replace('\t', ' ').split('\n')
        data = {
            'success': 1,
            'result': result
        }
    return JsonResponse(data)


def tail_file(request):
    obj = helper.helper(request)
    file_name = request.POST['file_name']
    source = request.POST['source'] + "/" + file_name
    node_id = request.POST['node_id']
    node = Nodes.objects.get(id=node_id)
    data_copy = {}
    data_copy['file_path'] = source
    url = "http://%s:%s/command/tail/" % (node.ip, node.port)

    headers = {"API-KEY": obj.get_api_key()}
    response = requests.post(url, data=json.dumps(data_copy), headers=headers)

    response_json = None
    try:
        response_json = json.loads(response.content)
    except TypeError:
        response_json = response.json()
    except Exception as e:
        print(e)

    # response_json = json.loads(response.content)

    if response_json['success'] is 0:
        data = {
            'success': 0,
            'msg': response_json['msg']
        }
    else:
        result = response_json['tail_result'].replace('\t', ' ').split('\n')
        data = {
            'success': 1,
            'result': result
        }
    return JsonResponse(data)