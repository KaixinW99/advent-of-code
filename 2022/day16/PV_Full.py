# 
# ! Ignore the empty valve, compress it to sub-graph, and chekc the flow rate and distances
# ! Use depth first search (dfs) with caches to brute forxe all possible paths
# ! Partition the sets of valves into every single possible split of two sets of brute force of them
# Use regular expression (flow rate= [^0]), there are only 15 with positive flow rates.
# test the code: python3 PV_part2.py < test.dat
# check the time: time python3 PV_part2.py < test.dat
from collections import deque
valves = {}
tunnels = {}
for line in open(0):
    line = line.strip()
    valve = line.split()[1]
    flow = int(line.split(";")[0].split("=")[1])
    targets = line.split("to ")[1].split(" ", 1)[1].split(", ")
    valves[valve]=flow
    tunnels[valve]=targets

dists = {}
nonempty = []

for valve in valves:
    if valve!="AA" and not valves[valve]:
        continue

    if valve!="AA":
        nonempty.append(valve)

    dists[valve]={valve:0,"AA":0}
    visited = set(valve)
    
    queue = deque([(0,valve)])

    while queue:
        distance, position = queue.popleft()
        for neighbor in tunnels[position]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            if valves[neighbor]:
                dists[valve][neighbor] = distance+1
            queue.append((distance+1,neighbor))
        
    del dists[valve][valve]
    if valve!="AA":
        del dists[valve]["AA"]

indices = {}
for index, element in enumerate(nonempty):
    indices[element]= index

cache={}

def dfs(time, valve, bitmask):
    if (time, valve, bitmask) in cache:
        return cache[(time, valve, bitmask)]
    
    maxval = 0
    for neighbor in dists[valve]:
        bit = 1 << indices[neighbor] # put zero on the right side
        if bitmask & bit:
            # 110100 & 10000 (the fourth valve)
            # 110100
            #& 10000
            #-------
            # 010000
            continue
        remtime = time -dists[valve][neighbor]-1
        if remtime<=0:
            continue
        maxval = max(maxval,dfs(remtime, neighbor, bitmask | bit)+valves[neighbor]*remtime)
    
    cache[(time,valve,bitmask)]=maxval
    return maxval

print("Answer to Part 1:",dfs(30,"AA",0))

b = (1<<len(nonempty))-1
# 1000 - 1 -> 1001 -> 1011 -> 1111 -> 111
# all valves are opened
# partition the tunnels into two ways
poss_press = []
for i in range( (b+1)//2 ): # only check half of them
    poss_press.append(dfs(26,"AA",i)+dfs(26,"AA",b^i))
print("Answer to Part 2:",max(poss_press))

