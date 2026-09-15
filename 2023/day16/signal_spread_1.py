#
# test the code: python3.10 signal_spread_1.py < input.txt
# check the time: time python3.10 signal_spread_1.py < input.txt

from collections import deque

grid = open(0).read().splitlines()

init = (0, -1, 0, 1) # starting point; direction

seen = set()
q = deque([init])

while q:
    r, c, dr, dc = q.popleft()

    if (r, c, dr, dc) in seen:
        continue
    seen.add((r, c, dr, dc))
    
    r += dr
    c += dc
    
    if (r < 0) or (r >= len(grid)) or (c < 0) or (c >= len(grid[0])):
        continue

    ch = grid[r][c]

    if (ch == ".") or (ch == "-" and dr == 0) or (ch == "|" and dc == 0):
        q.append((r, c, dr, dc))
    elif ch == "/":
        q.append((r, c, -dc, -dr))
    elif ch == "\\":
        q.append((r, c, dc, dr))
    elif ch == "|":
        q.append((r , c, -1, 0))
        q.append((r , c,  1, 0))
    else:
        q.append((r, c, 0, -1))
        q.append((r, c, 0,  1))

coords = {(r, c) for (r, c, _, _) in seen} - {(0,-1)}

def check():
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            print(ch if ch != "." else "#" if (r, c) in coords else ".", end="")
        print()

print(len(coords))