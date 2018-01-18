#!/usr/bin env python

"""
http://matthiaseisen.com/articles/graphviz/

pip install graphviz

"""

import functools
import graphviz as gv


## create a very simple undirected network
g1 = gv.Graph(format='svg')
g1.node('A')
g1.node('B')
g1.edge('A', 'B')

filename = g1.render(filename='imgs/g1')
print("creating...%s"%filename)

## create a very simple directed network
g2 = gv.Digraph(format='svg')
g2.node('A')
g2.node('B')
g2.edge('A', 'B')
filename = g2.render(filename='imgs/g2')
print("creating...%s"%filename)

## use functools to create a larger graph
graph = functools.partial(gv.Graph, format='svg')
digraph = functools.partial(gv.Digraph, format='svg')

def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph

def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph


g3 = add_edges(add_nodes(digraph(), ['A', 'B', 'C']), [('A', 'B'), ('A', 'C'), ('B', 'C')])
filename = g3.render('imgs/g3')
print("creating...%s"%filename)


g4 = add_edges(add_nodes(digraph(), [('A', {'label': 'Node A'}),
                                     ('B', {'label': 'Node B'}),
                                      'C']),
               [(('A', 'B'), {'label': 'Edge 1'}),
                (('A', 'C'), {'label': 'Edge 2'}),
                ('B', 'C')
               ])

filename = g4.render('imgs/g4')
print("creating...%s"%filename)


## styling

g5 = add_edges(
    add_nodes(digraph(), [
        ('A', {'label': 'Node A'}),
        ('B', {'label': 'Node B'}),
        'C'
    ]),
    [
        (('A', 'B'), {'label': 'Edge 1'}),
        (('A', 'C'), {'label': 'Edge 2'}),
        ('B', 'C')
    ]
)

styles = {
    'graph': {
        'label': 'A Fancy Graph',
        'fontsize': '16',
        'fontcolor': 'white',
        'bgcolor': '#333333',
        'rankdir': 'BT',
    },
    'nodes': {
        'fontname': 'Helvetica',
        'shape': 'hexagon',
        'fontcolor': 'white',
        'color': 'white',
        'style': 'filled',
        'fillcolor': '#006699',
    },
    'edges': {
        'style': 'dashed',
        'color': 'white',
        'arrowhead': 'open',
        'fontname': 'Courier',
        'fontsize': '12',
        'fontcolor': 'white',
    }
}

def apply_styles(graph, styles):
    graph.graph_attr.update(
        ('graph' in styles and styles['graph']) or {}
    )
    graph.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {}
    )
    graph.edge_attr.update(
        ('edges' in styles and styles['edges']) or {}
    )
    return graph

g5 = apply_styles(g5, styles)
filename = g5.render('imgs/g5')
print("creating...%s"%filename)
