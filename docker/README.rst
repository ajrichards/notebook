About
----------

https://docs.docker.com/get-started/#docker-concepts

Docker is a platform for developers and sysadmins to develop, deploy,
and run applications with containers. The use of Linux containers to
deploy applications is called containerization. Containers are not
new, but their use for easily deploying applications is.

A container is launched by running an image. An image is an executable
package that includes everything needed to run an application--the
code, a runtime, libraries, environment variables, and configuration
files.

A container runs natively on Linux and shares the kernel of the host
machine with other containers. It runs a discrete process, taking no
more memory than any other executable, making it lightweight.

common cmds
-------------

sudo systemctl start docker


start it
   ~$ sudo service docker start

test it
   ~$ sudo docker run hello-world

check that it running
   ~$ sudo systemctl status docker


~$ docker ps

~$  docker info

## managing the containers (not chef etc)
swarm, mesos-marathon

Working with a container
----------------------------

## check which images you have

   ~$ docker image ls


## check which containers you have running

   ~$ sudo docker container ls 

   
Removing unused images, containers and volumes
--------------------------------------------------

https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes


## clean up everything

   ~$ docker system prune -a
