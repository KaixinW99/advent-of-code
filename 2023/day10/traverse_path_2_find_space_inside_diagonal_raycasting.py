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
#print("\n".join(grid))

inside = 0
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch != ".":
            continue
        cr, cc = r - 1, c - 1
        within = False
        while (cr >= 0) and (cc >= 0):
            if grid[cr][cc] in "-|FJ":
                within = not within
            cr -= 1 
            cc -= 1
        if within:
            inside += 1 
print(inside)






     
