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


if __name__ == '__main__':
    try:                                
        opts, args = getopt(sys.argv[1:], "hdeir", ["help", "details", "degree", "distance", 'density']) 
    except GetoptError:
        usage(2)

    if len(args) != 1:
        usage(1)

    _details = _degree = _distance = _density = False
    for opt, arg in opts:
        if opt in ('-d', '--details'):
            _details = True
        if opt in ('-e', '--degree'):
            _degree = True
        if opt in ('-i', '--distance'):
            _distance = True
        if opt in ('-r', '--density'):
            _density = True

    fn = args[0]
    
    print ctime()
    print 'Load data'
    g = nx.read_pajek(fn, False)

    print ctime()

    if _details:
        print "Vertex: %d" % (g.number_of_nodes(),)
        print "Edge: %d" % (g.number_of_edges(),)

    if _density:
        print "Density (using networkx function): %f" % (nx.density(g),)

        lenvs = g.number_of_nodes()
        print "Calculated density: %f" % (1.*g.number_of_edges()/lenvs/(lenvs-1))
        print ""

    if _degree:
        in_degree = g.in_degree()
        out_degree = g.out_degree()
        mid = 1.*sum(in_degree) / len(g)
        mod = 1.*sum(out_degree) / len(g)

        print "Mean IN degree: %f" % mid
        print "Mean OUT degree: %f" % mod

        print "Variance IN Degree: %f" % degreeVariance(g, in_degree, mid)
        print "Variance OUT Degree: %f" % degreeVariance(g, out_degree, mod)

    if _distance:
        pass
        #cl = g.clusters()

        #giant = cl.giant()
        #print "Length max cluster: %d" % (len(giant.vs), )

        #printAverageDistance(giant)

        #print "Average distance 2: %f" % giant.average_path_length(True, False)

