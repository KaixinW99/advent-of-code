from tqdm import tqdm
f = open("input.dat","r")
lines = f.read().strip().split("\n")

sensors = []
beacons = []
for line in lines:
    parts = line.split(" ")
    sx = int(parts[2][2:-1])
    sy = int(parts[3][2:-1])
    bx = int(parts[-2][2:-1])
    by = int(parts[-1][2:])
    sensors.append((sx,sy))
    beacons.append((bx,by))

N = len(sensors)
dists = []

def Manhattan_dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

for i in range(N):
    dists.append(Manhattan_dist(sensors[i],beacons[i]))

Y = 2000000
intervals = []
for i, s in enumerate(sensors):
    dx = dists[i] - abs(s[1]-Y)
    if dx <= 0:
        # there isnt the intersection
        continue
    intervals.append(range(s[0]-dx,s[0]+dx+1))

# The only beacons in the forbidden range
allowed_x = set()
for bx, by in beacons:
    if by == Y:
        allowed_x.add(bx)

from itertools import chain
from functools import reduce
tot_intervals = set(reduce(chain,intervals)) # union the range()
for x in allowed_x:
    tot_intervals.remove(x)
print("Answer to Part 1:",len(tot_intervals))