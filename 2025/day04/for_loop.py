#! /usr/bin/env python3
import sys
rolls_of_paper = [list(line) for line in sys.stdin.read().strip().splitlines() if line]
neighbor_directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
accessible_rolls = 0
for ir, roll in enumerate(rolls_of_paper):
    for ic, ch in enumerate(roll):
        if ch == '.':
            continue
        num_of_neighbor_rolls = 0
        for dr, dc in neighbor_directions:
            nr, nc = ir + dr, ic + dc
            if 0 <= nr < len(rolls_of_paper) and 0 <= nc < len(rolls_of_paper[nr]):
                if rolls_of_paper[nr][nc] == '@' or rolls_of_paper[nr][nc] == 'x':
                    num_of_neighbor_rolls += 1
        if num_of_neighbor_rolls < 4:
            accessible_rolls += 1
            rolls_of_paper[ir][ic] = 'x'

def plot_accessible_rolls(rows_of_paper):
    for row in rows_of_paper:
        print(''.join(row))
    print()

print(accessible_rolls)
#plot_accessible_rolls(rolls_of_paper)