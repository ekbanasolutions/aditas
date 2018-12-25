from django.conf.urls import url

from hbase import hbase_status
from . import hbase
# from django.conf.urls import include, url

urlpatterns = [
    url(r'^add$', hbase.Add.as_view(), name="add_hbase"),
    url(r'^remove', hbase.Remove.as_view(), name="remove_hbase"),
    url(r'^status/', hbase_status.index, name="hbase_status"),
    url(r'^rs_restart$', hbase_status.h_rs_restart, name='h_rs_restart'),
    url(r'^rs_stop$', hbase_status.h_rs_stop, name='h_rs_stop'),
    url(r'^hm_restart$', hbase_status.h_hm_restart, name='h_hm_restart'),
    url(r'^hm_stop$', hbase_status.h_hm_stop, name='h_hm_stop'),
    url(r'^restart$', hbase_status.hb_all_restart, name='hb_all_restart'),
    url(r'^stop', hbase_status.hb_all_stop, name='hb_all_stop'),
    url(r'^command/kill/', hbase_status.h_kill, name='hb_kill')
]