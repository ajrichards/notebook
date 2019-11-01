#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def draw_neural_net(ax, left, right, bottom, top, layer_sizes):
    '''
    Draw a neural network cartoon using matplotilb.
    
    :usage:
        >>> fig = plt.figure(figsize=(12, 12))
        >>> draw_neural_net(fig.gca(), .1, .9, .1, .9, [4, 7, 2])
    
    :parameters:
        - ax : matplotlib.axes.AxesSubplot
            The axes on which to plot the cartoon (get e.g. by plt.gca())
        - left : float
            The center of the leftmost node(s) will be placed here
        - right : float
            The center of the rightmost node(s) will be placed here
        - bottom : float
            The center of the bottommost node(s) will be placed here
        - top : float
            The center of the topmost node(s) will be placed here
        - layer_sizes : list of int
            List of layer sizes, including input and output dimensionality
    '''
    n_layers = len(layer_sizes)
    v_spacing = (top - bottom)/float(max(layer_sizes))
    h_spacing = (right - left)/float(len(layer_sizes) - 1)
    
    ## create the nodes with patches
    patch_keys = {}
    for n, layer_size in enumerate(layer_sizes):
        layer_top = v_spacing*(layer_size - 1)/2. + (top + bottom)/2.
        for m in range(layer_size):
            x = n*h_spacing + left
            y = layer_top - m*v_spacing

            if n == 0:
                color = 'darkorange'
                label = 'input'
            elif n == len(layer_sizes)-1:
                color = 'dodgerblue'
                label = 'output'
            else:
                color = 'mediumpurple'
                label = 'hidden'
    
            p = mpatches.Circle((x, y), v_spacing/3.5, ec='k',fc=color)
            patch_keys[label] = p
            ax.add_patch(p)

    ## create the edges with annotations
    for n, (layer_size_a, layer_size_b) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:])):
        layer_top_a = v_spacing*(layer_size_a - 1)/2. + (top + bottom)/2.
        layer_top_b = v_spacing*(layer_size_b - 1)/2. + (top + bottom)/2.
        for m in range(layer_size_a):
            for o in range(layer_size_b):
                a = n*h_spacing + left
                b = (n + 1)*h_spacing + left
                c = layer_top_a - m*v_spacing
                d = layer_top_b - o*v_spacing

                ax.annotate('', xy=(b,d), xycoords='data',
                            xytext=(a,c), textcoords='data',
                            arrowprops=dict(facecolor='black',
                                            arrowstyle='->',
                                            shrinkA=18,
                                            shrinkB=18,
                                            )
               
                )
    ax.legend(patch_keys.values(), patch_keys.keys())

if __name__ == "__main__":

    fig = plt.figure(figsize=(10, 10))
    ax = fig.gca()
    ax.axis('off')
    draw_neural_net(ax, .1, .9, .1, .9, [4, 10, 7, 5,7, 2])

    fig.savefig('nn-complex.png')
    plt.show()
