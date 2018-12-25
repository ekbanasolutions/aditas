from django.conf.urls import url
from . import configuration

urlpatterns = [
    url(r'^add$', configuration.index_add, name='configuration_add'),
    url(r'^edit$', configuration.index_edit, name='configuration_edit'),
    url(r'^edit/(?P<service>[\w\-]+)$', configuration.edit_configure_service, name='edit_configuration_service'),
    url(r'^show$', configuration.index_show, name='configuration_show'),
    url(r'^user$', configuration.show_configure_service, name='configuration_show_each_node'),
    url(r'^add/(?P<service>[\w\-]+)$', configuration.add_configure_service, name='add_configuration_service'),
    url(r'ajax_configuration$', configuration.add_configure_service_ajax, name='add_submit_configuration'),
    url(r'edit_configure_submit_ajax$', configuration.edit_configure_submit_ajax, name='edit_submit_configuration_ajax'),
    url(r'ajax_configuration_others$', configuration.add_configure_service_other_ajax, name='add_submit_configuration_others'),
    url(r'ajax_configuration_save$', configuration.add_configure_nodes_save, name='add_save_configuration'),
    url(r'^sync$', configuration.sync_configurations, name='sync_configuration'),
    url(r'^revert$', configuration.revert_configuration, name='revert_configuration'),
    url(r'^(?P<node>\d+)/show_backup/(?P<service>[\w\-]+)$', configuration.show_backup_configure_service, name='configuration_backup_show_each_node'),
    url(r'^show_backup$', configuration.index_show_backup, name='configuration_show_backup'),
]