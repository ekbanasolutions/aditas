from django.conf.urls import url

from yarn import yarn_status
from . import yarn
# from django.conf.urls import include, url

urlpatterns = [
    url(r'^add$', yarn.Add.as_view(), name="add_yarn"),
    url(r'^remove', yarn.Remove.as_view(), name="remove_yarn"),
    url(r'^status/', yarn_status.index, name="add_yarn_status"),
    url(r'^nm_restart$', yarn_status.y_nm_restart, name='y_nm_restart'),
    url(r'^nm_stop$', yarn_status.y_nm_stop, name='y_nm_stop'),
    url(r'^rm_restart$', yarn_status.y_rm_restart, name='y_rm_restart'),
    url(r'^rm_stop$', yarn_status.y_rm_stop, name='y_rm_stop'),
    url(r'^restart$', yarn_status.y_all_restart, name='y_all_restart'),
    url(r'^stop', yarn_status.y_all_stop, name='y_all_stop'),
    url(r'^command/kill/', yarn_status.y_kill, name='y_kill')
]