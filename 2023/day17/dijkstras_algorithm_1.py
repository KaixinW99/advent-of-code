#
# test the code: python3.10 dijkstras_algorithm_1.py < input.txt
# check the time: time python3.10 dijkstras_algorithm_1.py < input.txt

#* Dijkstras: keep a priority Q allowing to insert elements (O(log n)) 
#*                                      and remove the smallest one (O(log n))
#* Dijkstras gives the single source shortest path 

#* Sort: O(nlog(n)); Min: O(n)
#* priority queue and heap implementation are the most efficient way

from heapq import heappush, heappop
#* Heap implementation is a data structure 
from queue import PriorityQueue
#* PQ is an abstract data type that is an interface defining properties and methods

grid = [list(map(int, line.strip())) for line in open(0)]

# heat loss, row, col, row_move, col_move, consecutive step in the same direction
pq = PriorityQueue()
pq.put((0, 0, 0, 0, 1, 0))
pq.put((0, 0, 0, 1, 0, 0))

seen = {(0, 0, 0, 1, 0): 0, (0, 0, 1, 0, 0): 0}
target = (len(grid) - 1, len(grid[0]) - 1)

while not pq.empty():
    hl, r, c, dr, dc, n = pq.get()

    if (r, c) == target:
        #* as long as we always use the cheapest way
        #* if it hits the target, the loop can be stopped
        #! the weights are non-negative.
        print(hl)
        break

    key = (r, c, dr, dc, n)
    if hl > seen[key]:
        continue

    dirs = []

    if n < 3:
        dirs.append((dr, dc))
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
                pq.put((nhl, *key))
