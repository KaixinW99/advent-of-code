#
# test the code: python dijestra_backtracks_2.py < input.txt
# check the time: time python dijestra_backtracks_2.py < input.txt
import heapq
from collections import defaultdict, deque
def parse_input():
    grids = [list(line.strip()) for line in open(0)]
    return grids

def dijestra(grids):
    rows = len(grids)
    cols = len(grids[0])
    for r in range(rows):
        for c in range(cols):
            if grids[r][c] == "S":
                sr, sc = r, c
                break
        else:
            continue
        break

    priority_queue = [(0, sr, sc, 0, 1, None, None, None, None)]
    lowest_cost = defaultdict(lambda: float("inf"))
    lowest_cost[(sr, sc, 0, 1)] = 0
    backtracks = defaultdict(set)
    best_cost = float("inf") # the best cost at final point
    end_states = set()

    while priority_queue:
        cost, r, c, dr, dc, lr, lc, ldr, ldc = heapq.heappop(priority_queue)
        if cost > lowest_cost[(r, c, dr, dc)]: continue
        lowest_cost[(r, c, dr, dc)] = cost
        if grids[r][c] == "E":
            if cost > best_cost: break
            best_cost = cost
            end_states.add((r, c, dr, dc)) # record the final point with different rotations
        backtracks[(r, c, dr, dc)].add((lr, lc, ldr, ldc))
        for new_cost, nr, nc, ndr, ndc in [(cost+1, r + dr, c + dc, dr, dc),(cost+1000, r, c, dc, -dr), (cost+1000, r, c, -dc, dr)]:
            if grids[nr][nc] == "#": continue
            if cost > lowest_cost[(nr, nc, ndr, ndc)]: continue
            heapq.heappush(priority_queue, (new_cost, nr, nc, ndr, ndc, r, c, dr, dc))
    return backtracks, end_states

def flood_fill(backtracks, end_states):
    states = deque(end_states)
    seen = set(end_states)
    
    while states:
        key = states.popleft()
        for last in backtracks[key]:
            if last in seen: continue
            states.append(last)
            seen.add(last)
    return {(r,c) for r, c, _, _ in seen if (r, c)!=(None, None)}

def main():
    grids = parse_input()
    backtracks, end_states = dijestra(grids)
    print(len(flood_fill(backtracks, end_states)))

if __name__ == "__main__":
    main()