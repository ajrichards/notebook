#!/usr/bin/env python 
"""
fit a beta distribution with several parameterizations
"""

import sys,os
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs


plt.style.use('seaborn')

SMALL_SIZE = 18
MEDIUM_SIZE = 20
LARGE_SIZE = 22

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=LARGE_SIZE)   # fontsize of the figure title

## declare variables
n = 10000
fig = plt.figure(figsize=(10,6))
splot = 0

## loop through parameterizations of the beta
for a,b in [(4,8),(5,2),(5,5)]:
    splot += 1
    ax = fig.add_subplot(1,3,splot)
    
    rv = scs.beta(a,b)
    r = scs.beta.rvs(a,b,size=1000)
    pdf_range = np.linspace(scs.expon.ppf(0.01),scs.expon.ppf(0.99), 100)

    ax.hist(r,bins=60,facecolor="#1E88E5",alpha=0.7,density=1,histtype='stepfilled')
    ax.plot(pdf_range, rv.pdf(pdf_range), '#F4511E', lw=5, label='frozen pdf')
    ax.set_xlim((0,1))
    ax.set_title(r"$\alpha$=%s, $\beta$=%s"%(a,b))
    ax.set_aspect(1./ax.get_data_ratio())
    plt.suptitle("Beta Distribution")
    
plt.savefig("beta-distn.png",dpi=600)    
plt.show()
