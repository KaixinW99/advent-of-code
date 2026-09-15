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

def print_structure(wire, depth=0):
    if wire[0] in "xy": return "  "*depth + wire
    x, op, y = formulas[wire]
    return "  "*depth + op + " (" + wire + ")\n" + print_structure(x, depth+1) + "\n" + print_structure(y, depth+1)

#print(print_structure("z00"), "\n")
#print(print_structure("z01"), "\n")
#print(print_structure("z02"), "\n")

def make_wire(char, num):
    return char + str(num).rjust(2, "0")

def verify_z(wire, num): # "xor" for the outmost layer of zN
    #print("vz", wire, num)
    if wire not in formulas: return False
    x, op, y = formulas[wire]
    if op != "XOR": return False
    if num == 0: return sorted([x, y]) == ["x00", "y00"]
    return (verify_intermeidate_xor(x, num) and verify_carry_bit(y, num)) or (verify_intermeidate_xor(y, num) and verify_carry_bit(x, num))

def verify_intermeidate_xor(wire, num): # "xor" for second layer of zN that combined xN and yN
    #print("vi", wire, num)
    if wire not in formulas: return False
    x, op, y = formulas[wire]
    if op != "XOR": return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

def verify_carry_bit(wire, num): # "or" for another second layer of zN, except for the z01 that is "and"
    #print("vc", wire, num)
    if wire not in formulas: return False
    x, op, y = formulas[wire]
    if num == 1:
        if op != "AND": return False
        return sorted([x, y]) == ["x00", "y00"]
    if op != "OR": return False
    return (verify_direct_carry(x, num-1) and verify_recarry(y, num-1)) or (verify_direct_carry(y, num-1) and verify_recarry(x, num-1))

def verify_direct_carry(wire, num): # "and" for the third layer of zN that combined x(N-1) and y(N-1)
    #print("vd", wire, num)
    if wire not in formulas: return False
    x, op, y = formulas[wire]
    if op != "AND": return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

def verify_recarry(wire, num): # "or" for the third layer of zN and recursion wraps
    #print("vr", wire, num)
    if wire not in formulas: return False
    x, op, y = formulas[wire]
    if op != "AND": return False
    return (verify_intermeidate_xor(x, num) and verify_carry_bit(y, num)) or (verify_intermeidate_xor(y, num) and verify_carry_bit(x, num))

def verify(num):
    return verify_z(make_wire("z", num), num)

def progress():
    for i in count():
        if not verify(i): break
    return i

swaps = []
for _ in range(4):
    baseline = progress()
    for x in formulas:
        for y in formulas:
            if x == y: continue
            formulas[x], formulas[y] = formulas[y], formulas[x]
            if progress() > baseline:
                break
            formulas[x], formulas[y] = formulas[y], formulas[x]
        else:
            continue
        break
    swaps += [x, y]
print(",".join(sorted(swaps)))