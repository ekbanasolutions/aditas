from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from administer import context_processors
from .models import Elastic_search
from administer.models import Service_cluster_reference, Services, Clusters,Nodes
from django.shortcuts import redirect
from django.db import IntegrityError, connection
from django.contrib import messages
from elastic_search.models import Elastic_search


# Create your views here.

class Add(View):
    def get(self, request):

        context = context_processors.base_variables_all(request)
        return render(request, 'elasticsearch/add.html', context)

    def post(self, request):
        ip = request.POST['ip']
        web_port = request.POST['web_port']
        rpyc_port = request.POST['rpyc_port']
        context = context_processors.base_variables_all(request)
        cluster_id = request.session[str(request.session['user'])]
        service_id = Services.objects.get(name="elasticsearch").id

        if request.POST['standby_ip']:
            if not Elastic_search.objects.filter(ip=ip, cluster=request.session[str(request.session['user'])]).exists():
                Elastic_search.objects.create(ip=request.POST['standby_ip'],cluster_id=cluster_id, type=1,state=0, web_port=web_port, rpyc_port=rpyc_port)
                context['standby_ip'] = request.POST['standby_ip']

        try:
            if not Elastic_search.objects.filter(ip=ip, cluster=request.session[str(request.session['user'])]).exists():
                Elastic_search.objects.create(ip=ip, type=1,cluster_id=cluster_id, web_port=web_port,state=1, rpyc_port=rpyc_port)

        except IntegrityError as e:
            context['message'] = e
            context['ip'] = ip
            context['type'] = type
            context['web_port'] = web_port
            context['rpyc_port'] = rpyc_port

        if not Service_cluster_reference.objects.filter(service_id=service_id,
                                                        cluster_id=cluster_id).exists():

            Service_cluster_reference.objects.create(service_id=service_id,
                                                     cluster_id=Clusters.objects.get(id=cluster_id))
            messages.success(request, 'elasticsearch successfully added')
            return redirect('index')
        else:
            messages.error(request, "<b>%s</b> as Masternode for this cluster is already set" % ip)
            return render(request, 'elasticsearch/add.html', context)

class Remove(View):
    def get(self, request):
        for_service_cluser = []

        [for_service_cluser.append(a["id"]) for a in Services.objects.filter(name='elasticsearch').values("id")]

        Elastic_search.objects.filter(cluster_id=request.session[str(request.session['user'])]).delete()
        Service_cluster_reference.objects.filter(service_id__in=for_service_cluser).delete()

        return redirect("install_service")
