#
# test the code: python3.10 networkx_1.py < input.txt
# check the time: time python3.10 networkx_1.py < input.txt

import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

for line in open("input.txt"):
    l, r = line.split(" -> ")
    for t in r.split(", "):
        g.add_edge(l[1:], t)

nx.draw(g)
plt.show()