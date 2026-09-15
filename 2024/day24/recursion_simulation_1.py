#
# test the code: python networkx_graph_interconnect_1.py < input.txt
# check the time: time python networkx_graph_interconnect_1.py < input.txt
from collections import defaultdict
from itertools import count

file = open(0)

known = defaultdict(int)

for line in file:
    if line.isspace(): break
    x, y = line.split(": ")
    known[x] = int(y)

formulas = defaultdict(tuple)

for line in file:
    x, op, y, z = line.replace(" -> ", " ").split()
    formulas[z] = (x, op, y)

operators = {
    "OR": lambda x, y: x | y,
    "AND": lambda x, y: x & y,
    "XOR": lambda x, y: x ^ y,
}

def calc(wire):
    # recursion
    if wire in known: return known[wire]
    x, op, y = formulas[wire]
    known[wire] = operators[op](calc(x), calc(y))
    return known[wire]

z = []

for i in count():
    #! rjust() method will add leading zeros to the string
    key = "z" + str(i).rjust(2, "0") 
    if key not in formulas: break
    z.append(calc(key))

print(int("".join(map(str, z[::-1])), 2))

