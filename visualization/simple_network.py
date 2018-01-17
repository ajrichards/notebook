#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

import warnings
warnings.filterwarnings("ignore")


def draw_network(edge_dict,file_name=None,ax=None,node_size=500,k=10):
    """draw a simple network"""
    if not ax:
        fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot(111)
        ax.set_yticks([])
        ax.set_xticks([])

    G = nx.Graph()
    for edge,weight in edge_dict.items():
        G.add_edge(edge[0],edge[1],weight=weight)

    pos=nx.spring_layout(G,k=k)

    ## draw the nodes                                                                                                          
    nx.draw_networkx(G,pos,node_size=node_size,
                     node_color='#ADD8E6',alpha=0.9,ax=ax)

    ax.axis('off')
    
    if file_name:
        plt.savefig(file_name)

if __name__ == "__main__":
    np.random.seed(42)
    edge_dict = {("A","B"):1,("B","C"):1,("A","C"):1,("A","E"):1}
    draw_network(edge_dict,"simple.png",k=100)
    plt.show()
    

     
