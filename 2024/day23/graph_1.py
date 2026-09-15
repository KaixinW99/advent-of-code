#
# test the code: python networkx_graph_interconnect_1.py < input.txt
# check the time: time python networkx_graph_interconnect_1.py < input.txt
from collections import defaultdict

def parse_input():
    return [tuple(line.strip().split("-")) for line in open(0).read().splitlines()]

def graph(edges):
    G = defaultdict(set)
    for x, y in edges:
        G[x].add(y)
        G[y].add(x)
    return G

def triangles(graph):
    triangles_set = set()
    for x in graph:
        for y in graph[x]:
            for z in graph[y]:
                if z in graph[x] and x!=z:
                    triangles_set.add(tuple(sorted([x, y, z])))
    return triangles_set

def filter_triangles(triangles, filter_element="t"):
    return [triangle for triangle in triangles if any(node.startswith(filter_element) for node in triangle)]

def main():
    edges = parse_input()
    G = graph(edges)
    triangles_set = triangles(G)
    t_triangles = filter_triangles(triangles_set, "t")
    print(len(t_triangles))

if __name__ == "__main__":
    main()