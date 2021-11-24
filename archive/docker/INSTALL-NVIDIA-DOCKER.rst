Install
=========


https://github.com/NVIDIA/nvidia-docker

## ensure that the 18.04 version of docker is installed even if you are on 18.10

   ~$ sudo apt purge docker*
   ~$ sudo apt install docker-ce=5:18.09.1~3-0~ubuntu-bionic

   ~$ curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
      sudo apt-key add -
   ~$ curl -s -L https://nvidia.github.io/nvidia-docker/ubuntu18.04/nvidia-docker.list | \
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

   ~$ sudo docker run -u $(id -u):$(id -g) -v ~/repos/notebook:/home/notebook --runtime=nvidia -it tensorflow/tensorflow:latest-gpu-py3 bash

Then cd into /home/notebook and

   ~$ python test-tensorflow-gpu.py 
