from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from . import context_processors
from .models import Clusters, Nodes
from django.db import IntegrityError


# Create your views here.

class IndexView(View):
    def get(self, request):
        context = context_processors.base_variables_all(request)

        return render(request, 'base.html', context)
        # return redirect("list_nodes")


class AddCluster(View):
    def get(self, request):
        context = context_processors.base_variables_all(request)
        return render(request, 'add_cluster.html', context)

    def post(self, request):
        if request.POST['cluster'] is not '':
            cluster = request.POST['cluster']
        else:
            data = {'success': 0,
                    'msg': "We are unable to get name of the cluster.Please refresh page and try again"}
            return JsonResponse(data)
        try:
            Clusters.objects.create(name=cluster)
            messages.success(request, "cluster " + cluster + " was added successfully")
            data = {"success": 1}
        except IntegrityError as e:
            data = {"success": 0, "msg": "cluster <b>" + cluster + "</b> already exists"}

        return JsonResponse(data)


class DeleteCluster(View):
    def post(self, request):

        if request.POST['cluster'] is not '':
            cluster = request.POST['cluster']
            print(cluster)
            if cluster == '1':
                data = {'success': 0,
                        'msg': "This cluster is protected"}
                return JsonResponse(data)
            if cluster == str(request.session[str(request.session['user'])]):
                data = {'success': 0,
                        'msg': "Currently seelcted cluster cannot be deleted"}
                return JsonResponse(data)
        else:
            data = {'success': 0,
                    'msg': "We are unable to get name of the cluster.Please refresh page and try again"}
            return JsonResponse(data)

        try:
            Clusters.objects.filter(id=cluster).delete()
            data = {'success': 1}
            messages.success(request, "cluster was deleted successfully")

        except Exception as e:
            data = {'success': 0,
                    'msg': "Sorry there was some problem deleting this cluster.Please make sure no nodes are associated with this cluster"}

        return JsonResponse(data)


class EditCluster(View):

    def post(self, request):

        if request.POST['cluster'] is not '':
            cluster = request.POST['cluster']
        else:
            data = {'success': 0,
                    'msg': "We are unable to get name of the cluster.Please refresh page and try again"}
            return JsonResponse(data)

        if request.POST['cluster_id'] is not '':
            id = request.POST['cluster_id']
        else:
            data = {'success': 0,
                    'msg': "We are unable to get id of the cluster.Please refresh page and try again"}
            return JsonResponse(data)
        try:
            if Clusters.objects.filter(name=cluster).exists():
                data = {'success': 0,
                        "msg": "cluster <b>" + cluster + "</b> already exists"}
            else:
                Clusters.objects.filter(id=id).update(name=cluster)
                data = {'success': 1}
                messages.success(request, "cluster was updated successfully")

        except Exception as e:
            print(e.args)
            data = {"success": 0, "msg": "Sorry there was some problem updating the value"}

        return JsonResponse(data)


class SelectCluster(View):
    def get(self, request, id):
        request.session[str(request.session['user'])] = id
        print(request.session[str(request.session['user'])])

        return redirect('index')


class ManageNodes(View):
    def get(self, request):
        nodes = Nodes.objects.filter(node_cluster=str(request.session[str(request.session['user'])])).all()
        context = context_processors.base_variables_all(request)
        context["nodes"] = nodes
        return render(request, 'nodes/approved_index.html', context)


class InstallServices(View):
    def get(self, request):
        context = context_processors.base_variables_all(request)
        return render(request, 'services/install.html', context)
