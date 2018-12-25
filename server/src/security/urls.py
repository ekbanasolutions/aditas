from django.conf.urls import url
from . import security
urlpatterns = [
    url(r'^generate_key/$', security.Generate_key.as_view(), name='generate_api_key')
]