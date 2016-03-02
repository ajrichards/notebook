#!/usr/bin/python

import cPickle,os


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
