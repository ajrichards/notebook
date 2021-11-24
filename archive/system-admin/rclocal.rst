(1) create the file in /etc/rc.local with the following header

   #!/bin/sh -e

(2) put your contents in there e.g.

   echo 0 > /sys/module/hid_apple/parameters/iso_layout
