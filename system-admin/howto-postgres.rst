Ubuntu specific directions
=============================

Basic install
----------------

From a terminal

   $ sudo apt-get install postgresql

Postgres has a superuser built-in called 'postgres' that we perfom admin tasks with

This is how you become the user postgres
--------------------------------------------

   $ sudo su - postgres
   $ psql -U postgres

Create a postgres user
--------------------------

   1. Become the super user 'postgres'

      $ CREATE USER ender WITH ENCRYPTED PASSWORD 'bugger';
      
Create a empty database
----------------------------

   1. Become the super user 'postgres'

      * $ CREATE DATABASE ansible;
      * [optionally] populate db (see below)
      * $ GRANT ALL PRIVILEGES ON DATABASE ansible to ender;

To populate the database with a sql dump
-------------------------------------------

   $ sudo su - postgres
   $ psql ansible < ansible.sql
   
Do not forget to grant privilages to the appropriate user(s)
   
To connect to the db
^^^^^^^^^^^^^^^^^^^^^^^^

From a terminal type

   $ psql -d ansible -U ender
      
