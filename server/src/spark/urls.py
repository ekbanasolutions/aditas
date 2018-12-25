from django.conf.urls import url
from . import spark,spark_status
# from django.conf.urls import include, url

urlpatterns = [
    url(r'^add$', spark.Add.as_view(), name="add_spark"),
    url(r'^remove', spark.Remove.as_view(), name="remove_spark"),
    url(r'^status/', spark_status.index, name="add_spark_status"),
    url(r'^sw_restart$', spark_status.sw_restart, name='sw_restart'),
    url(r'^sw_stop$', spark_status.sw_stop, name='sw_stop'),
    url(r'^sm_restart$', spark_status.sm_restart, name='sm_restart'),
    url(r'^sm_stop$', spark_status.sm_stop, name='sm_stop'),
    url(r'^restart$', spark_status.s_all_restart, name='s_all_restart'),
    url(r'^stop', spark_status.s_all_stop, name='s_all_stop'),
]