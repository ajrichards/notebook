#!/usr/bin/env python

import sys
import numpy as np

a = np.arange(10)
b = np.array([3,4,5])

mask1 = np.in1d(a,b)
mask2 = np.in1d(b,a)
print('mask1',mask1)
print('mask2',mask2)

