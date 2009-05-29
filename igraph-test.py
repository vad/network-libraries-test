#!/usr/bin/env python

import igraph
from time import ctime
import sys

def printInDegree(g):
    indegree = g.degree(type=igraph.IN)
    meanin = sum(indegree)*1./len(indegree)
    print "Mean IN degree: %f" %(meanin,)

def printOutDegree(g):
    outdegree = g.degree(type=igraph.OUT)
    meanout = sum(outdegree)*1./len(outdegree)
    print "Mean OUT degree: %f" %(meanout,)

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


def help(er):
    print "SYNTAX: test.py filename"
    print ""

    sys.exit(er)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help(1)

    fn = sys.argv[1]
    g = igraph.load(fn)

    print "Vertex: %d" % (len(g.vs),)
    print "Edge: %d" % (len(g.es),)

    printInDegree(g)
    printOutDegree(g)

    cl = g.clusters()

    giant = cl.giant()
    print "Length max cluster: %d" % (len(giant.vs), )

    #printAverageDistance(giant)

    #print "Average distance 2: %f" % giant.average_path_length(True, False)

    #print "Density: %f" % (g.density(),)
