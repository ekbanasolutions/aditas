import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from administer import context_processors
import re
from .models import User, Permission, Role, Role_permission
from .salting_hashing import get_salt, hash_string
from django.contrib import messages


class Groups_index(View):
    @staticmethod
    def get(request):
        context = context_processors.base_variables_all(request)
        groups = Role.objects.all()
        context["groups_data"] = groups

        return render(request, 'account/groups.html', context)


class Add_group(View):
    @staticmethod
    def get(request):
        context = context_processors.base_variables_all(request)

        return render(request, 'account/add_group.html', context)

    def post(self, request):
        context = context_processors.base_variables_all(request)
        group_name = request.POST["groupname"]
        if self.validate_group_name_character(group_name):
            if self.validate_group_name_length(group_name):
                if self.validate_group_name_exists(group_name):
                    try:
                        Role.objects.create(name=group_name)
                        group_id = Role.objects.get(name=group_name).id
                        messages.success(request, "%s successfully added to the group" % group_name)
                        if "addanother" in request.POST:
                            return redirect('add_group')
                        elif "continue" in request.POST:
                            return redirect('change_group', id=group_id)

                    except Exception:
                        messages.error(request, "%s adding to group failed" % group_name)
                        return redirect('add_group')
                else:
                    context["error_msg"] = " %s group name already exists" % group_name
            else:
                context["error_msg"] = " %s group name is < 5" % group_name
        else:
            context["error_msg"] = "group name must be all alphabet character"
        context["group_name"] = group_name
        return render(request, 'account/add_group.html', context)

    @staticmethod
    def validate_group_name_character(group_name):
        if group_name.isalpha():
            return True
        else:
            return False

    @staticmethod
    def validate_group_name_length(group_name):
        if len(group_name) >= 5:
            return True
        else:
            return False

    @staticmethod
    def validate_group_name_exists(group_name):
        group = Role.objects.filter(name=group_name)
        if group:
            return False
        else:
            return True


class Groups_delete(View):
    @staticmethod
    def post(request):
        print("i m inside")
        groups_id = request.POST["groups_id"]
        groups_id_list = list(json.loads(groups_id))
        if not groups_id_list:
            print("empty list")
            messages.error(request, 'select one of the group')
        else:
            group_name = []
            for group_id in groups_id_list:
                group = Role.objects.filter(id=group_id)
                groupname = ""
                if group:
                    groupname = group.values_list("name", flat=True)[0]
                    group_name.append(groupname)
                    group.delete()
                    group_permission = Role_permission.objects.filter(role_id=group_id)
                    if group_permission:
                        group_permission.delete()
            messages.success(request, '%s successfully deleted' % group_name)

        data = {
            'success': True
        }
        return JsonResponse(data)


class Change_group(View):
    @staticmethod
    def get(request, id):
        context = context_processors.base_variables_all(request)
        permissions = Permission.objects.all()
        try:
            context["group"] = Role.objects.get(id=id)
        except Exception as e:
            print(e)

        context["permissions"] = permissions
        group_permission = Role_permission.objects.filter(role_id=id)
        if group_permission:
            context["group_permissions"] = list(group_permission.values_list("permission_id", flat=True))

        return render(request, 'account/change_group.html', context)

    @staticmethod
    def post(request, id):
        permissions_ids = request.POST["permissions_id"]
        permissions_id_lists = list(json.loads(permissions_ids))
        group_name = request.POST["group_name"]
        if group_name != '':
            if Add_group().validate_group_name_character(group_name):
                if Add_group().validate_group_name_length(group_name):
                    group = Role.objects.filter(id=id)
                    if group:
                        group.update(name=group_name)
                    group_permissions = Role_permission.objects.filter(role_id=id)
                    if group_permissions:
                        group_permissions.delete()

                    if permissions_id_lists:
                        for permissions_id in permissions_id_lists:
                            Role_permission.objects.create(role_id=id, permission_id=int(permissions_id))

                    messages.success(request, '%s successfully changed' % group_name)
                    success = True
                else:
                    success = False
                    messages.error(request, "%s group name is < 5" % group_name)
            else:
                success = False
                messages.error(request, "group name must be all alphabet character")
        else:
            success = False
            messages.error(request, "group name must not be empty")
        data = {

            'success': success
        }
        return JsonResponse(data)

