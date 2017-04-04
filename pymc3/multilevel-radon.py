#!/usr/bin/env python
"""
multi-level example with GLM

Gelman et al.s (2007) radon dataset is a classic for hierarchical modeling

Radon gas is known to be the highest cause of lung cancer in non-smokers.

Here welll investigate this differences and try to make predictions of
radon levels predictions are for in different counties based on the
county itself and the presence of a basement.

radon_ic = b0 +b1*floor_ic + epison

The radon level (i) in county (c) is a linear function of radon levels that
considers multiple levels for the floor

There are 85 counties in MN

pooling - just run a regression on all data and assess 


"""

import os
import matplotlib.pyplot as plt
import numpy as np
import pymc3 as pm
import pandas as pd

data = pd.read_csv('radon.csv')

county_names = data.county.unique()
county_idx = data.county_code.values

n_counties = len(data.county.unique())

print("total counties: %s"%(n_counties))

print data[['county', 'log_radon', 'floor']].head()

## unpooled
############################################################################

run_trace = False
with pm.Model() as unpooled_model:

    # Independent parameters for each county
    a = pm.Normal('a', 0, sd=100, shape=n_counties)
    b = pm.Normal('b', 0, sd=100, shape=n_counties)

    # Model error
    eps = pm.HalfCauchy('eps', 5)
    
    # Model prediction of radon level
    # a[county_idx] translates to a[0, 0, 0, 1, 1, ...],
    # we thus link multiple household measures of a county
    # to its coefficients.
    radon_est = a[county_idx] + b[county_idx]*data.floor.values
    
    # Data likelihood
    y = pm.Normal('y', radon_est, sd=eps, observed=data.log_radon)

    
with unpooled_model:
    trace_pickle = "traces/unpooled_radon.pkl"
    if run_trace or not os.path.exists(trace_pickle):
        tmp = open(trace_pickle,'w')
        unpooled_trace = pm.sample(niter, step, start,random_seed=123, progressbar=True)
        cPickle.dump(trace,tmp)
        tmp.close()
    else:
        print("...loading saved trace")
        tmp = open(trace_pickle,'r')
        unpooled_trace = cPickle.load(tmp)


############################################################################
run_trace = False
with pm.Model() as hierarchical_model:

    # Hyperpriors for group nodes
    mu_a = pm.Normal('mu_a', mu=0., sd=100**2)
    sigma_a = pm.HalfCauchy('sigma_a', 5)
    mu_b = pm.Normal('mu_b', mu=0., sd=100**2)
    sigma_b = pm.HalfCauchy('sigma_b', 5)

    # Intercept for each county, distributed around group mean mu_a
    # Above we just set mu and sd to a fixed value while here we
    # plug in a common group distribution for all a and b (which are
    # vectors of length n_counties).

    a = pm.Normal('a', mu=mu_a, sd=sigma_a, shape=n_counties)

    # Intercept for each county, distributed around group mean mu_a
    b = pm.Normal('b', mu=mu_b, sd=sigma_b, shape=n_counties)

    # Model error
    eps = pm.HalfCauchy('eps', 5)
    
    radon_est = a[county_idx] + b[county_idx] * data.floor.values
    
    # Data likelihood
    radon_like = pm.Normal('radon_like', mu=radon_est, sd=eps, observed=data.log_radon)

# Inference button (TM)!
with hierarchical_model:
    trace_pickle = "traces/hierarchical_radon.pkl"
    if run_trace or not os.path.exists(trace_pickle):
        tmp = open(trace_pickle,'w')
        hierarchical_trace = pm.sample(niter, step, start,random_seed=123, progressbar=True)
        cPickle.dump(trace,tmp)
        tmp.close()
    else:
        print("...loading saved trace")
        tmp = open(trace_pickle,'r')
        hierarchical_trace = cPickle.load(tmp)

# Plotting the hierarchical model trace -its found values- from 500 iterations onwards (right side plot)
# and its accumulated marginal values (left side plot)
pm.traceplot(hierarchical_trace[1000:]);

plt.show()
