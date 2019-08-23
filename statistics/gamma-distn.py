#!/usr/bin/env python 
"""
The Gamma is a probability distribution over a positive random variable τ > 0 
It is governed by parameters a and b that are subject to the constraints a > 0 and b > 0 
The constraints exist to ensure that the distribution can be normalized.

Special case of a = 1 is known as the exponential distribution.

scipy.stats
With a shape parameter α = k and an inverse scale parameter β = 1/θ, called a rate parameter.

"""

import sys,os
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs

## declare variables
font_size = 11
font_name = 'sans-serif'
n = 10000
fig = plt.figure(figsize=(10,6))
splot = 0

## loop through parameterizations of the beta
for a,b in [(1.0,1.0),(3.0,1.0),(5.0,1.0)]:

    b = 1/b
    splot += 1
    ax = fig.add_subplot(1,3,splot)
    
    rv = scs.gamma(a=a,scale=b)
    r = scs.gamma.rvs(size=n,a=a,scale=b)

    ax.hist(r,bins=60,facecolor="#9999FF",alpha=0.7,density=1,histtype='stepfilled')
    pdf_range = np.linspace(scs.gamma.ppf(0.0001, a=a, scale=b),scs.gamma.ppf(0.9999, a=a, scale=b), 100)
    ax.plot(pdf_range, rv.pdf(pdf_range),'#FF0099', lw=4, label='pdf')
    ax.set_xlim((-1,20))
    ax.set_ylim((0,0.5))
    ax.set_title(r"$\alpha$=%s, $\beta$=%s"%(a,b))
    ax.set_aspect(1./ax.get_data_ratio())

    for t in ax.get_xticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)
    for t in ax.get_yticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)
    
plt.show()
