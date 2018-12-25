install_agent(){
PGPASSWORD="$c_pass" psql -a  -U "$c_user" -h "$host" -p "$port" -d "$db_name"  \
 -c "INSERT INTO administer_nodes (ip, fqdn, hostname, approved,name,port) VALUES ('$user_ip', '$fqdn', '$hostname', 0,'$hostname',11605)"
}

uninstall_agent(){
PGPASSWORD="$c_pass" psql -a   -U "$c_user" -h "$host" -p "$port" -d "$db_name" -v user_ip="$user_ip" \
 -f '/etc/aditas/agent/scripts/sql/uninstall_agent.sql'
}
