#
# test the code: python3.10 find_route_2.py < input.txt
# check the time: time python3.10 find_route_2.py < input.txt
import re
import math
steps, _, *lines = open(0).read().splitlines()
network = {}
for node in lines:
    pos, start, end = re.findall("\w{3}",node)
    network[pos] = [start,end]

starts = [key for key in network if key.endswith("A")]

def loop_to(steps,start,end_criteria="Z"):
    step_count = 0
    position = start
    while (not position.endswith("Z")) or (step_count == 0):
        position = network[position][int(steps[0]=="R")]
        steps = steps[1:]+steps[0]
        step_count += 1
    return position, step_count, steps

total = 1
for start in starts:
    end_1, step_count_1, steps = loop_to(steps,start)
    
    end_2, step_count_2, _ = loop_to(steps,end_1)
    assert end_1 == end_2 # XXA ---> XXZ ---> to same XXZ
    assert step_count_1 == step_count_2 # XXA --(N steps)--> XXZ --(N steps)--> XXZ with the same steps

    #total = math.lcm(total,step_count_1)
    total = total*step_count_1 // math.gcd(total,step_count_1)
print(total)