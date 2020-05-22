
class CC():
    marked = None
    id_ = None
    count = None

    def __init__(self,G):
        self.marked = [False for _ in range(G.getV())]
        self.id_ = [-10 for _ in range(G.getV())]
        self.count = 0

        for v in range(G.getV()):
            if not self.marked[v]:
                self.dfs(G,v)
                self.count += 1

    def getCount(self):
        return self.count

    def getId(self,v):
        return self.id_[v]

    def dfs(self,G,v):
        self.marked[v] = True
        self.id_[v] = self.count
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G,w)

if __name__ == '__main__':
    from Graph import Graph
    from In import In
    import sys

    in_ = In(sys.argv[1])
    G = Graph(filobject=in_)
    cc = CC(G)
    print(cc.id_)
    print(cc.marked)