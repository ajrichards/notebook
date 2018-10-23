install
----------

If you do not care about the latest version

   ~$ sudo apt install docker.io


https://docs.docker.com/engine/installation/linux/ubuntulinux/

add the following to /etc/apt/sources.list

   deb https://apt.dockerproject.org/repo ubuntu-xenial main


   ~$ sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
   ~$ sudo apt-get update
   ~$ sudo apt-get install docker-engine


