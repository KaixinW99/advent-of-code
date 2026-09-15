#
# test the code: python liberties_of_go_1.py < input.txt
# check the time: time python liberties_of_go_1.py < input.txt

from collections import deque, defaultdict

# flood fill algorithm
def flood_fill(board):
    regions = []
    seen = set()
    for r in range(len(board)):
        for c in range(len(board[0])):
            if (r, c) in seen: continue
            queue = deque([(r, c)])
            region = {(r,c)}
            seen.add((r, c))
            while queue:
                cr, cc = queue.popleft()
                for nr, nc in ((cr-1, cc), (cr+1, cc), (cr, cc-1), (cr, cc+1)):
                    if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == board[r][c] and (nr, nc) not in region:
                        region.add((nr, nc))
                        queue.append((nr, nc))
            seen |= region
            regions.append(region)
    return regions

def perimeter(region):
    output = 0
    for (r, c) in region:
        output += 4
        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if (nr, nc) in region:
                output -= 1
    return output

board = open(0).read().splitlines()
print(sum(perimeter(region)*len(region) for region in flood_fill(board)))