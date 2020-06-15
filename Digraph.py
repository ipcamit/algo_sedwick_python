from In import In

class Digraph():
    V=0
    E=0
    adj=None
    fileobject=None
    def __init__(self,V=0,fileobject=None):
        if V!= 0:
            pass
        elif(isinstance(fileobject,In)):
            self.fileobject = fileobject
            self.V = self.fileobject.readInt()
            self.E = self.fileobject.readInt()
            self.adj = [[] for _ in range(self.V)]
            for _ in range(self.E):
                v= self.fileobject.readInt()
                w= self.fileobject.readInt()
                self.addEdge(v,w)
        else:
            raise Exception("Improper Graph Init")
            exit()

    def addEdge(self,v,w):
        self.E+=1
        #  instead of adding to bag, append to list 
        self.adj[v].append(w)

    def getV(self):
        return self.V

    def getE(self):
        return self.E

    def toString(self):
        pass

    def reverse(self):
        temp_adj = [[] for _ in range(self.V)]
        for w in range(G.getV()):
            if 

if __name__ == '__main__':
    from In import In
    import sys

    file = sys.argv[1]
    in_ = In(file)
    D = Digraph(fileobject=in_)
    for v in range(D.getV()):
        for w in D.adj[v]:
            print("{}->{}".format(v,w))