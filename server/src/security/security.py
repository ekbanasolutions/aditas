from django.shortcuts import render, redirect
from django.views import View
from administer.context_processors import base_variables_all
import hashlib, random, string
from datetime import datetime
from django.contrib import messages
# Create your views here.
from security.models import Api_key


class Generate_key(View):
    def get(self, request):
        if 'user' not in request.session:
            return redirect('login')
        context = base_variables_all(request)

        keys = self.get_api_key()
        if keys:
            context["keys"] = keys[0]
        return render(request, 'security/api_key.html', context)

    def post(self, request):
        hash_string = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        sha_signature = hashlib.sha1(hash_string.encode()).hexdigest()
        api_key = self.get_api_key()

        if api_key:
            try:
                api_key.filter(id= api_key[0]['id']).update(key=sha_signature, created_at=datetime.today().replace(microsecond=0))
                request.session['api_key'] = hashlib.md5(sha_signature.encode()).hexdigest()
                messages.success(request, "api key changed successfully")
            except Exception as e:
                print(e)
                messages.error(request, "couldnot update api_key")
        else:
            Api_key.objects.create(key=sha_signature)
            request.session['api_key'] = hashlib.md5(sha_signature.encode()).hexdigest()
            messages.success(request, "api key created successfully")
        return redirect('generate_api_key')

    def get_api_key(self):
        return Api_key.objects.all().values()


