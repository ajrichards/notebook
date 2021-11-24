
the tensorflow way
######################


remove everything
--------------------

   ~$ sudo apt-get --purge remove nvidia-4*
   ~$ sudo apt-get --purge remove cuda-*10-*
   ~$ sudo rm -rf /usr/lib/nvidia/*
   ~$ sudo rm -rf /etc/apt/sources.list.d/cuda.list

install the driver
-------------------

~$ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
~$ sudo dpkg -i cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
~$ sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
~$ sudo apt-get update
~$ wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
~$ sudo apt install ./nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
~$ sudo apt-get update
~$ sudo apt-get install --no-install-recommends nvidia-driver-430
~$ sudo apt-get install nvidia-settings

REBOOT

Test the install with

~$ nvidia-smi


Install CUDA
----------------

sudo apt-get install --no-install-recommends \
    cuda-10-0 \
    libcudnn7=7.6.2.24-1+cuda10.0  \
    libcudnn7-dev=7.6.2.24-1+cuda10.0


Install other requirements
----------------------------


~$ sudo apt-get install -y --no-install-recommends libnvinfer5=5.1.5-1+cuda10.0 \
   libnvinfer-dev=5.1.5-1+cuda10.0


Install tensorflow
--------------------
   
By hand
###########

website to help you match cuda with driver
https://docs.nvidia.com/deploy/cuda-compatibility/index.html


Install NVIDIA driver
   
   ~$ sudo add-apt-repository ppa:graphics-drivers/ppa
   ~$ sudo apt-get update
   ~$ sudo apt-get install nvidia-440
   ~$ sudo apt-get install nvidia-modprobe
   
Reboot and check to see if the install worked
   
   ~$ lsmod | grep nvidia 
   ~$ nvidia-smi

.. note::

   before installing CUDA check here which version is the latest that is supported by tensorflow
   https://www.tensorflow.org/install/gpu (10.0 last time I checked)

basic cuda install
--------------------

Download cuda (10.0)

   Get download from here:
   https://developer.nvidia.com/cuda-downloads

   Then finish main install

    ~$ sudo dpkg -i cuda-repo-ubuntu1804-10-0-local-10.0.130-410.48_1.0-1_amd64.deb
    ~$ sudo apt-key add /var/cuda-repo-10-0-local-10.0.130-410.48/7fa2af80.pub
    ~$ sudo apt-get update
    ~$ sudo apt-get install cuda

Create a symbolic link

   ~$ ln -s /usr/local/cuda-9.0 /usr/local/cuda
    
Add the following to your .bashrc

    export PATH="/usr/local/cuda/bin:$PATH"
    export LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"
    export GLPATH=/usr/lib
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/extras/CUPTI/lib64

restart terminal

Add the extra packages
------------------------

~$ wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
~$ sudo apt install ./nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
~$ sudo apt-get install libcudnn7 libcudnn7-dev


TROUBLE SHOOTING
-------------------
   
Also you should be able to run `nvidia-settings`

On ubuntu 18.10 you may need to

   ~$ emacs /etc/gdm3/custom.conf 

and uncomment the line 'waylandEnable=False' line (this forces an xorg login screen)

GCC fix
^^^^^^^^^^^^

~$ sudo apt-get install gcc-6 g++-6
~$ sudo ln -s /usr/bin/gcc-6 /usr/local/cuda/bin/gcc
~$ sudo ln -s /usr/bin/g++-6 /usr/local/cuda/bin/g++

test it

   ~$ cd /usr/local/cuda-9.1/samples/1_Utilities/deviceQuery
   ~$ sudo make
   ~$ ./deviceQuery

   ~$ cd /usr/local/cuda-9.1/samples/2_Graphics/marchingCubes
   ~$ sudo make
   ~$ ./marchingCubes

tensorflow
--------------

sudo apt-get install cuda-command-line-tools-9.0

## add the following to your .bashrc
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH:+${LD_LIBRARY_PATH}:}/usr/local/cuda/extras/CUPTI/lib64

~$ sudo apt-get install libcupti9.1

install cuDNN (download and dpkg -i)

~$ pip install --upgrade tensorflow-gpu



   
Pycuda
-------------

   ~$ pip install pycuda

   
Ensure that theano works
-------------------------

http://deeplearning.net/software/theano/tutorial/using_gpu.html
