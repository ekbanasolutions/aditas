from Hadoop.run_hadoop_services import hadoop_home, dfs_start, dfs_stop, dfs_restart, namenode_start, namenode_stop, namenode_restart, datanode_start, datanode_stop, datanode_restart

path = {
    '/': hadoop_home,
    '/dfs/start/': dfs_start,
    '/dfs/stop/': dfs_stop,
    '/dfs/restart/': dfs_restart,
    '/namenode/start/': namenode_start,
    '/namenode/stop/': namenode_stop,
    '/namenode/restart/': namenode_restart,
    '/datanode/start/': datanode_start,
    '/datanode/stop/': datanode_stop,
    '/datanode/restart/': datanode_restart,
}
