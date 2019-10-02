Resource
-------------

https://www.fullstackpython.com/blog/install-mysql-ubuntu-1604.html




Install
----------

   ~$ sudo apt-get install mysql-server
   ~$ sudo mysql_secure_installation


working with mysql databases

Reset root password

Create a user
-----------------

   ~$ sudo mysql -u root
   ~$ CREATE USER 'mynewuser'@'localhost' IDENTIFIED BY 'goodPassword';

As a side note you can turn off the password validation if logged in as root with

   ~$ uninstall plugin validate_password;

Then grant privileges..

   ~$ GRANT ALL PRIVILEGES ON * . * TO 'mynewuser'@'localhost';
   ~$ FLUSH PRIVILEGES;

Then reconnect with the user to ensure that it works

   ~$ mysql -u mynewuser -p

Create a database
-----------------------

   ~$ mysql -u someuser -p
   ~$ CREATE DATABASE somedb;

Import a db dump
----------------------

   ~$  mysql -u username -p database_name < file.sql
