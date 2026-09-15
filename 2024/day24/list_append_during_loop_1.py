#
# test the code: python networkx_graph_interconnect_1.py < input.txt
# check the time: time python networkx_graph_interconnect_1.py < input.txt
from collections import defaultdict

a, b = open(0).read().split("\n\n")
input_dict = defaultdict(int)
for line in a.splitlines():
    key, value = line.split(": ")
    input_dict[key] = int(value)
b = b.splitlines()
    
def eval_exprs(exprs):
    for expr in exprs:
        operation, key = expr.split(" -> ")
        a, b = operation[:3], operation[-3:]
        if a not in input_dict or b not in input_dict:
            exprs.append(operation + " -> " + key)
            continue
        if "XOR" in operation:
            input_dict[key] = input_dict[a]^input_dict[b]
        elif "OR" in operation:
            input_dict[key] = input_dict[a]|input_dict[b]
        elif "AND" in operation:
            input_dict[key] = input_dict[a]&input_dict[b]
        else: raise ValueError("Invalid operation")

eval_exprs(b)
#print(*sorted(input_dict.items(), key=lambda x: x[0]), sep="\n")

final_num = 0
for key, item in input_dict.items():
    if "z" in key and item == 1:
        final_num += 2**int(key[1:])
print(final_num)
