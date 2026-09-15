#
# test the code: python3.10 xxx.py < input.txt
# check the time: time python3.10 xxx.py < input.txt

#! key point to get rid of the overlap function to compare the bricks
#! is that coords go through each coordinates with bricks

from collections import defaultdict

bricks = [list(map(int, line.replace("~",",").split(","))) for line in open(0)]
bricks.sort(key=lambda brick: brick[2])


coords = defaultdict(list)

def get_coords(brick):
    return [(x, y) for x in range(brick[0], brick[3] + 1) for y in range(brick[1], brick[4] + 1)]

#! map each point in the brick to the brick
#! coords dictionary is sorted due to the sorted bricks
for brick in bricks:
    for c in get_coords(brick):
        coords[c].append(brick)

#! simulate the bricks falling
for index, brick in enumerate(bricks):
    max_z = 1
    for c in get_coords(brick):
        for check in coords[c]:
            #! sorted due to the sorted bricks
            if check == brick:
                break
            max_z = max(max_z, check[5] + 1)
        brick[5] -= brick[2] - max_z
        brick[2] = max_z
bricks.sort(key=lambda brick: brick[2])

#! we no longer mutate the bricks anymore so we can hash it with type of tuple
bricks = list(map(tuple, bricks))
coords = {k: list(map(tuple, v)) for k, v in coords.items()}
ids = {brick: i for i, brick in enumerate(bricks)}

#* lower supports the uppers
l_supports_u = {i: set() for i in range(len(bricks))}
#* upper is supported by the lowers
u_supports_l = {i: set() for i in range(len(bricks))}

for upper in bricks:
    # j is the idx of upper one
    j = ids[upper]
    for c in get_coords(upper):
        for lower in coords[c]:
            if upper == lower:
                break
            # i is the idx of lower one
            i = ids[lower]
            if upper[2] == lower[5] + 1:
                l_supports_u[i].add(j)
                u_supports_l[j].add(i)


total = 0
#! to decide weather the lower can be disintegrate
#! start from iterating the all the bricks
#! check all the upper bricks supported by the lower bricks
#! then check all the upper bricks's other supports from lower bricks
for i in range(len(bricks)):
    if all(len(u_supports_l[j]) >= 2 for j in l_supports_u[i]):
        total += 1 

print(total)