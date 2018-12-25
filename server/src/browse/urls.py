from django.conf.urls import url
from . import browse, browse_others
urlpatterns = [
    url(r'^nodes/(?P<id>\d+)$', browse.browse_nodes, name='browse_nodes'),
    url(r'^nodes/hdfs$', browse.browse_hdfs, name='browse_hdfs'),
    url(r'^nodes/hdfs/get_node_data$', browse.get_node_datas, name='get_node_data'),
    url(r'^nodes/hdfs/directory$', browse.browse_hdfs_ajax, name='browse_hdfs_directory'),
    url(r'^node/directory$', browse.browse_directory_ajax, name='browse_directory_ajax'),
    url(r'^node/local/archive$', browse.archive_files_local, name='archive_files_local'),
    url(r'^node/local/extract$', browse.extract_files_local, name='extract_files_local'),
    url(r'^nodes/hdfs/browse_directory$', browse.browse_eachnode_directory_ajax, name='browse_eachnode_directory_ajax'),
    url(r'^node/directory/tohdfs$', browse.files_to_hdfs_ajax, name='files_to_hdfs_ajax'),
    url(r'^node/directory/back$', browse.back_with_ajax, name='back_with_ajax'),
    url(r'^nodes/hdfs/directory/back$', browse.back_eachnode_with_ajax, name='back_eachnode_with_ajax'),
    url(r'^nodes/hdfs/directory/files_to_local_ajax$', browse.files_to_local_ajax, name='files_to_local_ajax'),
    url(r'^node/directory/back_with_hdfs$', browse.back_with_hdfs_ajax, name='back_with_hdfs_ajax'),
    url(r'^node/directory/create_dir_hdfs_ajax$', browse.create_dir_hdfs_ajax, name='create_dir_hdfs_ajax'),
    url(r'^node/hdfs/directory/create_dir_local_aja$', browse.create_dir_local_ajax, name='create_dir_local_ajax'),
    url(r'^node/copy/$', browse_others.copy_on_nodes, name='copy_on_node'),
    url(r'^node/move/$', browse_others.move_on_nodes, name='move_on_node'),
    url(r'^node/rename/$', browse_others.rename_file, name='rename_file'),
    url(r'^node/delete/$', browse_others.delete_files, name='delete_files'),
    url(r'^node/head/$', browse_others.head_file, name='head_file'),
    url(r'^node/tail/$', browse_others.tail_file, name='tail_file'),

]
