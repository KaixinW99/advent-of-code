#
# test the code: python route_search_with_one_cheat_1.py < input.txt
# check the time: time python route_search_with_one_cheat_1.py < input.txt

# Assumption: there is only a single path from the start to the end
from collections import deque

def parse_input():
    grid = [list(line.strip()) for line in open(0)]
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                break
        else:
            continue
        break
    
    return grid, len(grid), len(grid[0]), (r, c)

def bfs_advance(grid, rows, cols, start):
    sr, sc = start
    dists = [[-1] * cols for _ in range(rows)]
    dists[sr][sc] = 0
    q = deque([(sr, sc)])

    while q:
        r, c = q.popleft()
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols: continue
            if grid[nr][nc] == '#': continue
            if dists[nr][nc] != -1: continue
            dists[nr][nc] = dists[r][c] + 1
            q.append((nr, nc))
    return dists

def single_route(grid, rows, cols, start):
    r, c = start
    dists = [[-1] * cols for _ in range(rows)]
    dists[r][c] = 0

    while grid[r][c] != "E":
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols: continue
            if grid[nr][nc] == '#': continue
            if dists[nr][nc] != -1: continue
            dists[nr][nc] = dists[r][c] + 1
            r, c = nr, nc
    return dists

def cheat_once(grid, rows, cols, dists, save_points):
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#": continue
            for nr, nc in [(r, c+2), (r+1, c+1), (r+2, c),(r+1, c-1)]: # right, down right, down, down left
                # prevent repeated counting
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols: continue
                if grid[nr][nc] == "#": continue
                if abs(dists[r][c] - dists[nr][nc]) >= save_points+2: count += 1
    return count

def dispaly(dists):
    for row in dists:
        print(*row, sep="\t")

def main():
    grid, rows, cols, start = parse_input()
    dists = single_route(grid, rows, cols, start)
    #dispaly(dists)
    print(cheat_once(grid, rows, cols, dists, 100))

if __name__ == "__main__":
    main()