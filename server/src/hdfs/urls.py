from django.conf.urls import url

from hdfs import hdfs_nodes_status
from . import hdfs
# from django.conf.urls import include, url

urlpatterns = [
    url(r'^add/$', hdfs.Add.as_view(), name="add_hdfs"),
    url(r'^remove', hdfs.Remove.as_view(), name="remove_hdfs"),
    url(r'^status/$', hdfs_nodes_status.index, name="hdfs_node_status"),
    url(r'^dn_restart$', hdfs_nodes_status.dn_restart, name='dn_restart'),
    url(r'^dn_stop$', hdfs_nodes_status.dn_stop, name='dn_stop'),
    url(r'^nn_restart$', hdfs_nodes_status.nn_restart, name='nn_restart'),
    url(r'^nn_stop$', hdfs_nodes_status.nn_stop, name='nn_stop'),
    url(r'^restart$', hdfs_nodes_status.h_all_restart, name='h_all_restart'),
    url(r'^stop$', hdfs_nodes_status.h_all_stop, name='h_all_stop'),
    url(r'^command/kill/', hdfs_nodes_status.h_kill, name='h_kill')
]