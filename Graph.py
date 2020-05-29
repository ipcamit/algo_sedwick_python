from In import In
class Graph():
    V = 0
    E = 0
    adj = None
    fileobject = None
    def __init__(self,V=0,fileobject = None):
        if V!=0 :
            pass
        elif(isinstance(fileobject,In)):
            self.fileobject = fileobject
            self.V = self.fileobject.readInt()
            self.E = self.fileobject.readInt()
            self.adj = [[] for _ in range(self.V)]
            # instead of bags or linked lists or sets, adj is simple list of lists
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
        self.adj[w].append(v)

    def getV(self):
        return self.V

    def getE(self):
        return self.E

    def toString(self):
        pass

 # #######################################################################
 # Graph processing API
 # #######################################################################
def degree(G,v):
    degree = 0
    for node in G.adj[v]:
        degree+=1
    return degree

def maxDegree(G):
    maxDegree = 0
    for v in range(G.getV()):
        degree = degree(G, v)
        if degree > maxDegree:
            maxDegree = degree
    return maxDegree

def averageDegree(G):
    return 2.0*G.getE()/G.getV()

def numberOfSelfLoops(G):
    count = 0
    for v in range(G.getV()):
        for w in G.adj[v]:
            if v==w:
                count+=1
    return count/2
