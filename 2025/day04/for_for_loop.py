#! /usr/bin/env python3
import sys
rolls_of_paper = [list(line) for line in sys.stdin.read().strip().splitlines() if line]
neighbor_directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

def paper_rolls_removed(rolls_of_paper):
    accessible_rolls = 0
    remove_paper_rolls = []
    for ir, roll in enumerate(rolls_of_paper):
        for ic, ch in enumerate(roll):
            if ch == '.':
                continue
            num_of_neighbor_rolls = 0
            for dr, dc in neighbor_directions:
                nr, nc = ir + dr, ic + dc
                if 0 <= nr < len(rolls_of_paper) and 0 <= nc < len(rolls_of_paper[nr]):
                    if rolls_of_paper[nr][nc] == '@':
                        num_of_neighbor_rolls += 1
            if num_of_neighbor_rolls < 4:
                accessible_rolls += 1
                remove_paper_rolls.append((ir, ic))
    return accessible_rolls, remove_paper_rolls

def plot_accessible_rolls(rows_of_paper, remove_paper_rolls):
    for ir, ic in remove_paper_rolls:
        rows_of_paper[ir][ic] = 'x'
    for row in rows_of_paper:
        print(''.join(row))
    print()

current_rolls = []
total_removed, accessible_rolls = 0, float('inf')
while accessible_rolls != 0:
    accessible_rolls, remove_paper_rolls = paper_rolls_removed(rolls_of_paper)
    total_removed += accessible_rolls
    #plot_accessible_rolls(rolls_of_paper, remove_paper_rolls)
    for ir, ic in remove_paper_rolls:
        rolls_of_paper[ir][ic] = '.'
    current_rolls = [ch for row in rolls_of_paper for ch in row]
print(total_removed)