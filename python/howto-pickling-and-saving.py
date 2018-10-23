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
results_pickle = 'foo.pickle'

## save it
print("...saving pickle")
tmp = open(results_pickle,'w')
cPickle.dump(results,tmp)
tmp.close()

## load it
print("...loading pickle")
tmp = open(results_pickle,'r')
loadedResults = cPickle.load(tmp)
tmp.close()

## clean up
print loadedResults
os.system("rm %s"%results_pickle)
print("done")


#######################################
## Saving multiple arrays NumPy
#######################################

a = np.arange(10)
b = np.arange(12)

## save it
file_name = 'foo.npz'
args = {'a':a,'b':b}
np.savez_compressed(file_name,**args)

## load it
npz = np.load(file_name)
print npz
print npz.keys()

a = npz['a']
b = npz['b']

print a
print b

## clean up
os.system("rm %s"%file_name)
