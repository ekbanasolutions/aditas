import hashlib
from bigdata_logs.logger import getLoggingInstance
log = getLoggingInstance()
from Postgres_connection.connection import get_postgres_connection


def get_apiKey():
    encrypted_api_key = None
    try:
        conn = get_postgres_connection()
        cur = conn.cursor()
        sql = "select key from security_api_key"
        cur.execute(sql)
        row = cur.fetchone()
        key = ''.join(row)
        key = key.strip()

        encrypted_api_key = hashlib.md5(key.encode()).hexdigest()

        cur.close()
    except Exception as e:
        log.error(e)
    return encrypted_api_key


def check_apiKey(header_key):
    print("key: %s" % header_key)

    if header_key is None:
        return '{"success": 0, "msg": ["API-Key not provided!!!"]}'

    api_key_db = get_apiKey()

    if header_key == api_key_db:
        return 'success'
    else:
        return '{"success": 0, "msg": ["API-Key does not match!!!"]}'
