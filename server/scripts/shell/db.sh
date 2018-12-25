create_db_and_user(){
PGPASSWORD="" psql -U "$superuser" -h "$host" -p "$port" -v db_name="$db_name" -v c_user="$c_user" -v c_pass="$c_pass" \
-f '/etc/aditas/server/scripts/sql/aditas-create_database_and_user.sql'
}

copy_csv_to_default_configuration(){
PGPASSWORD="$c_pass" psql -a -U "$c_user" -h "$host" -p "$port" -d "$db_name"  -v table="configuration_default_configuration" \
--set ON_ERROR_STOP=on -f '/etc/aditas/server/scripts/sql/configuration_default.sql'
}

drop_database_and_tables(){
psql -U postgres -h "$host" -p "$port" -v db_name="$db_name" -v c_user="$c_user" -v c_pass="$c_pass" \
 -f '/etc/aditas/server/scripts/sql/aditas.sql'
}
