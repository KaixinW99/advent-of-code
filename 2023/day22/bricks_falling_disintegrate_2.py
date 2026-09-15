#
# test the code: python3.10 flood_filling_2_kaixin.py < input.txt
# check the time: time python3.10 flood_filling_2_kaixin.py < input.txt
from collections import deque

bricks = [list(map(int, line.replace("~",",").split(","))) for line in open(0)]
bricks.sort(key=lambda brick: brick[2])

def overlaps(a, b):
    # check the overlap of two rectangles from bird view
    return (max(a[0], b[0]) <= min(a[3], b[3])) and (max(a[1], b[1]) <= min(a[4], b[4]))

for index, brick in enumerate(bricks):
    max_z = 1
    for check in bricks[:index]:
        if overlaps(brick, check):
            max_z = max(max_z, check[5] + 1)
    brick[5] -= brick[2] - max_z
    brick[2] = max_z
bricks.sort(key=lambda brick: brick[2])

#* lower supports the uppers
l_supports_u = {i: set() for i in range(len(bricks))}
#* upper is supported by the lowers
u_supports_l = {i: set() for i in range(len(bricks))}

for j, upper in enumerate(bricks):
    for i, lower in enumerate(bricks[:j]):
        if overlaps(lower, upper) and upper[2] == lower[5] + 1:
            l_supports_u[i].add(j)
            u_supports_l[j].add(i)


total = 0
#! to decide weather the lower can be disintegrate
#! start from iterating the all the bricks
#! check all the upper bricks supported by the lower bricks
#! then check all the upper bricks's other supports from lower bricks
for i in range(len(bricks)):
    # load a queue of things that solely integrating
    q = deque(j for j in l_supports_u[i] if len(u_supports_l[j]) == 1)
    # variable falling is the same as seen
    falling = set(q)
    # the disintegrating brick (quite importatnt for u_supports_l[u] <= falling)
    falling.add(i) 

    while q:
        j = q.popleft()
        for u in l_supports_u[j] - falling:
            if u_supports_l[u] <= falling:
                # <= means subsets
                q.append(u)
                falling.add(u)
    
    total += len(falling) - 1 # the disintegraing brick we add to "falling" set

print(total)
