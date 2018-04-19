#!/usr/bin/env python
'''
+---------+---------+--------+
|         | winners | losers |
+---------+---------+--------+
| Drug    |   90    |   10   |
+---------+---------+--------+
| Placebo |   80    |   20   |
+---------+---------+--------+

If we were interested in comparing the proportion
of winners based on drug and placebo treatments
we could use a fisher's exact test

'''

import numpy as np
import scipy.stats as stats


table = np.array([[90,10],[80,20]])

print(table)

results = stats.fisher_exact(table)
print(results)
