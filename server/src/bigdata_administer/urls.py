"""bigdata_administer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView

# from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
    url(r'', include('administer.urls')),
    url(r'^elasticsearch/', include('elastic_search.urls')),
    url(r'^hbase/', include('hbase.urls')),
    url(r'^hdfs/', include('hdfs.urls')),
    url(r'^yarn/', include('yarn.urls')),
    url(r'^spark/', include('spark.urls')),
    url(r'^security/', include('security.urls')),
    url(r'^settings/', include('settings.urls')),
    url(r'^browse/', include('browse.urls')),
    url(r'^configuration/', include('configuration.urls')),
    url(r'^nodes/', include('nodes.urls')),


]
