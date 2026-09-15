#
# test the code: python robot_moving_1.py < input.txt
# check the time: time python robot_moving_1.py < input.txt

import re
from functools import reduce
runs = 100
row, col = 103, 101
count_region = [0]*4
for line in open(0):
    x, y, vx, vy = map(int,re.findall(r'-?\d+', line))
    nx, ny = (x + vx * runs)%col, (y + vy * runs)%row
    if nx < col//2 and ny < row//2:
        count_region[0] += 1
    elif nx < col//2 and ny > row//2:
        count_region[1] += 1
    elif nx > col//2 and ny < row//2:
        count_region[2] += 1
    elif nx > col//2 and ny > row//2:
        count_region[3] += 1
print(reduce(lambda x,y: x*y, count_region))