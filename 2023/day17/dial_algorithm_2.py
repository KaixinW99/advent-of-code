#
# test the code: python3.10 dijkstras_algorithm_1.py < input.txt
# check the time: time python3.10 dijkstras_algorithm_1.py < input.txt

#* Dail's algorithm: an optimiazed version of Dijkstra's algorithm for small range of weights

from collections import deque
grid = [list(map(int, line.strip())) for line in open(0)]

# heat loss, row, col, row_move, col_move, consecutive step in the same direction
buckets = deque([[(0, 0, 0, 0, 1, 0), (0, 0, 0, 1, 0, 0)], *[[] for _ in range(8)]])
#* keep 9 buckets for hl from 1 to 9 (9 kinds of weights)

seen = {(0, 0, 0, 1, 0): 0, (0, 0, 1, 0, 0): 0}
target = (len(grid) - 1, len(grid[0]) - 1)

while buckets:
    buckets.append([])
    for hl, r, c, dr, dc, n in buckets.popleft():

        if (r, c) == target and n >= 4: # before end move at least 4 blocks
            #* as long as we always use the cheapest way
            #* if it hits the target, the loop can be stopped
            #! the weights are non-negative.
            print(hl)
            exit(0)

        key = (r, c, dr, dc, n)
        if hl > seen[key]:
            continue

        dirs = []

        if n < 10:
            dirs.append((dr, dc))
        if n >= 4:    
            dirs.append((-dc, dr))
            dirs.append((dc, -dr))

        for ndr, ndc in dirs:
            nr = r + ndr
            nc = c + ndc
            if (0 <= nr < len(grid)) and (0 <= nc < len(grid[0])):
                nhl = hl + grid[nr][nc]
                key = (nr, nc, ndr, ndc, n+1 if (ndr, ndc) == (dr, dc) else 1)
                if (key not in seen) or (nhl < seen[key]):
                    seen[key] = nhl
                    buckets[grid[nr][nc]-1].append((nhl, *key))
