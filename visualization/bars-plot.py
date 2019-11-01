#!/usr/bin/env python
"""
bar plot example

DATA:

    data produced by: http://unsdsn.org/about-us/vision-and-organization
    data compilied from: https://worldhappiness.report
"""

import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## plot style and fonts
plt.style.use('seaborn')
SMALL_SIZE = 12
MEDIUM_SIZE = 14 
LARGE_SIZE = 16
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes 
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title 
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=LARGE_SIZE)   # fontsize of the figure title

BLUE = "#0066FF"
ORANGE = "#FF6600"
GREY = "#777777"

data = {2015: {'Australia and New Zealand': 7.285, 'Central and Eastern Europe': 5.332931034482758, 'Eastern Asia': 5.626166666666666, 'Latin America and Caribbean': 6.144681818181818, 'Middle East and Northern Africa': 5.406899999999999, 'North America': 7.273, 'Southeastern Asia': 5.317444444444445, 'Southern Asia': 4.580857142857143, 'Sub-Saharan Africa': 4.202800000000001, 'Western Europe': 6.689619047619048}, 2016: {'Australia and New Zealand': 7.323499999999999, 'Central and Eastern Europe': 5.3706896551724155, 'Eastern Asia': 5.624166666666667, 'Latin America and Caribbean': 6.10175, 'Middle East and Northern Africa': 5.386052631578948, 'North America': 7.254, 'Southeastern Asia': 5.338888888888889, 'Southern Asia': 4.563285714285715, 'Sub-Saharan Africa': 4.136421052631578, 'Western Europe': 6.685666666666665}, 2017: {'Australia and New Zealand': 7.299000024795535, 'Central and Eastern Europe': 5.409931034877382, 'Eastern Asia': 5.646666606267293, 'Latin America and Caribbean': 5.957818193869158, 'Middle East and Northern Africa': 5.369684194263659, 'North America': 7.154500007629395, 'Southeastern Asia': 5.444875001907348, 'Southern Asia': 4.628428561346871, 'Sub-Saharan Africa': 4.111948722448104, 'Western Europe': 6.703714302607945}}

df = pd.DataFrame(data)
df['average'] = (df[2015] + df[2016] + df[2017]) / 3

regions = np.array(list(df.index))
year_2015 = df[2015].values
year_2016 = df[2016].values
year_2017 = df[2017].values
averages = df['average'].values
sorted_inds = np.argsort(averages)

fig = plt.figure(figsize=(10,12))
ax = fig.add_subplot(111)

## make bar plot
N = regions.size
ind = np.arange(N)
width = 0.3

rects1 = ax.bar(ind, year_2015[sorted_inds], width, color=BLUE, label='2015')
rects2 = ax.bar(ind+width, year_2016[sorted_inds], width, color=ORANGE, label='2016')
rects3 = ax.bar(ind+width+width, year_2017[sorted_inds], width, color=GREY, label='2017')

ax.set_xticks(ind+width)
ax.set_xticklabels(regions[sorted_inds],rotation=90)

ax.legend()

plt.show()
#plt.savefig("bar.png",bbox_inches='tight',pad_inches = 0,dpi=500) 
