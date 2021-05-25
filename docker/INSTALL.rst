Install Docker
#####################

Ubuntu
--------------

https://docs.docker.com/install/linux/docker-ce/ubuntu/

Ensure you system is up to date
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash
		
    ~$ sudo apt-get update
    ~$ sudo apt-get upgrade

Remove older versions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    ~$ sudo apt-get remove docker docker-engine docker.io containerd runc

Ensure you have the prereqs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. code-block:: bash
   
   ~$ sudo apt-get install apt-transport-https ca-certificates curl 
   ~$ sudo apt-get install gnupg-agent software-properties-common 

If you do not care about the latest version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash
		
    ~$ sudo apt install docker.io

    
Otherwise install from docker repo (suggested)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add the GPG key

.. code-block:: bash

   ~$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   ~$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

Verify the key has the following fingerprint 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88

.. code-block:: bash

   ~$ sudo apt-key fingerprint 0EBFCD88
   ~$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

Install it

.. code-block:: bash

   ~$ sudo apt-get update
   ~$ sudo apt-get install docker-ce docker-ce-cli containerd.io

test it
------------------

.. code-block:: bash

   ~$ sudo docker run hello-world


If you would like to use Docker as a non-root user
----------------------------------------------------

adding your user to the “docker” group with something like

.. code-block:: bash

    sudo usermod -aG docker your-user

Your will need to log out and back in for this to take effect.
