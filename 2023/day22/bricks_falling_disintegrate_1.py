#
# test the code: python3.10 flood_filling_2_kaixin.py < input.txt
# check the time: time python3.10 flood_filling_2_kaixin.py < input.txt

bricks = [list(map(int, line.replace("~",",").split(","))) for line in open(0)]
bricks.sort(key=lambda brick: brick[2])

def overlaps(a, b):
    # check the overlap of two rectangles from bird view
    return (max(a[0], b[0]) <= min(a[3], b[3])) and (max(a[1], b[1]) <= min(a[4], b[4]))

#! simulate the bricks falling
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
    if all(len(u_supports_l[j]) >= 2 for j in l_supports_u[i]):
        total += 1 

print(total)