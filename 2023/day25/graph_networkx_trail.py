import networkx as nx

def make_weakly_connected(G):
    # Create a copy of the graph so we don't modify the original
    H = G.copy()

    # Get the strongly connected components of the graph
    scc = list(nx.strongly_connected_components(G))

    # If there's more than one strongly connected component, the graph is not weakly connected
    if len(scc) > 1:
        # For each pair of strongly connected components
        for i in range(len(scc) - 1):
            # Add an edge between a node in the first component and a node in the second component
            H.add_edge(list(scc[i])[0], list(scc[i+1])[0])

    return H

#g = nx.DiGraph()
g = nx.Graph()

for line in open(0):
    left, right = line.strip().split(':')
    for node in right.strip().split():
        g.add_edge(left, node)
        g.add_edge(node, left)

#g = make_weakly_connected(g)
g.remove_edges_from(nx.minimum_edge_cut(g))
a, b = nx.connected_components(g)

print(len(a) * len(b))