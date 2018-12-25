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

if [ ! $(which psql) ]; then
echo "postgres client is required to run this application"
var_sanity_check="fail"
fi
}

check_and_set_variables()
{
if [ -z "$sudo_pass" ]; then
export sudo_pass="${sudo_pass}"
fi

if [ -z "$db_name" ]; then
export db_name="${db_name}"
fi

if [ -z "$host" ]; then
echo "ERROR: no host provided.Please run 'dpkg-reconfigure' to configure host ip for database"
exit 1
fi

if [ -z "$port" ]; then
echo "ERROR: no port provided.Please run 'dpkg-reconfigure' to configure port for database"
exit 1
fi

if [ -z "$c_user" ]; then
echo "ERROR: no superuser provided.Please run 'dpkg-reconfigure' to configure superuser for database"
exit 1
fi

if [ -z "$c_pass" ]; then
echo "ERROR: no pass provided.Please run 'dpkg-reconfigure' to configure password for database"
exit 1
fi

export USER="${SUDO_USER}"

export user_ip=$(hostname -I | awk '{ print $1 }')
export hostname=$(hostname)
export fqdn=$(hostname -f | awk '{ print $1 }')

}

remove_db_leftovers(){
check_and_set_variables
if [[ -f "${SQL_SCRIPT}" ]]; then
. "${SQL_SCRIPT}"
uninstall_agent
fi
}

setup_venv(){
if [[ ! -d "${ADITAS_VENV_PATH}" ]]; then
echo "virtual env ${virtualenv}"
"${virtualenv}" "${ADITAS_VENV_PATH}" -p "${python}"
fi
}

export_venv(){

echo "pip: ${pip}"
echo "venv: $(which virtualenv)"

if [[ ! "$(which virtualenv)" ]]; then
echo "no venv found, installing venv"
"${pip}" install virtualenv
export_venv
export virtualenv="$(which virtualenv)"
else
export virtualenv="$(which virtualenv)"
fi
}

install_venv(){
export_venv
setup_venv
export python="${ADITAS_VENV_PATH}/bin/python3"
export pip="${ADITAS_VENV_PATH}/bin/pip3"
}

do_install(){
check_and_set_variables
echo "variables checked: OK"
sanity_check
echo "sanity checked: OK"

if [ "$var_sanity_check" == "fail" ]; then
echo "sanity checked: FAILED "
exit 1
fi

if [ -f "${SET_ENV_FILE}" ]; then
. "${SET_ENV_FILE}"
fi

install_venv

if [ -f "${SQL_SCRIPT}" ]; then
. "${SQL_SCRIPT}"
install_agent
fi

if [[ -f "${ADITAS_HOME}/requirements.txt" ]]; then
"${pip}" install -r "${ADITAS_HOME}/requirements.txt"
fi

chown -R "${USER}:${USER}" ${ADITAS_HOME}

}

case "$1" in
"install")
do_install
;;

"clean")
remove_db_leftovers
;;

esac

