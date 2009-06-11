#!/usr/bin/env python

import networkx as nx
from time import ctime
from getopt import *
import sys

def usage(error):
    sys.exit(error)


def degreeVariance(g, degrees, mean):
    '''
g:      graph
mean:   mean degree for this type
'''
    variance = 1.*sum([(nodeDegree - mean)**2 for nodeDegree in degrees])/len(g)
    return variance



def meanVVdistance(g):
    'Mean Vertex-Vertex distance'

    giant = nx.strongly_connected_component_subgraphs(g)[0]
    mean = 0
    #spd = nx.shortest_path_length
    spd = nx.dijkstra_path_length
    nodes = giant.nodes()
    print " * max cluster #nodes: %d" % len(nodes)
    for i in range(len(nodes)):
        if i % 100 == 0:
            print "Step", i
        source = nodes[i]
        for j in range(len(nodes)):
            dest = nodes[j]
            mean += spd(g, source, dest)

    return (mean*1. / len(giant) / (len(giant)-1))


def fastMeanVVdistance(g):
    'Mean Vertex-Vertex distance using average_shortest_path_length'

    giant = nx.strongly_connected_component_subgraphs(g)[0]
    
    return nx.average_shortest_path_length(giant, weighted = True)

if __name__ == '__main__':
    try:                                
        opts, args = getopt(sys.argv[1:], "hdeirt", ["help", "details", "degree", "distance", 'density', 'transitivity']) 
    except GetoptError:
        usage(2)

    if len(args) != 1:
        usage(1)

    _details = _degree = _distance = _density = _transitivity = False
    for opt, arg in opts:
        if opt in ('-d', '--details'):
            _details = True
        if opt in ('-e', '--degree'):
            _degree = True
        if opt in ('-i', '--distance'):
            _distance = True
        if opt in ('-r', '--density'):
            _density = True
        if opt in ('-t', '--transitivity'):
            _transitivity = True

    fn = args[0]
    
    print ctime()
    print 'Load data'
    g = nx.read_pajek(fn, False)
    print ctime()
    if _transitivity: # needs DiGraph
        g = nx.DiGraph(g)

    print ctime()

    if _details:
        print " * vertex: %d" % (g.number_of_nodes(),)
        print " * edge: %d" % (g.number_of_edges(),)

    if _density:
        print " * density (using networkx function): %f" % (nx.density(g),)

        lenvs = g.number_of_nodes()
        print " * calculated density: %f" % (1.*g.number_of_edges()/lenvs/(lenvs-1))
        print ""

    if _degree:
        in_degree = g.in_degree()
        out_degree = g.out_degree()
        mid = 1.*sum(in_degree) / len(g)
        mod = 1.*sum(out_degree) / len(g)

        print " * mean IN degree: %f" % mid
        print " * mean OUT degree: %f" % mod

        print " * variance IN Degree: %f" % degreeVariance(g, in_degree, mid)
        print " * variance OUT Degree: %f" % degreeVariance(g, out_degree, mod)

    if _transitivity:
        print " * transitivity: %f" % (nx.transitivity(g), )

    if _distance:
        print " * mean VV distance (hand made): %f" % (fastMeanVVdistance(g), )
        #cl = g.clusters()

        #giant = cl.giant()
        #print "Length max cluster: %d" % (len(giant.vs), )

        #printAverageDistance(giant)

        #print "Average distance 2: %f" % giant.average_path_length(True, False)

