#
# test the code: python networkx_graph_interconnect_1.py < input.txt
# check the time: time python networkx_graph_interconnect_1.py < input.txt
import networkx as nx
import matplotlib.pyplot as plt

def parse_input():
    return [tuple(line.strip().split("-")) for line in open(0).read().splitlines()]

def find_triangles(G):
    triangles = set()
    for node in G.nodes():
        neighbors = set(G.neighbors(node))
        for neighbor in neighbors:
            common_neighbors = neighbors.intersection(set(G.neighbors(neighbor)))
            for common_neighbor in common_neighbors:
                triangles.add(tuple(sorted([node, neighbor, common_neighbor])))
    return triangles

def filter_triangles(triangles, filter_element="t"):
    return [triangle for triangle in triangles if any(node.startswith('t') for node in triangle)]

def main():
    G = nx.Graph()
    G.add_edges_from(parse_input())
    
    triangles = find_triangles(G)
    filtered_triangles = filter_triangles(triangles)

    #print(filtered_triangles)
    print(len(filtered_triangles))

    nx.draw(G, with_labels=True)
    plt.show()

if __name__ == "__main__":
    main()