
basic install
--------------------

sudo apt-get purge nvidia-*
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-get update
sudo apt-get install nvidia-375


Other notes
---------------------

manually rebuild the kernel module of the nvidia driver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   ~$ dpkg-reconfigure nvidia-current

If you are using nvidia I believe that only the lightdm works as a display manager

   ~$ dpkg-reconfigure gdm


howto run examples
---------------------


cd /root/NVIDIA_CUDA-7.0_Samples/ 


BUGS in 375
----------------

https://bugs.launchpad.net/ubuntu/+source/nvidia-graphics-drivers-375/+bug/1662860
