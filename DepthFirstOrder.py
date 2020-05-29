
class DepthFirstOrder():
    marked = None
    reversePost = None

    def __init__(self,G):
        self.marked = [False for _ in range(G.getV())]
        self.reversePost = []
        for v in range(G.getV()):
            if not self.marked[v]:
                self.dfs(G,v)


    def dfs(self, G, v):
        self.marked[v] = True
        for w in G.adj[v]:
            if(not self.marked[w]):
                self.dfs(G,w)
        self.reversePost.append(v)

    def reverseReversePost(self):
        self.reversePost.reverse()
        return self.reversePost

if __name__ == '__main__':
    from Digraph import Digraph
    from In import In
    import sys

    in_ = In(sys.argv[1])
    G = Digraph(fileobject=in_)
    dfp = DepthFirstOrder(G)
    print(dfp.reverseReversePost())