from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from administer import context_processors
from .models import Yarn
from administer.models import Service_cluster_reference, Services, Clusters
from django.shortcuts import redirect
from django.db import IntegrityError,connection
from django.contrib import messages
# Create your views here.

class Add(View):
    def get(self, request):
        context = context_processors.base_variables_all(request)
        return render(request, 'yarn/add.html', context)

    def post(self, request):
        ip = request.POST['ip']
        # type = request.POST['type']
        web_port = request.POST['web_port']
        rpyc_port = request.POST['rpyc_port']
        service_id = Services.objects.get(name="yarn").id

        context = context_processors.base_variables_all(request)

        cluster_id = request.session[str(request.session['user'])]

        if request.POST['standby_ip']:
            if not Yarn.objects.filter(ip=ip, cluster=request.session[str(request.session['user'])]).exists():
                Yarn.objects.create(ip=request.POST['standby_ip'], type=1, state=0,cluster_id=cluster_id, web_port=web_port, rpyc_port=rpyc_port)
                context['standby_ip'] = request.POST['standby_ip']
        try:
            if not Yarn.objects.filter(ip=ip, cluster=request.session[str(request.session['user'])]).exists():
                Yarn.objects.create(ip=ip, type=1, state=1, web_port=web_port,cluster_id=cluster_id, rpyc_port=rpyc_port)

        except IntegrityError as e:
            context['message'] = e
            context['ip'] = ip
            context['type'] = type
            context['web_port'] = web_port
            context['rpyc_port'] = rpyc_port

        if not Service_cluster_reference.objects.filter(service_id=service_id, cluster_id=cluster_id).exists():

            Service_cluster_reference.objects.create(service_id=service_id,
                                                     cluster_id=Clusters.objects.get(id=cluster_id))
            messages.success(request, 'yarn successfully added')
            return redirect('index')
        else:
            messages.error(request, "<b>%s</b> as Resource manager for this cluster is already set" % ip)
            return render(request, 'yarn/add.html', context)

class Remove(View):
    def get(self, request):
        for_service_cluser = []

        [for_service_cluser.append(a["id"]) for a in Services.objects.filter(name='yarn').values("id")]

        Yarn.objects.filter(cluster_id=request.session[str(request.session['user'])]).delete()
        Service_cluster_reference.objects.filter(service_id__in=for_service_cluser).delete()

        return redirect("install_service")
