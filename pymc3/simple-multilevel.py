#!/usr/bin/env python
"""
simple multi-level linear regression
"""

import sys, os
#sys.path.insert(0, os.path.expanduser('~/work/git/github/taku-y/pymc3'))
import theano
theano.config.floatX = 'float64'
import matplotlib.pyplot as plt
import numpy as np
import pymc3 as pm
import pandas as pd

import seaborn as sns
sns.set(style="ticks")
plt.style.use('classic')

df = pd.read_csv('radon.csv')
county_names = df.county.unique()
county_idx = df['county_code'].values
n_counties = len(df.county.unique())

print n_counties
print df.columns

# Load the example tips dataset
#tips = sns.load_dataset("tips")
#print tips.shape
#sys.exit()

y = data.log_radon.values
x1 = n_counties.values

# Draw a nested boxplot to show bills by day and sex
sns.boxplot(x=x1, y=y, hue="sex", data=tips, palette="PRGn")
sns.despine(offset=10, trim=True)

plt.show()
