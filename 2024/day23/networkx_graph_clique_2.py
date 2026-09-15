#
# test the code: python networkx_graph_interconnect_2.py < input.txt
# check the time: time python networkx_graph_interconnect_2.py < input.txt
import networkx as nx
import matplotlib.pyplot as plt

def parse_input():
    return [tuple(line.strip().split("-")) for line in open(0).read().splitlines()]

def find_largest_clique(G):
    cliques = list(nx.find_cliques(G))
    return max(cliques, key=len)

def generate_password(clique):
    return ",".join(sorted(clique))

def main():
    G = nx.Graph()
    G.add_edges_from(parse_input())

    largest_clique = find_largest_clique(G)
    password = generate_password(largest_clique)
    print(password)

    #nx.draw(G, with_labels=True)
    #plt.show()

if __name__ == "__main__":
    main()