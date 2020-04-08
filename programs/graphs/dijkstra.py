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
