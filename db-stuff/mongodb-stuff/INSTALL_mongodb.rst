remove anything old
---------------------
  ~$ sudo rm /var/lib/mongodb/mongod.lock
  ~$sudo apt-get purge mongodb mongodb-clients mongodb-server mongodb-dev
  ~$ sudo apt-get purge mongodb-10gen
  ~$ sudo apt-get autoremove

add the repo (to keep things uptodate)
---------------------------------------------------

  ~$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
  
open the following file
  ~$ sudo emacs -nw /etc/apt/sources.list

add these two lines to the end of the file
  ## mongodb
  deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse
  
install the 10gen version of mongodb
--------------------------------------

  ~$ sudo apt-get update
  ~$ sudo apt-get install -y mongodb-org
  ~$ sudo pip install pymongo
  
