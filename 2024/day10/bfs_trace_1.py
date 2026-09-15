#
# test the code: python bfs_trace_1.py < input.txt
# check the time: time python bfs_trace_1.py < input.txt
from collections import deque

def parse_map(input_data):
    return [list(map(int, line.strip())) for line in input_data.splitlines()]

def find_trailheads(topographic_map):
    trailheads = []
    for r in range(len(topographic_map)):
        for c in range(len(topographic_map[0])):
            if topographic_map[r][c] == 0:
                trailheads.append((r, c))
    return trailheads

def bfs(topographic_map, start):
    rows, cols = len(topographic_map), len(topographic_map[0])
    queue = deque([start])
    visited = set([start])
    reachable_nines = set()
    
    while queue:
        r, c = queue.popleft()
        current_height = topographic_map[r][c]
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                next_height = topographic_map[nr][nc]
                if next_height == current_height + 1:
                    if next_height == 9:
                        reachable_nines.add((nr, nc))
                    queue.append((nr, nc))
                    visited.add((nr, nc)) 
    return len(reachable_nines)

def main(input_data):
    topographic_map = parse_map(input_data)
    trailheads = find_trailheads(topographic_map)
    
    total_score = 0
    for trailhead in trailheads:
        score = bfs(topographic_map, trailhead)
        total_score += score
    
    print(total_score)

if __name__ == "__main__":
    main(open(0).read())

