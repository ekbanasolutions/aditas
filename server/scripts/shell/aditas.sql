SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = :'db_name';

REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM :c_user;
REVOKE ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public FROM :c_user;
REVOKE ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public FROM :c_user;

DROP DATABASE :db_name;

REASSIGN OWNED BY :c_user TO postgres;
DROP OWNED BY :c_user;

-- DROP ROLE IF EXISTS :c_user;
DROP USER IF EXISTS :c_user;