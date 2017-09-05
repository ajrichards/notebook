
basic driver install
--------------------

   ~$ sudo apt-get purge nvidia-*
   ~$ sudo add-apt-repository ppa:graphics-drivers/ppa
   ~$ sudo apt-get update
   ~$ sudo apt-get install nvidia-375

basic cuda install
--------------------

Download cuda

   Get download from here:
   https://developer.nvidia.com/cuda-downloads

   or
   
      ~$  wget https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64-deb

   Then finish main install

      ~$ sudo dpkg -i cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64-deb
      ~$ sudo apt-get update
      ~$ sudo apt-get install cuda


   Install the available patch

   

      
Add the following to your .bashrc
      
   export PATH="/usr/local/cuda/bin:$PATH"
   export LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"
   export GLPATH=/usr/lib

restart terminal


GCC fix
-------------------

~$ sudo apt-get install gcc-5 g++-5
~$ sudo ln -s /usr/bin/gcc-5 /usr/local/cuda/bin/gcc

test it

   ~$ cd /usr/local/cuda/samples/1_Utilities/deviceQuery
   ~$ sudo make
   ~$ ./deviceQuery

   ~$ cd /usr/local/cuda/samples/2_Graphics/marchingCubes
   ~$ sudo make
   ~$ ./marchingCubes


Pycuda
-------------

   ~$ pip install pycuda

   
Ensure that theano works
-------------------------

http://deeplearning.net/software/theano/tutorial/using_gpu.html
