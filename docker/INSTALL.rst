install
----------

https://docs.docker.com/engine/installation/linux/ubuntulinux/

If you do not care about the latest version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   ~$ sudo apt install docker.io

Otherwise install from docker repo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First ensure apt working over https

   ~$ sudo apt-get install apt-transport-https ca-certificates curl software-properties-common

Add the key

   ~$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

Verify the key has the following fingerprint 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88

   ~$ sudo apt-key fingerprint 0EBFCD88

Setup the repo

   ~$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

## install

   ~$ sudo apt-get update
   ~$ sudo apt-get install docker-ce

## test it

   ~$ sudo docker run hello-world

  
