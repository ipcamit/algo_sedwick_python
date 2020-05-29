class BreadthFirstPaths():
    marked = None
    edgeTo = None
    distTo = None
    s = None

    def __init__(self, G, s):
        self.marked = [False for _ in range(G.getV())]
        self.edgeTo = [None for _ in range(G.getV())]
        self.distTo = [0 for _ in range(G.getV())]
        self.s = s
        self.bfs(G, s)

    def bfs(self,G,s):
        queue = [] # list can act as queue by pop(0)
        queue.append(s)
        self.marked[s]  = True
        while len(queue) != 0:
            v = queue.pop(0)
            for w in G.adj[v]:
                if not self.marked[w]:
                    queue.append(w)
                    self.distTo[w] = self.distTo[v] + 1
                    self.marked[w] = True
                    self.edgeTo[w] = v

    def hasPathTo(self,v):
        return self.marked[v]

    def pathTo(self,v):
        if (not self.hasPathTo(v)):
            return None
        else:
            path = [v]
            x = v
            while not (x == self.s):
                path.append(self.edgeTo[x])
                x = self.edgeTo[x]
            # path.append(v)
            return list(reversed(path))

if __name__ == '__main__':
    from Digraph import Digraph
    from In import In
    import sys

    in_ = In(sys.argv[1])
    G = Digraph(fileobject=in_)
    bfp = BreadthFirstPaths(G,0)
    print(bfp.edgeTo)
    print(bfp.marked)
    print(bfp.pathTo(3))
    print(bfp.distTo)
