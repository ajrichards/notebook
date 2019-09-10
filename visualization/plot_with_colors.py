"""
To see the different colormaps
https://matplotlib.org/examples/color/colormaps_reference.html
"""

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

x = np.random.randint(1000, size=50)
y = np.random.randint(1000, size=50)
n = x.size

master_list = np.array(["black","magenta","blue"])

fig = plt.figure(figsize=(8,8))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

colors = np.zeros(n,dtype='int')
colors[((x+y)%2)==0] = 1

## plot with a corresponding iterable of explicit colors
color_list = [master_list[c] for c in colors]
ax1.scatter(x,y,s=50,c=color_list)
ax1.set_aspect('equal')
ax1.set_title("Using a list of colors")

## plot with a cmap
s = ax2.scatter(x,y,s=50,c=colors,cmap='inferno')
ax2.set_aspect('equal')
ax2.set_title("Using a cmap")

plt.show()
