#
# test the code: python3.10 find_route_1.py < input.txt
# check the time: time python3.10 find_route_1.py < input.txt
import re
steps, _, *lines = open(0).read().splitlines()
network = {}
for node in lines:
    pos, start, end = re.findall("\w+",node)
    network[pos] = [start,end]

step_count = 0
current = "AAA"

while current != "ZZZ":
    current = network[current][0 if steps[0]=="L" else 1]
    steps = steps[1:]+steps[0]
    #step = steps[step_count % len(steps)]
    #current = network[current][0 if step == "L" else 1]
    step_count += 1

print(step_count)