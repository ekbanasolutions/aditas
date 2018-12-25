import requests

from django.shortcuts import render
from django.views import View
from administer import context_processors, helper
from administer.helper import helper
from .models import Spark
from administer.models import Service_cluster_reference, Services, Clusters, Nodes
from django.shortcuts import redirect
from django.db import IntegrityError, connection
from django.contrib import messages


# Create your views here.

class Add(View):
    def get(self, request):

        context = context_processors.base_variables_all(request)
        return render(request, 'spark/add.html', context)

    def post(self, request):
        ip = request.POST['ip']
        # type = request.POST['type']
        web_port = request.POST['web_port']
        rpyc_port = request.POST['rpyc_port']
        service_id = Services.objects.get(name="spark").id

        cluster_id = request.session[str(request.session['user'])]
        context = context_processors.base_variables_all(request)

        try:
            if not Spark.objects.filter(ip=ip, cluster=request.session[str(request.session['user'])]).exists():
                Spark.objects.create(ip=ip, type=1, web_port=web_port,cluster_id=cluster_id, rpyc_port=rpyc_port, state=1)

        except IntegrityError as e:
            context['message'] = e
            context['type'] = type
            context['ip'] = ip
            context['web_port'] = web_port
            context['rpyc_port'] = rpyc_port

        if not Service_cluster_reference.objects.filter(service_id=service_id, cluster_id=cluster_id).exists():
            Service_cluster_reference.objects.create(service_id=service_id,
                                                     cluster_id=Clusters.objects.get(id=cluster_id))
            messages.success(request, 'spark successfully added')
            return redirect('index')
        else:
            messages.error(request, "<b>%s</b> as Master for this cluster is already set" % ip)
            return render(request, 'spark/add.html', context)


class Remove(View):
    def get(self, request):
        for_service_cluser = []

        [for_service_cluser.append(a["id"]) for a in Services.objects.filter(name='spark').values("id")]

        Spark.objects.filter(cluster_id=request.session[str(request.session['user'])]).delete()
        Service_cluster_reference.objects.filter(service_id__in=for_service_cluser).delete()

        return redirect("install_service")

