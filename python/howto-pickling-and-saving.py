#!/usr/bin/python
"""
cPickle works well and it is very flexible, but if array only data are available 
numpy's save features can provide better read speed

"""

import cPickle,os
import numpy as np

#######################################
## Basic cPickle example
#######################################

results = {'a':1,'b':range(10)}
resultsPickle = 'foo.pickle'

## save it
print("...saving pickle")
tmp = open(resultsPickle,'w')
cPickle.dump(results,tmp)
tmp.close()

## load it
print("...loading pickle")
tmp = open(resultsPickle,'r')
loadedResults = cPickle.load(tmp)
tmp.close()

## clean up
print loadedResults
os.system("rm %s"%resultsPickle)
print("done")


#######################################
## Saving multiple arrays NumPy
#######################################

a = np.arange(10)
b = np.arange(12)

fileName = 'foo.npz'
args = {'a':a,'b':b}
np.savez_compressed(fileName,**args)

npz = np.load(fileName)
print npz
print npz.keys()
a = npz['a']
b = npz['b']

print a
print b
os.system("rm %s"%fileName)
