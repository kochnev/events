create user events_admin with password '123456789';
alter user events_admin createdb;
alter user events_admin set client_encoding to 'utf8';
alter user events_admin set default_transaction_isolation to 'read committed';
alter user events_admin set timezone to 'UTC';

create database events owner events_admin;