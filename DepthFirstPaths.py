
class DepthFirstPaths():
    marked = None
    edgeTo = None
    s = None

    def __init__(self,G,s):
        self.marked = [False for _ in range(G.getV())]
        self.edgeTo = [None for _ in range(G.getV())]
        self.s = s
        self.dfs(G, s)

    def dfs(self, G, s):
        self.marked[s] = True
        for w in G.adj[s]:
            if(not self.marked[w]):
                self.dfs(G,w)
                self.edgeTo[w] = s

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
    dfp = DepthFirstPaths(G,0)
    print(dfp.edgeTo)
    print(dfp.marked)
    print(dfp.pathTo(3))