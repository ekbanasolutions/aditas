from HBase.run_hbase_services import hbase_home, hbase_start, hbase_stop, hbase_restart, hmaster_start, hmaster_stop, hmaster_restart, hregionserver_start, hregionserver_stop, hregionserver_restart

path = {
    '/': hbase_home,
    '/start/': hbase_start,
    '/stop/': hbase_stop,
    '/restart/': hbase_restart,
    '/master/start/': hmaster_start,
    '/master/stop/': hmaster_stop,
    '/master/restart/': hmaster_restart,
    '/regionserver/start/': hregionserver_start,
    '/regionserver/stop/': hregionserver_stop,
    '/regionserver/restart/': hregionserver_restart,
}
