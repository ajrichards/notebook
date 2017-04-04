install postgres
-----------------------

these notes are Ubuntu specific

~$ sudo apt-get install postgresql


create a user
--------------------------
sudo su - postgres
psql -U postgres
CREATE USER ender WITH ENCRYPTED PASSWORD 'bugger';
\q

create a database
----------------------
sudo su - postgres
psql -U postgres
CREATE DATABASE readychef WITH OWNER ender;
\q

populate a database from a dump
------------------------------------
cd /home/adam/repos/sql/data/      
psql readychef < readychef.sql

## ensure we can login through terminal
sudo emacs -nw /etc/postgresql/9.5/main/pg_hba.conf

then change

    local   all             postgres                                peer
    local   all             postgres                                md5


sudo /etc/init.d/postgresql restart


connect locally to a database
---------------------------------
psql -U ender -d readychef



