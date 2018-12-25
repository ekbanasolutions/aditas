 vhost=$(cat <<EOF
 Listen 11600
 <VirtualHost $user_ip:11600>
    # error and acces logs
 ErrorLog \${APACHE_LOG_DIR}/aditas_error.log
     CustomLog \${APACHE_LOG_DIR}/aditas_access.log combined

 Alias /static ${ADITAS_HOME}/static

 <Directory ${ADITAS_HOME}/static>
     Require all granted
 </Directory>

 <Directory ${ADITAS_HOME}/bigdata_administer>
     <Files wsgi.py>
         Require all granted
     </Files>
 </Directory>

 WSGIDaemonProcess aditas python-path=${ADITAS_HOME} python-home=$python

 WSGIProcessGroup aditas

 WSGIScriptAlias / ${ADITAS_HOME}/bigdata_administer/wsgi.py \
          application-group=%{GLOBAL}
 </VirtualHost>
EOF
 )

env=$(cat <<EOF
secret_key=70hw&&3en4emtk-miqi6&koswmkcrnyxjd)j*qhl^9)@u9jn^$
debug=False
allowed_hosts=$user_ip,localhost,127.0.0.1,aditas.ekbana.net
NAME=$db_name
HOST=$host
PORT=$port
USER=$c_user
PASSWORD=$c_pass
EOF
)

echo "$vhost">"${ADITAS_HOME}/aditas.conf"
mkdir -p "/etc/aditas/server/conf"
echo "$env">"/etc/aditas/server/conf/server.env"

