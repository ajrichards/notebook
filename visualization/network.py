import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx

import pandas as pd


def get_a_dict(filepath):
    df = pd.read_csv(filepath).iloc[:, 1:13]
    theme_dict = {}
    interesting_theme_idx = [3, 6, 11, 15, 16]
    theme_names = ['Horrendous IVR', 'Mobile Disengagement', "Couldn't Find it Online", "Mobile Users", "Just Show Me the Summary"]
    counter = 0
    for row_num in interesting_theme_idx:
        theme_dict[theme_names[counter]] = [df.iloc[row_num, ::2], df.iloc[row_num, 1::2]]
        counter += 1
    return theme_dict

def draw_graph(edgeWeights,plotName='network_graph.png'):
    """
    INPUT: this function takes in a dictionary of each edge names and the weight corresponding to that edge name
    """
    
    edgeDict = {"t1e1":("T1","E1"), "t1e2":("T1","E2"), "t1e6":("T1","E6"), "t2e4":("T2","E4"), "t2e5":("T2","E5"),  "t2e6":("T2","E6"), "t3e3":("T3","E3"), "t3e4":("T3","E4"), "t3e5":("T3","E5")}

    ## initialize the graph
    G = nx.Graph()
    for node in ["T1","T2","T3","E1","E2","E3","E4", "E5", "E6"]:
        G.add_node(node)

    for edgeName,edge in edgeDict.iteritems():
        G.add_edge(edge[0],edge[1],weight=edgeWeights[edgeName])

    # explicitly set positions
    pos={"T1":(2,2),
         "T2":(3.5,2),
         "T3":(5,2),
         "E1":(1,1),
         "E2":(2,1),
         "E3":(3,1),
         "E4":(4,1),
         "E5": (5, 1),
         "E6": (6, 1)}

    ## get insignificant edges
    isEdges = [(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] ==0.0]

    # plot the network
    nodeSize = 2000
    colors = [edge[2]['weight'] for edge in G.edges_iter(data=True)]
    cmap = plt.cm.winter
    fig = plt.figure(figsize=(12,6))
    fig.suptitle('Word Theme Probabilities', fontsize=14, fontweight='bold')
    ax  = fig.add_axes([0.355, 0.0, 0.7, 1.0])
    nx.draw(G,pos,node_size=nodeSize,edge_color=colors,width=4,edge_cmap=cmap,edge_vmin=-0.5,edge_vmax=0.5,ax=ax, with_labels=True)
    nx.draw_networkx_nodes(G,pos,node_size=nodeSize,nodelist=["T1","T2","T3"],node_color='#F2F2F2',with_labels=True)
    nx.draw_networkx_nodes(G,pos,node_size=nodeSize,nodelist=["E1","E2","E3","E4", "E5", "E6"],node_color='#0066FF',with_labels=True)
    nx.draw_networkx_edges(G,pos,edgelist=isEdges,width=1,edge_color='k',style='dashed')

    ## add a colormap
    ax1 = fig.add_axes([0.03, 0.05, 0.35, 0.14])
    norm = mpl.colors.Normalize(vmin=0.05, vmax=.2)
    cb1 = mpl.colorbar.ColorbarBase(ax1,cmap=cmap,
                                    norm=norm,
                                    orientation='horizontal')


    # add an axis for the legend
    ax2 = fig.add_axes([0.03,0.25,0.35,0.65]) # l,b,w,h
    ax2.set_yticks([])
    ax2.set_xticks([])
    ax2.set_frame_on(True)
    fontSize = 10
    ax2.text(0.1,0.9,r"$T1$ = Horrendous IVR" ,color='k',fontsize=fontSize,ha="left", va="center")
    ax2.text(0.1,0.8,r"$T2$ = Mobile Disengagement" ,color='k',fontsize=fontSize,ha="left", va="center")
    ax2.text(0.1,0.7,r"$T3$ = Mobile Users" ,color='k',fontsize=fontSize,ha="left", va="center")
    ax2.text(0.1,0.6,r"$E1$ = agent.transfer->ivr.exit" ,color='k',fontsize=fontSize,ha="left", va="center")
    ax2.text(0.1,0.5,r"$E2$ = agent.assigned->call.transfer" ,color='k',fontsize=fontSize,ha="left", va="center")
    ax2.text(0.1,0.4,r"$E3$ = sureswip.login->view.account.summary" ,color='k',fontsize=fontSize,ha="left", va="center")
    ax2.text(0.1,0.3,r"$E4$ = mobile.exit->mobile.entry" ,color='k',fontsize=fontSize,ha="left", va="center")
    ax2.text(0.1,0.2,r"$E5$ = mobile.exit->journey.exit" ,color='k',fontsize=fontSize,ha="left", va="center")
    ax2.text(0.1,0.1,r"$E6$ = ivr.entry->ivr.proactive.balance" ,color='k',fontsize=fontSize,ha="left", va="center")
    plt.savefig(plotName)

if __name__ == "__main__":
    filepath = '../word_transition_model/data/transitions_df.csv'
    data_dict = get_a_dict(filepath)
    summary = data_dict['Just Show Me the Summary']
    summary_events = summary[0]
    summary_scores = summary[1]

    edge_weights =  {"t1e1":0.14, "t1e2":0.13, "t1e6":0.12, "t2e4":0.05, "t2e5":0.16,  "t2e6":0.0, "t3e3":0.3, "t3e4":0.1, "t3e5":0.04}
    draw_graph(edge_weights)
