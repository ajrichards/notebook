#!/usr/bin/python
"""
cPickle works well and it is very flexible, but if array only data are available 
numpy's save features can provide better read speed
"""

import pickle,os
import numpy as np

#######################################
## Basic pickle example
#######################################

results = {'a':1,'b':range(10)}
results_pickle = 'foo.pickle'

if not os.path.exists(results_pickle):

    ## save it
    print("...saving pickle")
    with open(results_pickle,'wb') as tmp:
        pickle.dump(results,tmp)
else:
    ## load it
    print("...loading pickle")
    with open(results_pickle,'rb') as tmp:
        loaded_results = pickle.load(tmp)
    
## clean up
#print(loadedResults)
#os.system("rm %s"%results_pickle)
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
print(npz)
print(npz.keys())

a = npz['a']
b = npz['b']

print(type(a))
print(type(b))

## clean up
os.system("rm %s"%file_name)

## see also pandas to_pickle
## see also numpy save 
