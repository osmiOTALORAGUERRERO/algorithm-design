from pqdict import PQDict
import matplotlib.pyplot as plt
import networkx as nx

def dijkstra(G, start, end=None):
    inf = float('inf')
    D = {start: 0}          # mapping of nodes to their dist from start
    Q = PQDict(D)           # priority queue for tracking min shortest path
    P = {}                  # mapping of nodes to their direct predecessors
    U = set(G.keys())       # unexplored nodes

    while U:                                    # nodes yet to explore
        (v, d) = Q.popitem()                    # node w/ min dist d on frontier
        D[v] = d                                # est dijkstra greedy score
        U.remove(v)                             # remove from unexplored
        if v == end: break

        # now consider the edges from v with an unexplored head -
        # we may need to update the dist of unexplored successors
        for w in G[v]:                          # successors to v
            if w in U:                          # then w is a frontier node
                d = D[v] + G[v][w]              # dgs: dist of start -> v -> w
                if d < Q.get(w, inf):
                    Q[w] = d                    # set/update dgs
                    P[w] = v                    # set/update predecessor

    return D, P


def shortest_path(G, start, end):
    dist, pred = dijkstra(G, start, end)
    print(dist, pred, 's')
    v = end
    path = [v]
    path2 = []
    while v != start:
        path2.append((pred[v],v))
        v = pred[v]
        path.append(v)
    path.reverse()
    path2.reverse()
    return path, path2


def make_graph(G, shortPath):
    DG = nx.DiGraph()
    adj = G
    e = [(u, v, {'weight': d}) for u, nbrs in adj.items()
         for v, d in nbrs.items()]
    DG.update(edges = e, nodes=adj)
    pos=nx.spring_layout(DG)
    edge_labels = {(n1,n2): DG[n1][n2]['weight'] for (n1,n2) in DG.edges()}
    red_edges = shortPath
    edge_colors = ['black' if not edge in red_edges else 'red' for edge in DG.edges()]
    options = {
        'node_color': 'blue',
        'node_size': 500,
        'width': 2,
        'arrowstyle': '-|>',
        'arrowsize': 12,
        'edge_color' : edge_colors
    }
    nx.draw_networkx_edge_labels(DG,pos,edge_labels=edge_labels)
    nx.draw_networkx(DG, pos, arrows=True, **options)
    plt.show()
    # G = {}
    #
    # with open(filename) as file:
    #     for row in file:
    #         r = row.strip().split('\t')
    #         label = r.pop(0)
    #         neighbors = {v: int(length) for v, length in [e.split(',') for e in r]}
    #         G[label] = neighbors
    #
    # return G


if __name__ == '__main__':

    graph = {'c0': {'c1': 5, 'c5': 2},
            'c1': {'c2': 4},
            'c5': {'c4': 8, 'c2': 1},
            'c2': {'c3': 9},
            'c3': {'c4': 7, 'c5': 3},
            'c4': {'c0': 1}}

    # get shortest path distances to each node in `graph` from `a`
    dist, pred = dijkstra(graph, 'c0')
    p1, p2 = shortest_path(graph, 'c0', 'c3')
    print(p1, p2)
    print(dist)
    make_graph(graph, p2)
    # assert shortest_path(graph, 'a', 'c3') == list('abcd')
    # assert dist == {'a': 0, 'c': 3, 'b': 1, 'd': 4}     # min dist from `a`
    # assert pred == {'b': 'a', 'c': 'b', 'd': 'c'}       # direct predecessors

    graph = {'a': {'b': 14, 'c': 9, 'd': 7},
             'b': {'a': 14, 'c': 2, 'e': 9},
             'c': {'a': 9, 'b': 2, 'd': 10, 'f': 11},
             'd': {'a': 7, 'c': 10, 'f': 15},
             'e': {'b': 9, 'f': 6},
             'f': {'c': 11, 'd': 15, 'e': 6}}

    dist, pred = dijkstra(graph, start='a')
    expected = {'a': 0, 'c': 9, 'b': 11, 'e': 20, 'd': 7, 'f': 20}
    assert dist == expected
    print(dist)
    print(shortest_path(graph, 'c', 'a'))
