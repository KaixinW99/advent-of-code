#
# test the code: python route_search_with_cheats_2.py < input.txt
# check the time: time python route_search_with_cheats_2.py < input.txt

# Assumption: there is only a single path from the start to the end
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

def points(max_time):
    for radius in range(2, max_time+1):
        for dr in range(radius+1):
            dc = radius-dr
            yield {(dr, dc, radius), (dr, -dc, radius), (-dr, dc, radius), (-dr, -dc, radius)} # repetition when dr == 0 or dc == 0
    
def cheat_many_times(grid, rows, cols, dists, save_points, max_time):
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#": continue
            for changes in points(max_time):
                for dr, dc, radius in changes:
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols: continue
                    if grid[nr][nc] == "#": continue
                    if dists[r][c] - dists[nr][nc] >= save_points+radius: count += 1
    return count

def dispaly(dists):
    for row in dists:
        print(*row, sep="\t")

def main():
    grid, rows, cols, start = parse_input()
    dists = single_route(grid, rows, cols, start)
    #dispaly(dists)
    print(cheat_many_times(grid, rows, cols, dists, 100, 20))

if __name__ == "__main__":
    main()