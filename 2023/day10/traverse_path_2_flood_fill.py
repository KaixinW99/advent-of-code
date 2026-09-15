#
# test the code: python3.10 traverse_path_1.py < input.txt
# check the time: time python3.10 traverse_path_1.py < input.txt
import re

grid = open(0).read().splitlines()

U = (-1, 0)
D = (1, 0)
L = (0, -1)
R = (0, 1)

dirs = {
    "|": (U, D),
    "-": (L, R),
    "L": (U, R),
    "J": (U, L),
    "7": (D, L),
    "F": (D, R),
    ".": (),
}

s_values = set(dirs) - set(".")

ss = [(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "S"]
assert len(ss) == 1
sr, sc = ss[0]

if (sr == 0) or (D not in dirs[grid[sr-1][sc]]):
    # S value is on the top or not connect to one from top (D)
    s_values -= set("|LJ")

if (sr == len(grid) - 1) or (U not in dirs[grid[sr+1][sc]]):
    # S value is at last row or not connect to one from bottom (U)
    s_values -= set("|7F")

if (sc == 0) or (R not in dirs[grid[sr][sc-1]]):
    s_values -= set("-J7")

if (sc == len(grid[0]) - 1) or (L not in dirs[grid[sr][sc+1]]):
    s_values -= set("-LF")

assert len(s_values) == 1
[S] = s_values
#! to unpack the value in set, [*w] = {"a", "b", "c"} -> w = ["a", "b", "c"]

grid = [row.replace("S",S) for row in grid]
seen = {(sr, sc)}

pr, pc = sr, sc # keep previous and current step to avoid backtracking
dr, dc = dirs[grid[sr][sc]][0] # random choose the initial step: two directions
# here is the first step 
nr = pr + dr
nc = pc + dc

while (nr, nc) != (sr, sc):
    seen.add((nr,nc))
    for dr, dc in dirs[grid[nr][nc]]:
        if (dr + nr, nc + dc) != (pr, pc):
            pr, pc = nr, nc
            nr += dr
            nc += dc
            break

# disgard the point out of the loop
grid = ["".join(ch if (r,c) in seen else "." for c, ch in enumerate(row)) for r, row in enumerate(grid)]

ng = [] # expand the grid into 3 times in each direction for new grid

for row in grid:
    top = []
    mid = []
    bot = []
    for ch in row:
        subgrid = [[False]*3 for _ in range(3)]
        if ch != ".":
            subgrid[1][1] = True
            if U in dirs[ch]:
                subgrid[0][1] = True
            if D in dirs[ch]:
                subgrid[2][1] = True
            if L in dirs[ch]:
                subgrid[1][0] = True
            if R in dirs[ch]:
                subgrid[1][2] = True
        top += subgrid[0]
        mid += subgrid[1]
        bot += subgrid[2]
    ng += [top, mid, bot]

"""
for row in ng:
    for wall in row:
        print("#" if wall else ".", end ="")
    print()
exit(0)
"""

outside = {(0, 0)}
from collections import deque
q = deque([(0, 0)])
while q:
    r, c = q.popleft()
    for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
        if (0 <= nr < len(ng)) and (0 <= nc < len(ng[nr])) and (not ng[nr][nc]) and (nr, nc) not in outside:
            outside.add((nr,nc))
            q.append((nr,nc))
total = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if (r, c) in seen:
            continue
        if (3*r + 1, 3*c + 1) in outside:
            # ! to consider the point at the top-left cornor
            continue
        total += 1
print(total)
