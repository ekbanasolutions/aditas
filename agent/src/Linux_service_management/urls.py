from Linux_service_management.system_statistics import system_home, get_system_statistics, get_system_statistics_history, get_total_space

path = {
    '/': system_home,
    '/statistics/': get_system_statistics,
    '/statistics/history/': get_system_statistics_history,
    '/total/space/': get_total_space,
}
