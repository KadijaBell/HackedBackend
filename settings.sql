-- settings.sql
CREATE DATABASE hacked;
CREATE USER hackeduser WITH PASSWORD 'ABC123';
GRANT ALL PRIVILEGES ON DATABASE hacked TO hackeduser;
