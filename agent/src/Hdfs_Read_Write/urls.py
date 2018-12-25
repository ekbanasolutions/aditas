from Hdfs_Read_Write.hdfs_read_write_service import hdfs_read_write_home, hdfs_get, hdfs_write

path = {
    '/': hdfs_read_write_home,
    '/get/': hdfs_get,
    '/write/': hdfs_write,
}
