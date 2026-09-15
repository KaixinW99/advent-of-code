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


def main():
    edges = parse_input()
    G = graph(edges)

    cliques_set = set()
    def search(node, clique):
        req = tuple(sorted(clique))
        if req in cliques_set: return
        cliques_set.add(req)

        for neighbor in G[node]:
            if neighbor in clique: continue
            if not all(neighbor in G[q] for q in clique): continue
            search(neighbor, {*clique, neighbor})

    for node in G:
        search(node, {node})
        
    print(",".join(max(cliques_set, key=len)))


if __name__ == "__main__":
    main()