#!/usr/bin/env python
"""
functions dealing with the runtime of scripts

"""

import time


### simple timer
runStart = time.time()
time.sleep(2)
runStop = time.time()

m, s = divmod(runStop-runStart, 60)
h, m = divmod(m, 60)
print "%d:%02d:%02d" % (h, m, s)


     
