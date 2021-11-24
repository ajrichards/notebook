
Ubuntu specific commands
============================


system related
-----------------

Get os version

.. code-block:: bash

    ~$ lsb_release -a


install related
---------------------

install pycharm

.. code-block:: bash

    ~$ sudo snap install [pycharm-professional|pycharm-community] --classic


python related
--------------------


ensure you have the latest...
https://www.anaconda.com/distribution/

.. code-block:: bash

    ~$ rm -rf ~/.ipython		
    ~$ rm -rf ~/.conda
    ~$ rm -rf ~/anaconda3


sudo apt update
sudo apt -y install build-essential
sudo apt -y install python3 python3-pip
sudo apt -y install python3-dev
sudo apt -y install jupyter-core
sudo apt -y install jupyter-notebook

pip install -U -r requirements.txt


## NEXT TIME MIGHT WANT TO CONSIDER jupyter from pip
for some reason it went here ~/.local/bin/jupyter-nbextension 

## configureing jupyter

~$ pip install jupyter_contrib_nbextensions && jupyter contrib nbextension install 
~$ pip install jupyter_contrib_nbextensions
~$ jupyter contrib nbextension install --user

~$ pip install -U RISE
~$ jupyter-nbextension install rise --py --sys-prefix
~$ jupyter-nbextension enable rise --py --sys-prefix
~$ jupyter nbextension enable spellchecker/main



