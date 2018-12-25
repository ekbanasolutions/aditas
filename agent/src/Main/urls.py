from route_apps import home, kill_running_service

from Hadoop import urls as hadoop_urls
from Yarn import urls as yarn_urls
from HBase import urls as hbase_urls
from Spark import urls as spark_urls
from Configuration import urls as config_urls
from Hdfs_Read_Write import urls as hdfs_wr_urls
from ElasticSearch import urls as es_urls
from Basic_linux_commands import urls as lx_cmd_urls
from Linux_service_management import urls as system_urls

path = {
    '/': home,
    '/kill/service/': kill_running_service,
    '/hadoop/': hadoop_urls.path,
    '/yarn/': yarn_urls.path,
    '/hbase/': hbase_urls.path,
    '/spark/': spark_urls.path,
    '/config/': config_urls.path,
    '/hdfs/': hdfs_wr_urls.path,
    '/es/': es_urls.path,
    '/command/': lx_cmd_urls.path,
    '/system/': system_urls.path,
}
