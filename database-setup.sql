DROP DATABASE IF EXISTS "user_management_db";

CREATE DATABASE "user_management_db"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

COMMENT ON DATABASE "django-db"
    IS 'Used for the Django project';

GRANT ALL ON DATABASE "django-db" TO postgres;

GRANT TEMPORARY, CONNECT ON DATABASE "django-db" TO PUBLIC;
-- Password = django
DROP ROLE IF EXISTS django;

CREATE ROLE django WITH
  LOGIN
  NOSUPERUSER
  INHERIT
  CREATEDB
  NOCREATEROLE
  REPLICATION
  ENCRYPTED PASSWORD 'SCRAM-SHA-256$4096:vOa3G04Vm8GyrGMXbAloIg==$/mqyErND/C1elg1A9GtdJdhlyUuiQmJ9O9/mG7Po+r8=:/Qw3wdAf8h3CSXMq3C64Bc7OPtwu4RdNDP8OzBzbll8=';

COMMENT ON ROLE django IS 'django-db user';

GRANT ALL ON DATABASE "django-db" TO django;