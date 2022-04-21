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

-- Role: django (change pwd for django so that everyone uses the same pwd)
-- DROP ROLE IF EXISTS django;

-- CREATE ROLE django WITH
--   LOGIN
--   NOSUPERUSER
--   INHERIT
--   CREATEDB
--   NOCREATEROLE
--   REPLICATION
--   ENCRYPTED PASSWORD 'SCRAM-SHA-256$4096:mAEvgBr5Cx/WRdNnD6zpAg==$6E5fs8M7BVoA8CwZ5Y4szmpQmAwbvBNX9H8CC40+r6c=:PRoinnZwg7vcA4yiwHxO+D5KQal8hKDRMmquikGoNMI=';

-- COMMENT ON ROLE django IS 'django-db user';

GRANT ALL ON DATABASE "django-db" TO django;