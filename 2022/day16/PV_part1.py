from collections import deque
with open("input.dat","r") as f: lines=f.read().strip().split("\n")
graph = {}
flows = {}
for line in lines:
    tokens = [part.strip(",;") for part in line.split(" ")]
    valve = tokens[1]
    neighbors = tuple(tokens[9:])
    graph[valve]=neighbors
    flows[valve]=int(tokens[4][5:])

# Breadth-first searching
# min opened curr pres
def find_max_pressure(graph,flows,start="AA",tot_time=30):
    queue = deque([(0,start,(),0)])
    v = set()
    poss_press = set()
    while queue:
        time, curr, path, press = queue.popleft()
        if time==tot_time:
            poss_press.add((press,path))
            continue
        if (curr,path) in v:
            continue
        v.add((curr,path))

        for i in path:
            press+=flows[i]
        
        if flows[curr]!=0:
            if curr not in path:
                queue.append((time+1,curr,tuple(list(path)+[curr]),press))
        
        for i in graph[curr]:
            queue.append((time+1,i,path,press))
    return poss_press
print("Answer to part 1:",max(find_max_pressure(graph,flows),key=lambda x:x[0]))

