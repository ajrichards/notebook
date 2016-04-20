#!/usr/bin/env python

import numpy as np

a = np.arange(10)
b = np.array([3,4,5])

mask1 = np.in1d(a,b)
mask2 = np.in1d(b,a)

print mask1
print mask2

mask2Inds = np.where(mask2==True)[0]
#mask12nds = map(lambda x: 1 if x else 0, mask1)

print mask2Inds
print b[mask2]
print b[mask2Inds]
