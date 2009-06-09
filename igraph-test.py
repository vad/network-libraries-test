#!/usr/bin/env python

import igraph
from time import ctime
from getopt import *
import sys


## GLOBAL VARIABLES

## FUNCTIONS

def meanDegree(g, type):
    degree = g.degree(type=type)
    mean = 1.*sum(degree)/len(degree)
    return mean


def degreeVariance(g, type, mean):
    '''
g:      graph
type:   type (igraph.IN or igraph.OUT)
mean:   mean degree for this type
'''
    degree = g.degree(type=type)
    variance = 1.*sum([(nodeDegree - mean)**2 for nodeDegree in degree])/len(g.vs)
    return variance


def printAverageDistance(g):
    print 'DISTANCES', ctime()
    dSum = 0
    for i in range(len(g.vs)):
        print i
        dSum += sum(g.shortest_paths_dijkstra(i, weights='weight')[0])
    #distances = giant.shortest_paths_dijkstra()

    print 'AVERAGE', ctime()
    avg_dist = 1.*dSum / (len(g.vs) * (len(g.vs)-1))
    print "Average distance: %f" % avg_dist


def usage(error = 0):
    print "SYNTAX: test.py filename"
    print ""

    sys.exit(error)


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
    g = igraph.load(fn)

    if _details:
        print "Vertex: %d" % (len(g.vs),)
        print "Edge: %d" % (len(g.es),)

    if _density:
        print "Density: %f" % (g.density(),)

        lenvs = len(g.vs)
        print "Calculated density: %f" % (1.*len(g.es)/lenvs/(lenvs-1))
        print ""

    if _degree:
        mid = meanDegree(g, igraph.IN)
        mod = meanDegree(g, igraph.OUT)

        print "Mean IN degree: %f" % mid
        print "Mean OUT degree: %f" % mod

        print "Variance IN Degree: %f" % degreeVariance(g, igraph.IN, mid)
        print "Variance OUT Degree: %f" % degreeVariance(g, igraph.OUT, mod)

    if _distance:
        cl = g.clusters()

        giant = cl.giant()
        print "Length max cluster: %d" % (len(giant.vs), )

        #printAverageDistance(giant)

        #print "Average distance 2: %f" % giant.average_path_length(True, False)


