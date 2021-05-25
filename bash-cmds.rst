Return the name of your Ubuntu release

.. code::

   lsb_release -cs


fix an ntfs hard disk that was usb mounted but becuse it was now ejected correctly it is READ-ONLY
You can find out the location using the 'disks' program

.. code::

   sudo ntfsfix /dev/sdc2
