from ElasticSearch.run_es_services import es_home, elasticsearch_start, elasticsearch_stop, elasticsearch_restart

path = {
    '/': es_home,
    '/start/': elasticsearch_start,
    '/stop/': elasticsearch_stop,
    '/restart/': elasticsearch_restart,
}
