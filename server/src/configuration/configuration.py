import json, requests, datetime, ast
from .profiler_test import profile
from administer import context_processors,helper
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render
from administer.models import Services, Nodes,Service_cluster_reference
from administer.helper import helper
from .models import User_preferred_configuration, Backup_configuration, Restart_after_configuration, sync_configuration,Default_configuration
from django.http import JsonResponse

# Create your views here.

def index_add(request):
    context = context_processors.base_variables_all(request)
    context["action"]="add"
    return render(request, 'configuraion/configuration.html', context)

def index_edit(request):
    context = context_processors.base_variables_all(request)
    context["action"] = "edit"
    return render(request, 'configuraion/configuration.html',context)

def index_show(request):
    context = context_processors.base_variables_all(request)
    node = Nodes.objects.all()
    context["node"] = node
    context["action"] = "show"
    return render(request, 'configuraion/configuration_copy.html', context)

def index_show_backup(request, id):
    context = context_processors.base_variables_all(request)
    node = Nodes.objects.all()
    context["node"] = node
    context["action"] = "backup"
    return render(request, 'configuraion/configuration.html', context)



def add_configure_service(request, service):
    service_object = Services.objects.get(name=service)
    key_configurations_users = User_preferred_configuration.objects.filter(service_id=service_object.id)
    key_configurations = Default_configuration.objects.exclude(name__in=[x.key_name for x in key_configurations_users]).filter(service_id=service_object.id)
    nodes_configuration = helper(request).get_all_nodes()

    context = context_processors.base_variables_all(request)

    context["key_configurations"] = key_configurations
    context["id"] = service_object.id
    context["service_name"] = service
    context["nodes_configuration"] = nodes_configuration

    return render(request, 'configuraion/configure_service.html', context)


def add_configure_service_ajax(request):
    if request.is_ajax and request.method == "POST":
        key_name = request.POST['key_name']
        key_value = request.POST['key_value']
        key_type = request.POST['key_type']
        nodes_submit = request.POST.getlist('nodes')
        service_id = request.POST['service_id']
        nodes_submit = ast.literal_eval(nodes_submit[0])
        if nodes_submit == '[]':
            delete_user_preffered = User_preferred_configuration.objects.filter(key_name=key_name)
            delete_user_preffered.delete()
            data = {'success': True}

            return JsonResponse(data)

        else:

            configure_row_user = User_preferred_configuration.objects.filter(key_name=key_name,
                                                                             service_id=service_id,
                                                                             key_type=key_type).exists()

            if configure_row_user:
                row_user1 = User_preferred_configuration.objects.filter(key_name=key_name, service_id=service_id,
                                                                        key_type=key_type)
                value_dict = {}
                for node in nodes_submit:
                    value_dict[str(node)] = key_value

                row_user1.update(value=value_dict)

                data = {'success': True}
                return JsonResponse(data)

            else:
                value_dict = {}
                for node in nodes_submit:
                    value_dict[str(node)] = key_value

                create_conf_user = User_preferred_configuration(service_id=service_id, key_name=key_name,
                                                                value=value_dict, key_type=key_type)
                create_conf_user.save()

                data = {'success': True}


                return JsonResponse(data)

def edit_configure_submit_ajax(request):
    if request.is_ajax and request.method == "POST":
        key_name = request.POST['key_name']
        key_value = request.POST['key_value']
        key_type = request.POST['key_type']
        service_id = request.POST['service_id']

        configure_row_user = User_preferred_configuration.objects.filter(key_name=key_name,
                                                                         service_id=service_id,
                                                                         key_type=key_type).exists()

        if configure_row_user:
            row_user1 = User_preferred_configuration.objects.filter(key_name=key_name, service_id=service_id,
                                                                    key_type=key_type)

            row_user1.update(value=key_value)
            data = {'success': True}

            return JsonResponse(data)

        else:
            create_conf_user = User_preferred_configuration(service_id=service_id, key_name=key_name,
                                                            value=key_value, key_type=key_type)
            create_conf_user.save()
            data = {'success': True}

            return JsonResponse(data)

def add_configure_nodes_save(request):
    nodes = helper(request).get_all_nodes()
    service_id = request.POST['service_id']

    for node in nodes:
        configuration = {}

        row_user_types = User_preferred_configuration.objects.order_by().values('key_type').distinct() \
            .filter(value__contains=node, service_id=service_id)

        for row_user_type in row_user_types:
            configuration_inside = {}
            row_users = User_preferred_configuration.objects.filter(key_type=row_user_type['key_type'], value__contains=node)
            for row_user in row_users:
                value = ast.literal_eval(row_user.value)
                configuration_inside[row_user.key_name] = value[str(node)]

            configuration[row_user_type['key_type']] = configuration_inside

        url = "http://%s:11605/config/" % node

        response = requests.post(url, data=json.dumps(configuration), headers={"API-KEY": helper.get_api_key()})
        response_dict = json.loads(response.content.decode())
        if response_dict["success"] == 0:
            data = {
                'success': False
            }
            return JsonResponse(data)

    data = {
        'success': True
    }

    restart_service_check = Restart_after_configuration.objects.filter(service_id=service_id).exists()
    if restart_service_check:
        restart_service = Restart_after_configuration.objects.get(service_id=service_id)
        restart_service.status = 1
        restart_service.save()
    else:
        restart_service = Restart_after_configuration(service_id=service_id, status=1)
        restart_service.save()

    return JsonResponse(data)

def edit_configure_service(request, service):
    context = context_processors.base_variables_all(request)
    service_object = Services.objects.get(name=service)


    nodes_configuration = helper(request).get_all_nodes()

    key_configurations = User_preferred_configuration.objects.filter(service_id=service_object.id)

    context["key_configurations"]=key_configurations
    context["id"]=service_object.id
    context["service_name"]=service
    context["nodes_configuration"]=nodes_configuration

    return render(request, 'configuraion/edit_configuration.html', context)


def show_configure_service(request):
    context = context_processors.base_variables_all(request)
    node = request.GET["node"]
    service = request.GET["service_id"]
    key_configurations = User_preferred_configuration.objects.filter(service_id=service, value__contains=node)
    if key_configurations:
        key_configuration_list = []
        for key_configuration in key_configurations:
            key_configuration_dict = {}
            key_configuration_dict["key"] = key_configuration.key_name
            key_configuration_dict["type"] = key_configuration.key_type
            value = ast.literal_eval(key_configuration.value)
            key_configuration_dict["value"] = value[str(node)]

            key_configuration_list.append(key_configuration_dict)

        context["key_configurations"] = key_configuration_list

    backup_key_configurations = Backup_configuration.objects.filter(service_id=service, value__contains=node)
    if backup_key_configurations:
        backup_key_configurations_list = []
        for key_configuration in backup_key_configurations:
            backup_key_configurations_dict = {}
            backup_key_configurations_dict["key"] = key_configuration.key_name
            backup_key_configurations_dict["type"] = key_configuration.key_type
            value = ast.literal_eval(key_configuration.value)
            backup_key_configurations_dict["value"] = value[str(node)]

            backup_key_configurations_list.append(backup_key_configurations_dict)

        context["backup_key_configurations"] = backup_key_configurations_list

    context["node_ip"] = node
    context["service_name"] = service
    return render(request, 'configuraion/show_configuration.html', context)

def sync_configurations(request):
    try:
        data = ""
        user_configurations = User_preferred_configuration.objects.all()
        backup_configurations = Backup_configuration.objects.all()

        if backup_configurations:
            backup_configurations.delete()

        if user_configurations:
            try:
                for user_configuration in user_configurations:
                    user_configuration_dict = user_configuration.__dict__
                    user_configuration_dict.pop('id')
                    user_configuration_dict.pop('_state')
                    Backup_configuration.objects.create(**user_configuration_dict)

                    user_name_sync = request.user.username
                    last_sync = datetime.datetime.now()

                    sync_configuration.objects.create(sync_by=user_name_sync, last_sync=last_sync)

                    data = {
                        'success': True
                    }

            except Exception as e:
                data = {
                    'success': False,
                    'msg': '%s' % e
                }
            return JsonResponse(data)
        else:
            data = {
                'success': False,
                'msg': 'user configuration table is empty'
            }

    except Exception as e:
        data = {
            'success': False,
            'msg': '%s' % e
        }


    return JsonResponse(data)


def revert_configuration(request):
    try:
        user_configurations = User_preferred_configuration.objects.all()
        backup_configurations = Backup_configuration.objects.all()

        if user_configurations:
            user_configurations.delete()

        if backup_configurations:

            for backup_configuration in backup_configurations:
                backup_configuration_dict = backup_configuration.__dict__
                backup_configuration_dict.pop('id')
                backup_configuration_dict.pop('_state')
                User_preferred_configuration.objects.create(**backup_configuration_dict)

                data = {
                    'success': True
                }
        else:
            data = {
                'success': False,
                'msg': "backup table is empty...revert aborted"
            }
    except Exception as e:
        data = {
            'success': False,
            'msg': '%s' % e
        }


    return JsonResponse(data)

def add_configure_service_other_ajax(request):
    other_configurations = request.POST['other_configurations']
    service_id = request.POST['service_id']

    other_configurations = json.loads(other_configurations)
    list_data = []
    for other_configuration in other_configurations:
        try:
            for other_configuration_type in other_configuration['type']:
                value_dict = {}
                for node in other_configuration['node']:
                    value_dict[str(node)] = other_configuration['value']

                User_preferred_configuration.objects.create(service_id=service_id, key_name=other_configuration['key'],
                                                            value=value_dict, key_type=other_configuration_type)

                data = {
                    'success': True,
                }
                list_data.append(data)
        except IntegrityError as e:

            data = {
                'success': False,
                'msg': 'key_name duplicate *%s' % other_configuration['key'],

            }
            list_data.append(data)



    list_data1 = {'list_data': list_data}

    return JsonResponse(list_data1)

def settings(request):
    return render(request, 'settings/setting.html')

def show_backup_configurations(request):
    key_configurations = Backup_configuration.objects.all()
    return render(request, 'configuraion/backup_configuration.html', {"key_configurations": key_configurations})

def show_backup_configure_service(request, node, service):
    context = context_processors.base_variables_all(request)

    service_id = Services.objects.get(name=service).id

    node_ip = Nodes.objects.get(id=node).ip

    key_configurations = Backup_configuration.objects.filter(service_id=service_id, value__contains=node_ip)

    context["key_configurations"] = key_configurations
    context["node_ip"] = node_ip
    context["service_name"] = service

    return render(request, 'configuraion/backup_configuration.html', context)

