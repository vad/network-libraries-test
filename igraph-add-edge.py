#!/usr/bin/env python

import igraph as ig
from random import randint


## GLOBAL VARIABLES
n_node = 1000
n_edge = 100000

## FUNCTIONS

if __name__ == '__main__':
    g = ig.Graph(n=0)

    for i in xrange(1,n_node+1):
        g.add_vertices(1)
    print len(g.vs)

    for i in xrange(1,n_edge):
        g.add_edges((randint(1,n_node-1), randint(1,n_node-1)))

    print len(g.vs)
