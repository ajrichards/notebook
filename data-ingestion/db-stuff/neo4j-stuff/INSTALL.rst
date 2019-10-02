
first install java
-----------------------

edit your sources file

  ~$ sudo emacs -nw /etc/apt/sources.list

by adding the following lines

  ## java
  deb http://ppa.launchpad.net/webupd8team/java/ubuntu bionic main
  deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu bionic main

Then add the key
  
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  



Install Neo4j
-----------------

   ~$ wget --no-check-certificate -O - https://debian.neo4j.org/neotechnology.gpg.key | sudo apt-key add -
   ~$ echo 'deb http://debian.neo4j.org/repo stable/' | sudo tee /etc/apt/sources.list.d/neo4j.list
   ~$ sudo apt update
   ~$ sudo apt-get install neo4j
   
