#!/usr/bin/env python
"""
tinkering with distance matrices

here is a good place to visit if you are lost
http://docs.scipy.org/doc/scipy/reference/spatial.distance.html

note that pdist is generic for m dimensions
cdist can work as well when we have only 2 dimensions
"""

import numpy as np
import scipy.spatial.distance as dist
from scipy.spatial.distance import cdist,pdist,squareform

## try to think of all possible distances between obsevations as a matrix
x1 = np.array([[1,0,1,1]]).T
x2 = np.array([[1,1,1,1]]).T
x3 = np.array([[0,0,0,0]]).T
observation_names = ['obs1','obs2','obs3','obs4']

## organize your data as observations by features
x = np.hstack([x1,x2,x3])
print("\nx (%s observations, %s features)"%(x.shape[0],x.shape[1]))
print(x)

## calculate distance (change the metric)
distance_metric = 'euclidean'
_m = pdist(x,distance_metric)
m = squareform(_m)

## save my distances in a dict
print("\nall pairwise distances in x")
distances = {}
for o1,obs1 in enumerate(observation_names):
    for o2, obs2 in enumerate(observation_names):
        if o1 >= o2:
            continue
        print("d(%s,%s) = %s"%(obs1,obs2,m[o1,o2]))
        distances[obs1+'-'+obs2] = m[o1,o2]

## demonstrate how to compute distances one at a time e.g if you have a new point and just want to append to the matrix
## also show that you can compute euclidean distance several ways
print("\ngot some new observation...")
next_obs = np.array([[0,1,0]])
for i in range(x.shape[0]):
    obs_i = x[i,:]
    dist1 = dist.dist.euclidean(obs_i,next_obs)                                ## using scipy
    dist2 = np.linalg.norm(obs_i-next_obs)                                ## using norm of the difference
    dist3 = np.sqrt(np.sum( (a - b)**2 for a, b in zip(obs_i, next_obs))) ## by hand
    print(dist1,dist2,dist3)

## or more efficiently
new_dist = cdist(x, next_obs, 'euclidean')
print(new_dist)
    
