from django.conf.urls import url

from elastic_search import elasticsearch_status
from . import elasticsearch
# from django.conf.urls import include, url

urlpatterns = [
    url(r'^add$', elasticsearch.Add.as_view(), name="add_elasticsearch"),
    url(r'^remove', elasticsearch.Remove.as_view(), name="remove_elasticsearch"),
    url(r'^status/', elasticsearch_status.index, name="elasticsearch_status"),
    url(r'^es_restart$', elasticsearch_status.es_restart, name='es_restart'),
    url(r'^es_stop$', elasticsearch_status.es_stop, name='es_stop'),
    url(r'^restart$', elasticsearch_status.es_all_restart, name='es_all_restart'),
    url(r'^stop', elasticsearch_status.es_all_stop, name='es_all_stop'),
]