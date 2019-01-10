#!/usr/env/python

"""
simple neural network example to model cosine data
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('bmh')

x_train = np.linspace(-3, 3, num=50)
y_train = np.cos(x_train) + np.random.normal(0, 0.1, size=50)
x_train = x_train.astype(np.float32).reshape((50, 1))
y_train = y_train.astype(np.float32).reshape((50, 1))

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

ax.plot(x_train,y_train,color='darkblue',markersize=10,linestyle='none',marker='s')
ax.set_aspect(1./ax.get_data_ratio())

def fix_layout(ax,buff=0.01):
    """use x and y to add well spaced margins"""
    xmin,xmax = ax.get_xlim()
    ymin,ymax = ax.get_ylim()
    xbuff = buff * (xmax - xmin)
    ybuff = buff * (ymax - ymin)
    ax.set_xlim(xmin-xbuff,xmax+xbuff)
    ax.set_ylim(ymin-ybuff,ymax+ybuff)

fix_layout(ax)

    
plt.show()

print("done")
