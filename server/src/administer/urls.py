from django.conf.urls import url

from nodes import nodes
from . import administer
# from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', nodes.Nodes_status.as_view(), name="index"),
    url(r'^add_cluster$', administer.AddCluster.as_view(), name="add_cluster"),
    url(r'^delete_cluster$', administer.DeleteCluster.as_view(), name="delete_cluster"),
    url(r'^edit_cluster$', administer.EditCluster.as_view(), name="edit_cluster"),
    url(r'^select_cluster/(?P<id>\d+)$', administer.SelectCluster.as_view(), name="select_cluster"),
    url(r'^install_service/$', administer.InstallServices.as_view(), name="install_service")
]