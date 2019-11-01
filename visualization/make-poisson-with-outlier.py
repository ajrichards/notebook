#!/usr/bin/env python

"""
show what outliers are using a poisson distirbution
"""



import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

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

## declare the figure
fig = plt.figure(figsize=(15,8))
ax = fig.add_subplot(111)

a = np.arange(15)

poi = stats.poisson
lambda_ = [2.0, 5.0]
colours = ["#1E88E5", "#F4511E"]

plt.bar(a, poi.pmf(a, lambda_[0]), color=colours[0],
        label="$\lambda = %.1f$" % lambda_[0], alpha=0.60,
        edgecolor=colours[0], lw="3")

plt.bar([12.0], [0.05] , color=colours[1],
        label="$\lambda = %.1f$" % lambda_[1], alpha=0.60,
        edgecolor=colours[1], lw="3")

plt.xticks(a + 0.4, a)
#plt.legend()
plt.ylabel("Probability of $k$")
plt.xlabel("$k$")
#plt.title("Probability mass function of a Poisson");
plt.savefig("poisson-with-outliers.png", dpi=600)
plt.show()

