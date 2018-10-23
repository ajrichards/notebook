#!/usr/bin/env python
"""
multi-level example with GLM

pooling - just run a regression on all data and assess 

"""

import os
import matplotlib.pyplot as plt
import numpy as np
import pymc3 as pm
import pandas as pd


np.random.seed(42)
n = 20
b0_true = -0.3
b1_true = 0.5
x,y = get_simple_regression_samples(n,b0=b0_true,b1=b1_true,error)

## simulate data
b0a_true = -0.3
b1a_true = 0.5
x1,y1 = get_simple_regression_samples(n,b0=b0a_true,b1=b1a_true,error=0.12)

b0b_true = -0.3
b1b_true = 0.5
x2,y2 = get_simple_regression_samples(n,b0=b0b_true,b1=b1b_true,error=0.15)

b0a_true = -0.3
b1a_true = 0.5
x3,y3 = get_simple_regression_samples(n,b0=b0_true,b1=b1a_true,error=0.18)

print


## create scatter of data
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

## run unpooled model


## run pooled model
print("exiting early...")
sys.exit()


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
