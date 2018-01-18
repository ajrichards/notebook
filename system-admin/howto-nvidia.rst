
basic driver install
--------------------

   ~$ sudo apt-get purge nvidia-*
   ~$ sudo add-apt-repository ppa:graphics-drivers/ppa
   ~$ sudo apt-get update
   ~$ sudo apt-get install nvidia-387
   ~$ sudo apt-get install nvidia-modprobe
   
Reboot and check to see if the install worked
   
   ~$ lsmod | grep nvidia 

Also you should be able to run `nvidia-settings`
   
basic cuda install
--------------------

Download cuda

   Get download from here:
   https://developer.nvidia.com/cuda-downloads

   Then finish main install


    ~$ sudo dpkg -i cuda-repo-ubuntu1704-9-1-local_9.1.85-1_amd64.deb
    ~$ sudo apt-key add  /var/cuda-repo-9-1-local/7fa2af80.pub
    ~$ sudo apt-get update
    ~$ sudo apt-get install cuda
      
Add the following to your .bashrc
      
   export PATH="/usr/local/cuda-9.1/bin:$PATH"
   export LD_LIBRARY_PATH="/usr/local/cuda-9.1/lib64:$LD_LIBRARY_PATH"
   export GLPATH=/usr/lib


   
restart terminal


GCC fix
-------------------

~$ sudo apt-get install gcc-6 g++-6
~$ sudo ln -s /usr/bin/gcc-6 /usr/local/cuda-9.1/bin/gcc
~$ sudo ln -s /usr/bin/g++-6 /usr/local/cuda-9.1/bin/g++

test it

   ~$ cd /usr/local/cuda-9.1/samples/1_Utilities/deviceQuery
   ~$ sudo make
   ~$ ./deviceQuery

   ~$ cd /usr/local/cuda-9.1/samples/2_Graphics/marchingCubes
   ~$ sudo make
   ~$ ./marchingCubes


Pycuda
-------------

   ~$ pip install pycuda

   
Ensure that theano works
-------------------------

http://deeplearning.net/software/theano/tutorial/using_gpu.html
