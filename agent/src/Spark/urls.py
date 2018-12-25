from Spark.run_spark_servers import spark_home, start_spark, stop_spark, restart_spark, start_spark_master, stop_spark_master, spark_master_restart, start_spark_slave, stop_spark_slave, spark_slave_restart

path = {
    '/': spark_home,
    '/start/': start_spark,
    '/stop/': stop_spark,
    '/restart/': restart_spark,
    '/master/start/': start_spark_master,
    '/master/stop/': stop_spark_master,
    '/master/restart/': spark_master_restart,
    '/slave/start/': start_spark_slave,
    '/slave/stop/': stop_spark_slave,
    '/slave/restart/': spark_slave_restart,
}
