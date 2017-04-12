
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

   The finish install

      ~$ sudo dpkg -i cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64-deb
      ~$ sudo apt-get update
      ~$ sudo apt-get install cuda

Add the following to your .bashrc
      
   export PATH="/usr/local/cuda/bin:$PATH"
   export LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"
   export GLPATH=/usr/lib

restart terminal


test it

   ~$ cd /usr/local/cuda/samples/1_Utilities/deviceQuery
   ~$ sudo make
   ~$ ./deviceQuery

   ~$ cd /usr/local/cuda/samples/2_Graphics/marchingCubes
   ~$ sudo make
   ~$ ./marchingCubes

   

