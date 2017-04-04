#!/usr/bin/env python
"""
Let's say we play a game where I keep flipping a coin until I get
heads. If the first time I get heads is on the nth coin, then I pay
you 2n-1 dollars. How much would you pay me to play this game?

You should end up with a sequence that you need to find the closed
form of. If you don't know how to do this, write some python code that
sums the first 100.

E(W) = sum_{n >= 1} (2n-1)/2^n = 3

"""


import matplotlib.pyplot as plt
import numpy as np

## simulate the number of flips before heads
def coin():
    tails, num_flips = True, 0
    while tails:
        num_flips += 1
        if np.random.binomial(1,0.5):
            tails = False
    return num_flips


if __name__ == '__main__':

    ## simulate
    flips = [coin() for k in xrange(10000)]

    ## get the distribution of counts condition on the number of flips
    range_flips = range(1, max(flips) + 1)
    counts = np.array([flips.count(k)*1. for k in range_flips])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(range_flips,counts,alpha=0.4)
    ax.set_ylabel("counts")
    ax.set_xlabel("num flips to win")
    
    #print [int(i) for i in counts]
    
    winnings = sum([counts[k - 1]*(2*(k)-1)/sum(counts) for k in range_flips])

    #print range_flips
    print winnings
    
    plt.show()
