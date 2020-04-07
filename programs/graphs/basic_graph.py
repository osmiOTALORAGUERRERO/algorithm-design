import matplotlib.pyplot as plt
import networkx as nx

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=1):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def getAdjacencyGraph(self):
        adjacency = {}
        for vertex in self.getVertices():
            connected = {}
            for neighbour in self.getVertex(vertex).getConnections():
                print(neighbour)
                connected[neighbour.id] = self.getVertex(vertex).getWeight(neighbour)
            adjacency[vertex] = connected

        return adjacency

    def drawGraph(self):
        DG = nx.DiGraph()
        # dict-of-dict-of-attribute
        adj = self.getAdjacencyGraph()
        e = [(u, v, {'weight': d}) for u, nbrs in adj.items()
             for v, d in nbrs.items()]
        DG.update(edges = e, nodes=adj)
        pos=nx.spring_layout(DG)
        edge_labels = {(n1,n2): DG[n1][n2]['weight'] for (n1,n2) in DG.edges()}
        options = {
            'node_color': 'blue',
            'node_size': 500,
            'width': 2,
            'arrowstyle': '-|>',
            'arrowsize': 12
        }
        nx.draw_networkx_edge_labels(DG,pos,edge_labels=edge_labels)
        nx.draw_networkx(DG, pos, arrows=True, **options)
        plt.show()


    def __iter__(self):
        return iter(self.vertList.values())
