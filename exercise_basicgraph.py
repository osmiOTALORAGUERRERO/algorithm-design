from programs.graphs import basic_graph, adjacency_matrix, dijkstra

#Creacion del grafo
g = basic_graph.Graph()

#Asignacion de verticies
g.addEdge('c0','c1',5)
g.addEdge('c0','c5',2)
g.addEdge('c1','c2',4)
g.addEdge('c2','c3',9)
g.addEdge('c3','c4',7)
g.addEdge('c3','c5',3)
g.addEdge('c4','c0',1)
g.addEdge('c5','c4',8)
g.addEdge('c5','c2',1)


#Vista del grafo

adjacencyGraph = g.getAdjacencyGraph()  #Matriz de adyacencia

print('Matriz de adyacencia:', adjacencyGraph)

print('Conecciones')
for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))

g.drawGraph()

# dijkstra
dist, pred = dijkstra.dijkstra(adjacencyGraph, 'c0')
print('distancia: ',dist)
print('Predecesor: ', pred)
p1, p2 = dijkstra.shortest_path(adjacencyGraph, 'c5', 'c3')
print('Nodos dijkstra: ', p1)
print('Camino dijkstra: ', p2)
dijkstra.make_graph(adjacencyGraph, p2)
