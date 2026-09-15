import networkx as nx

#https://networkx.org/documentation/stable/reference/classes/index.html
g = nx.Graph()
# Graph is undirected and DiGraph is directed

for line in open(0):
    left, right = line.strip().split(':')
    for node in right.strip().split():
        g.add_edge(left, node)

assert nx.is_connected(g)
assert len(nx.minimum_edge_cut(g)) == 3

#https://networkx.org/documentation/stable/reference/algorithms/connectivity.html
g.remove_edges_from(nx.minimum_edge_cut(g))
#https://networkx.org/documentation/stable/reference/algorithms/component.html
a, b = nx.connected_components(g)

print(len(a) * len(b))