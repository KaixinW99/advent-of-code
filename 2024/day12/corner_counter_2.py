#
# test the code: python corner_counter_2.py < input.txt
# check the time: time python corner_counter_2.py < input.txt

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

def corners(region):
    corner = set()
    for r, c in region:
        for cor, coc in [(r-0.5, c-0.5), (r-0.5, c+0.5), (r+0.5, c-0.5), (r+0.5, c+0.5)]:
            corner.add((cor, coc))
    
    total_corner = 0
    for cor, coc in corner:
        config = [(r, c) in region for r, c in [(cor-0.5, coc-0.5), (cor-0.5, coc+0.5), (cor+0.5, coc-0.5), (cor+0.5, coc+0.5)]]
        number = sum(config)
        if number == 1:
            total_corner += 1
        elif number == 2:
            if config[0]==config[-1]==True or config[1] == config[2] == True:
                total_corner += 2
        elif number == 3:
            total_corner += 1
    return total_corner

board = open(0).read().splitlines()
print(sum(corners(region)*len(region) for region in flood_fill(board)))