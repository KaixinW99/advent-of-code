#
# test the code: python3.10 signal_spread_2.py < input.txt
# check the time: time python3.10 signal_spread_2.py < input.txt

from collections import deque

grid = open(0).read().splitlines()

def calc(r, c, dr, dc):
    init = (r, c, dr, dc) # starting point; direction

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

    coords = {(r, c) for (r, c, _, _) in seen}
    return len(coords) - 1

max_val = 0
for r in range(len(grid)):
    max_val = max(max_val, calc(r, -1, 0, 1))
    max_val = max(max_val, calc(r, len(grid[0]), 0, -1))
for c in range(len(grid[0])):
    max_val = max(max_val, calc(-1, c, 1, 0))
    max_val = max(max_val, calc(len(grid), c, -1, 0))
print(max_val)