#
# test the code: python3 MMap.py < test.dat
# check the time: time python3 MMap.py < test.dat
import re

grid = []
done = False

for line in open(0):
    line = line[:-1]
    if line == "":
        done = True
    if done:
        sequence = line
    else:
        grid.append(line)

width = max(map(len, grid))
grid = [line+" "*(width-len(line)) for line in grid]        # padding the grid
numr = len(grid)
numc = len(grid[0])

r = 0
c = 0
dr = 0
dc = 1

while grid[r][c] != ".":
    c+=1

for x, y in re.findall(r"(\d+)([RL]?)",sequence):           # find "number then R/L/Null"
    x = int(x)
    for _ in range(x):
        nr = r                                              # next r
        nc = c                                              # next c
        while True:
            nr = (nr+dr)%numr
            nc = (nc+dc)%numc
            if grid[nr][nc] != " ":
                break
        if grid[nr][nc]=="#":
            break
        r = nr
        c = nc
    if y == "R":
        dr, dc = dc, -dr
    elif y == "L":
        dr, dc = -dc, dr

# mapping the direction to the faces
if dr == 0:
    if dc == 1:
        k = 0
    else:
        k = 2
else:
    if dr == 1:
        k = 1
    else:
        k = 3

print("Answer to Part 1:",1000*(r+1)+4*(c+1)+k)



