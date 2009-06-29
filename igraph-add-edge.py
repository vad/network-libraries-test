#!/usr/bin/env python

import igraph as ig
from random import randint


## GLOBAL VARIABLES
n_node = 1000
n_edge = 100000

## FUNCTIONS

if __name__ == '__main__':
    g = ig.Graph(n=0)

    for i in xrange(0,n_node):
        g.add_vertices(1)

    ulim = n_node - 1
    for i in xrange(0,n_edge):
        g.add_edges((randint(0,ulim), randint(0,ulim)))

    print 'Nodes:', len(g.vs)
    print 'Edges:', len(g.es)
