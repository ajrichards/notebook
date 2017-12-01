HOWTO
---------

Directories are setup as overarching categories
Subdirectores are setup as topics within those categories

e.g.

  * Supervised-learning

    * support-vector-machines
    * k-nearest neighbor
    * ...

Each subdirectory or topic contains a README.rst

Render topic README to simple html

.. code-block:: bash

   pandoc HOWTO.rst -f rst -t html -o HOWTO.html


Render a topic README to a nicer html

The html and css templates are borrowed from `<https://github.com/tonyblundell/pandoc-bootstrap-template>`_

.. code-block:: bash

   pandoc HOWTO.rst -f rst -t html -o HOWTO.html --template template.html --css template.css --self-contained
