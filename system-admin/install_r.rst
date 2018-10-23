
Add the following two lines to the end of your '/etc/apt/sources.list'

   ## R stuff
   deb http://cran.cnr.berkeley.edu/bin/linux/ubuntu/ xenial/

Add the key to your keyserver

   ~$ gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9
   ~$ gpg -a --export E084DAB9 | sudo apt-key add -
   ~$ sudo apt-get update && sudo apt-get upgrade

Install R
   
   ~$ sudo apt-get install r-base

