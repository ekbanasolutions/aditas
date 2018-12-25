from Yarn.run_yarn_services import yarn_home, yarn_start, yarn_stop, yarn_restart, resourcemanager_start, resourcemanager_stop, resourcemanager_restart, nodemanager_start, nodemanager_stop, nodemanager_restart

path = {
    '/': yarn_home,
    '/start/': yarn_start,
    '/stop/': yarn_stop,
    '/restart/': yarn_restart,
    '/rm/start/': resourcemanager_start,
    '/rm/stop/': resourcemanager_stop,
    '/rm/restart/': resourcemanager_restart,
    '/nm/start/': nodemanager_start,
    '/nm/stop/': nodemanager_stop,
    '/nm/restart/': nodemanager_restart,
}
