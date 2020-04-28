from programs.graphs import basic_graph, adjacency_matrix, dijkstra, reader_graph
from files.graph import graph

graphReaded = reader_graph.readerGraph(graph.configGraph)
print(len(graphReaded))
#Creacion del grafo
g = basic_graph.Graph()

#Asignacion de verticies
for i in range(len(graphReaded)):
    for j in range(len(graphReaded[i])):
        if graphReaded[i][j] != '0' and graphReaded[i][j] != 0:
            print(graphReaded[i][j])
            if graph.configGraph['nameNodes'] != None:
                g.addEdge(graph.configGraph['nameNodes'][i], graph.configGraph['nameNodes'][j], graphReaded[i][j])
            else:
                g.addEdge('n'+str(i), 'n'+str(j), graphReaded[i][j])

#Vista del grafo

adjacencyGraph = g.getAdjacencyGraph()  #Matriz de adyacencia

print('lista de adyacencia:', adjacencyGraph)

print('Conecciones')
for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))

g.drawGraph()

# dijkstra
dist, pred = dijkstra.dijkstra(adjacencyGraph, graph.configGraph['dijkstra'][0])
print('distancia: ',dist)
print('Predecesor: ', pred)
p1, p2 = dijkstra.shortest_path(adjacencyGraph, graph.configGraph['dijkstra'][0], graph.configGraph['dijkstra'][1])
print('Nodos dijkstra: ', p1)
print('Camino dijkstra: ', p2)
dijkstra.make_graph(adjacencyGraph, p2)
