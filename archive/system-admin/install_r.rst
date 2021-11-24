
Ubuntu
---------


Add the key to your keyserver then add the source

   sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
   sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/'
   sudo apt-get update && sudo apt-get upgrade

Install R
   
   ~$ sudo apt-get install r-base


OSX
-----

~$ brew tap caskroom/cask
~$ brew install caskroom/cask/xquartz
