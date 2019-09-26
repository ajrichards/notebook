
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


sudo apt-get update
sudo apt-get -y install build-essential
sudo apt-get -y install python3 python3-pip
sudo apt-get -y install python3-dev
sudo apt-get install python ipython jupyter
sudo apt-get install python3-scipy python3-numpy python3-pandas python3-matplotlib python3-seaborn

sudo chown adam:adam -R /usr/share/jupyter

pip install -U setuptools
pip install -U sphinx
pip install -U sphinxcontrib-bibtex
pip install -U sphinx-rtd-theme
pip install -U nbsphinx
pip install RISE

jupyter-nbextension install rise --py --sys-prefix
jupyter-nbextension enable rise --py --sys-prefix
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
jupyter nbextension enable spellchecker/main
jupyter notebook


# install requirements first
RUN pip3 install --upgrade pip
RUN 
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install -r /code/requirements.txt


    
update and install the essentials

.. code-block:: bash

    ~$ conda update --all
    ~$ conda install sphinx
