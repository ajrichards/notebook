


curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update


## make sure docker is about to get pulled from the right place
apt-cache policy docker-ce

## install it
sudo apt-get install -y docker-ce

## check that it is running
~$ sudo systemctl status docker


## ensure you can run docker without sudo

~$ sudo usermod -aG docker ${USER}
~$ su - ${USER}

## the just to be sure
~$ id -nG
