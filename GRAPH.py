class graph():
    def __init__(self,vertex):
        self.adjmatrix=[[-1]*vertex  for x in range(vertex) ]
        self.vertices={}
        self.verticeslist=[0]*vertex
        self.numvertex=vertex

    def setvertex(self,vtx,id):
        if vtx>=0 and vtx<=self.numvertex:
            self.vertices[id] = vtx
            self.verticeslist[vtx] = id


    def setedge(self,frm,to,cost=0):

        frm=self.vertices[frm]
        to=self.vertices[to]

        self.adjmatrix[frm][to]=cost
        # since it is undirected graph thus if a to b is 4then b to a is also 4
        self.adjmatrix[to][frm]=cost
    def getvertex(self):
        return self.verticeslist

    def getedges(self):
        edges=[]
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                if self.adjmatrix[i][j]!=-1:
                    edges.append((self.verticeslist[i],self.verticeslist[j],self.adjmatrix[i][j]))
        return edges
    def getmatrix(self):
        return self.adjmatrix

G =graph(6)
G.setvertex(0,'a')
G.setvertex(1,'b')
G.setvertex(2,'c')
G.setvertex(3,'d')
G.setvertex(4,'e')
G.setvertex(5,'f')
G.setedge('a','e',10)
G.setedge('a','c',20)
G.setedge('c','b',30)
G.setedge('b','e',40)
G.setedge('e','d',50)
G.setedge('f','e',60)

print(G.getvertex())
print(G.getedges())
print(G.getmatrix())

