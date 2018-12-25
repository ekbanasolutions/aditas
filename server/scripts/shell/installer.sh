var_sanity_check=""

sanity_check() {
if [[ "$(which python3)" ]]; then
python="$(which python3)"
else
echo "Error : python version $(python -V 2>/dev/null) detected.Please install python 3.5 or above"
python="$(which python2)"
fi

if [[ "$(which pip3)" ]]; then
pip="$(which pip3)"
else
pip="$(which pip)"
fi

psql=$(command -v psql)
if [ ! $psql ]; then
echo "postgres database is required to run this application"
var_sanity_check="fail"
fi
}

check_and_set_variables()
{
if [ -z "$db_name" ]; then
export db_name="${db_name}"
fi

if [ -z "$c_user" ]; then
export c_user="${c_user}"
fi

if [ -z "$c_pass" ]; then
export c_pass="${c_pass}"
fi

if [ -z "$host" ]; then
echo "ERROR: no host provided.Please run 'dpkg-reconfigure' to configure host ip for database"
exit 1
fi

if [ -z "$port" ]; then
echo "ERROR: no port provided.Please run 'dpkg-reconfigure' to configure port for database"
exit 1
fi

if [ -z "$superuser" ]; then
echo "ERROR: no superuser provided.Please run 'dpkg-reconfigure' to configure superuser for database"
exit 1
fi

if [ -z "$db_pass" ]; then
echo "ERROR: no pass provided.Please run 'dpkg-reconfigure' to configure password for database"
exit 1
fi
}

remove_db_leftovers(){
check_and_set_variables
if [[ -f "${SQL_SCRIPT}" ]]; then
. "${SQL_SCRIPT}"
fi
drop_database_and_tables
}

setup_venv(){
if [[ ! -d "${ADITAS_VENV_PATH}" ]]; then
echo "virtual env ${virtualenv}"
"${virtualenv}" "${ADITAS_VENV_PATH}" -p "${python}"
fi
}

export_venv(){

if [[ ! "$(which virtualenv)" ]]; then
echo "no venv found, installing venv"
"${pip}" install virtualenv
export_venv
export virtualenv="$(which virtualenv)"
fi
}

install_venv(){
if [[ "$(which virtualenv)" ]]; then
export virtualenv="$(which virtualenv)"
setup_venv
else
    site_package="$(python3 -m site | awk '/^USER_SITE/ {print $2}'| cut -d"'" -f 2)"
    venv_path=$(echo $site_package| cut -d'/' -f -4)
    if [[ -d "${site_package}" ]] && [[ -f "${venv_path}/bin/virtualenv" ]]; then
    echo "which virtual env"
       export virtualenv="${venv_path}/bin/virtualenv"
    fi
    setup_venv
fi
export python="${ADITAS_VENV_PATH}/bin/python3"
export pip="${ADITAS_VENV_PATH}/bin/pip3"
}

install_django_requirements(){
local req_file="${ADITAS_HOME}/requirements.txt"
if [[ -d "${ADITAS_HOME}" ]] && [[ -f "${req_file}" ]]; then
"${pip}" install -r "${req_file}"
"${python}" "${ADITAS_HOME}/"manage.py makemigrations
"${python}" "${ADITAS_HOME}/"manage.py migrate
"${python}" "${ADITAS_HOME}/"manage.py loaddata "${ADITAS_HOME}/account/fixtures/superuser.json"
fi
}

do_install(){
check_and_set_variables
sanity_check

if [ "$var_sanity_check" == "fail" ]; then
echo "STATUS:sanity check failed "
exit 1
fi

if [ -f "${SQL_SCRIPT}" ]; then
. "${SQL_SCRIPT}"
create_db_and_user
install_venv

export user_ip=$(hostname -I | awk '{ print $1 }')
if [ -f "${VHOST_FILE}" ]; then
. "${VHOST_FILE}"
fi

install_django_requirements
copy_csv_to_default_configuration
fi
}

######################################################################################

case "$1" in
"install")
do_install
;;

"remove")
do_clean
;;

"cleandb")
remove_db_leftovers
;;

esac

