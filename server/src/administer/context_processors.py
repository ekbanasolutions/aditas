from django.shortcuts import redirect

from .models import Clusters, Nodes, Services, Service_cluster_reference
from account.models import User, Role, Role_permission, User_role, Permission
from django.db import connection


def base_variables_all(request):
    if 'user' not in request.session:
        context=None
    else:
        if 'user' in request.session:
            user_id = str(request.session['user'])
            if user_id in request.session:
                cluster = Clusters.objects.get(id=request.session[user_id])
                c_id = cluster.id
                request.session[user_id] = c_id
                nodes = Nodes.objects.filter(approved=1)
            else:
                cluster = Clusters.objects.get(id=1)
                c_id = cluster.id
                request.session[user_id] = c_id
                nodes = Nodes.objects.filter(approved=1)

        clusters = Clusters.objects.all()
        user_own = User.objects.get(id=request.session['user'])

        permission_user = get_permission(user_own.id)

        service_names = Services.objects.values('name')
        services_total = []
        for names in service_names:
            services_total.append(names['name'])

        installed_services = Service_cluster_reference.objects.filter(cluster_id=cluster.id)
        installed_services_names = []

        with connection.cursor() as cursor:
            cursor.execute("select s.name,s.id from administer_services as s join " \
                           "administer_service_cluster_reference as scr on " \
                           "s.id=scr.service_id where scr.cluster_id_id='" + str(c_id) + "'")
            services = cursor.fetchall()

        if installed_services:
            for installed_service in installed_services:
                installed_service_name = Services.objects.get(id=installed_service.service_id)
                installed_services_names.append(installed_service_name.name)

        hdfs_installed = False
        if "hdfs" in installed_services_names:
            hdfs_installed = True

        uninstalled_services = list(set(services_total) - set(installed_services_names))

        context = {"clusters": clusters, "cluster": cluster, "installed_services_names": installed_services_names,
                   "uninstalled_services": uninstalled_services, "nodes_all": nodes, "user_own": user_own,
                   "user_id": int(user_id), "installed_services": installed_services, "services": services,
                   "permission_user": permission_user, "hdfs_installed" : hdfs_installed}

    return context


def get_permission(user_id):
    user_groups = User_role.objects.filter(user_id=user_id).values("role_id")
    permission_user = []

    for user_group in user_groups:
        group_permissions = Role_permission.objects.filter(role_id=user_group['role_id']).values("permission_id")
        for group_permission in group_permissions:
            user_permissions = Permission.objects.filter(id=group_permission["permission_id"]).values("content_type_id")
            for user_permission in user_permissions:
                permission_user.append(user_permission["content_type_id"])

    permission_user = list(set(permission_user))
    return permission_user