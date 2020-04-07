from programs.graphs import basic_graph

g = basic_graph.Graph()
for i in range(6):
    g.addVertex(i)

print(g.vertList)

g.addEdge('c0','c1',5)
g.addEdge('c0','c5',2)
g.addEdge('c1','c2',4)
g.addEdge('c2','c3',9)
g.addEdge('c3','c4',7)
g.addEdge('c3','c5',3)
g.addEdge('c4','c0',1)
g.addEdge('c5','c4',8)
g.addEdge('c5','c2',1)

for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))
