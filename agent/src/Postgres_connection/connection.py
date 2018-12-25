import os

import psycopg2

db = os.getenv("postgres_db")
user_name = os.getenv("postgres_user")
user_pass = os.getenv("postgres_password")
host = os.getenv("postgres_host")
port = os.getenv("postgres_port")


def get_postgres_connection():
    '''
    :return: Returns postgres connection
    '''
    conn = psycopg2.connect(database=db, user=user_name, password=user_pass,
                            host=host,
                            port=port)
    return conn
