
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

if __name__ == '__main__':
    from Graph import Graph
    from In import In
    import sys

    in_ = In(sys.argv[1])
    G = Graph(filobject=in_)
    dfp = DepthFirstPaths(G,0)
    print(dfp.edgeTo)
    print(dfp.marked)