Install
=========


https://github.com/NVIDIA/nvidia-docker


## If you have nvidia-docker 1.0 installed: we need to remove it and all existing GPU containers

   ~$ docker volume ls -q -f driver=nvidia-docker | xargs -r -I{} -n1 docker ps -q -a -f volume={} | xargs -r docker rm -f
   ~$ sudo apt-get purge -y nvidia-docker

## Add the package repositories
   ~$ curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
      sudo apt-key add -
      distribution=$(. /etc/os-release;echo $ID$VERSION_ID)

   ~$ curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-docker.list

## Install nvidia-docker2 and reload the Docker daemon configuration

  ~$ sudo apt-get update
  ~$ sudo apt-get install nvidia-docker2
  ~$ sudo pkill -SIGHUP dockerd

## test it

   ~$ docker run --runtime=nvidia --rm nvidia/cuda:9.0-base nvidia-smi

## test the tensorflow docker image

   ~$ docker run --runtime=nvidia -it -p 8888:8888 tensorflow/tensorflow:latest-gpu

## or open a bash session in the container

   ~$ sudo docker run --runtime=nvidia -it tensorflow/tensorflow:latest-gpu bash


