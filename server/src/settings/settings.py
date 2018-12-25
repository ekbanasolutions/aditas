from django.shortcuts import render, redirect
from django.views import View
from administer import context_processors
from administer.models import Nodes


class Settings(View):
    def get(self, request):
        if 'user' not in request.session:
            return redirect('login')
        context = context_processors.base_variables_all(request)
        unapproved=Nodes.objects.filter(approved=0).count()
        apprroved = Nodes.objects.filter(approved=1)
        context["unapproved"]=unapproved
        context["approved"]=apprroved
        return render(request,"settings/setting.html",context)

    def post(self, request):
       pass



