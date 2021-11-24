#!/usr/bin/env python

#import re,csv,sys
#import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib as mpl

import warnings
warnings.filterwarnings("ignore")

def draw_weighted_network(edge_weights,fig_name='toy_graph.png',font_size = 12):
    """
    INPUT: dictionary with edge weights
    """

    color_range = (0,1)
    
    ## specify the graph
    edge_dict = {"e1":("X1","X4"),"e2":("X1","X5"),"e2":("X1","X6"),"e4":("X1","X7"),
                 "e5":("X2","X4"),"e6":("X2","X5"),"e7":("X2","X6"),"e8":("X2","X7"),
                 "e9":("X3","X4"),"e10":("X3","X5"),"e11":("X3","X6"),"e12":("X3","X7")}
               
    ## initialize the axes
    fig = plt.figure(figsize=(12,10))
    
    ## initialize the graph
    G = nx.Graph()
    
    for edge_name,edge in edge_dict.items():
        G.add_edge(edge[0],edge[1],weight=edge_weights[edge_name])

    # explicitly set positions
    pos={"X1":(0.5,2),
         "X2":(3,2),
         "X3":(5.5,2),
         "X4":(1,1),
         "X5":(2.5,1),
         "X6":(3.5,1),
         "X7":(5,1)}

    ## get insignificant edges
    is_edges = [(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] > 0.1]

    # plot the network (ax1)
    node_size = 2000
    colors = [edge[2]['weight'] for edge in G.edges_iter(data=True)]
    cmap = plt.cm.RdBu
    
    ax1 = fig.add_axes([0.3, 0.0, 0.7, 1.0])  # l,b,r,t
    nx.draw(G,pos,node_size=node_size,edge_color=colors,width=4,edge_cmap=cmap,edge_vmin=color_range[0],edge_vmax=color_range[1],ax=ax1)
    nx.draw_networkx_nodes(G,pos,node_size=node_size,nodelist=["X1","X2","X3"],node_color='#FF6600',with_labels=True,ax=ax1)
    nx.draw_networkx_nodes(G,pos,node_size=node_size,nodelist=["X4","X5","X6","X7"],node_color='#0066FF',with_labels=True,ax=ax1)
    nx.draw_networkx_edges(G,pos,edgelist=is_edges,width=1,edge_color='k',style='dashed',ax=ax1)
    nx.draw_networkx_labels(G,pos,font_size=font_size,font_color='k',font_family='sans-serif',font_weight='bold',alpha=1.0,ax=ax1)
    
    # add an axis for the legend (ax2)
    ax2 = fig.add_axes([0.05,0.25,0.27,0.69]) # l,b,w,h
    ax2.set_yticks([])
    ax2.set_xticks([])
    ax2.set_frame_on(True)
    ax2.text(0.1,0.89,r"$X1$ = species richness",color='k',fontsize=font_size,ha="left", va="center")
    ax2.text(0.1,0.78,r"$X2$ = CO$_2$ treatment",color='k',fontsize=font_size,ha="left", va="center")
    ax2.text(0.1,0.67,r"$X3$ = N treatment",color='k',fontsize=font_size,ha="left", va="center")
    ax2.text(0.1,0.56,r"$X4$ = synchrony",color='k',fontsize=font_size,ha="left", va="center")
    ax2.text(0.1,0.45,r"$X5$ = environment variance ($\Sigma^{2}_{e}$)",color='k',fontsize=font_size,ha="left", va="center")
    ax2.text(0.1,0.34,r"$X6$ = community biomass",color='k',fontsize=font_size,ha="left", va="center")
    ax2.text(0.1,0.23,r"$X7$ = demographic variance ($\Sigma^{2}_{d}$)",color='k',fontsize=font_size,ha="left", va="center")

    ## add a colormap (ax3)
    ax3 = fig.add_axes([0.05, 0.05, 0.27, 0.12]) # l,b,w,h
    norm = mpl.colors.Normalize(vmin=color_range[0], vmax=color_range[1])
    cb1 = mpl.colorbar.ColorbarBase(ax3,cmap=cmap,
                                    norm=norm,
                                    orientation='horizontal')

    plt.savefig(fig_name)
    plt.show()
    
if __name__ == "__main__":
    print("foo")


    edge_weights = {"e1":0.5,"e2":0.1,"e2":0.2,"e4":0.3,
                    "e5":0.4,"e6":0.3,"e7":0.3,"e8":0.9,
                    "e9":0.2,"e10":0.2,"e11":0.9,"e12":0.4}

    draw_weighted_network(edge_weights)
