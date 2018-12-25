env=$(cat <<EOF
hadoop_home=
hbase_home=
spark_home=
es_home=

hadoop_conf_dir=${hadoop_home}etc/hadoop/
hbase_conf_dir=${hbase_home}conf/
spark_conf_dir=${spark_home}conf/
es_conf_dir=

hadoop_bin_dir=${hadoop_home}bin/
hadoop_sbin_dir=${hadoop_home}sbin/
hbase_bin_dir=${hbase_home}bin/
spark_sbin_dir=${spark_home}sbin/
es_bin_dir=${es_home}bin/

parent_dir=${ADITAS_HOME}/
user=${USER}
user_pass=${sudo_pass}

file_read_lines=100

log_dir=${ADITAS_HOME}/logs/
log_filename=error.log

postgres_db=$db_name
postgres_user=$c_user
postgres_password=$c_pass
postgres_host=$host
postgres_port=$port
EOF
)

mkdir -p "/etc/aditas/agent/conf"
echo "$env">"/etc/aditas/agent/conf/agent.env"

