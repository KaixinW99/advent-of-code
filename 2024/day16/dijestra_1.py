#
# test the code: python dijestra_1.py < input.txt
# check the time: time python dijestra_1.py < input.txt
import heapq

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

    priority_queue = [(0, sr, sc, 0, 1)]
    seen = {(sr, sc, 0, 1)}

    while priority_queue:
        cost, r, c, dr, dc = heapq.heappop(priority_queue)
        seen.add((r, c, dr, dc)) # prevent looping to get the cheapest cost
        if grids[r][c] == "E":
            return cost
        for new_cost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc),(cost+1000, r, c, dc, -dr), (cost+1000, r, c, -dc, dr)]:
            if grids[nr][nc] == "#": continue
            if (nr, nc, ndr, ndc) in seen: continue
            heapq.heappush(priority_queue, (new_cost, nr, nc, ndr, ndc))

def main():
    grids = parse_input()
    print(dijestra(grids))

if __name__ == "__main__":
    main()