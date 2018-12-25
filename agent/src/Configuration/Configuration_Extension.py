
class Extension:
    '''
    Returns filename with corresponding extensions
    '''
    # file lists
    hdfs_files_list = ['hdfs', 'core', 'yarn', 'mapred', 'ssl_client', 'ssl_server']
    hbase_files_list = ['hbase']
    zookeeper_files_list = ['zoo']
    spark_files_list = ['spark_defaults', 'spark_env']
    es_files_list = ['elasticsearch']

    # Extension for HDFS
    hdfs = 'hdfs-site.xml'
    core = 'core-site.xml'
    mapred = 'mapred-site.xml'
    yarn = 'yarn-site.xml'
    ssl_client = 'ssl-client.xml'
    ssl_server = 'ssl-server.xml'

    # Extension for HBase
    hbase = 'hbase-site.xml'

    # Extension for Zookeeper
    zoo = 'zoo.cfg'

    # Extension for spark
    spark_defaults = 'spark-defaults.conf'
    spark_env = 'spark-env.sh'

    # Extension for elasticsearch
    elasticsearch = 'elasticsearch.yml'
