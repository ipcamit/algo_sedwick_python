from In import In
from Graph import Graph
import sys

in_ = In(sys.argv[1])
G = Graph(fileobject=in_)
for v1 in range(G.getV()):
    for v2 in G.adj[v1]:
        print("{}-{}".format(v1, v2))