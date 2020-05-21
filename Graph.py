from In import In
class Graph():
    V = 0
    E = 0
    adj = None
    filobject = None
    def __init__(self,V=0,filobject = None):
        if V!=0 :
            pass
        elif(isinstance(filobject,In)):
            self.filobject = filobject
            self.V = self.filobject.readInt()
            self.E = self.filobject.readInt()
            self.adj = [[] for _ in range(self.V)]
            for _ in range(self.V):
                v= self.filobject.readInt()
                w= self.filobject.readInt()
                self.addEdge(v,w)
        else:
            raise Exception("Improper Graph Init")
            exit()

    def addEdge(self,v,w):
        self.E+=1
        self.adj[v].append(w)
        self.adj[w].append(v)

    def getV(self):
        return self.V

    def getE(self):
        return self.E

    def toString(self):
        pass

