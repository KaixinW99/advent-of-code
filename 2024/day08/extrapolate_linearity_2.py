#
# test the code: python extrapolate_linearity_1.py < input.txt
# check the time: time python extrapolate_linearity_1.py < input.txt

from collections import defaultdict
antennas_dict = defaultdict(list)
antinode_dict = defaultdict(set)
for i, line in enumerate(open(0)):
    row = line.strip()
    for j, col in enumerate(row):
        if col == '.':
            continue
        else:
            antennas_dict[col].append((i, j))
row_len, col_len = i+1, j+1

def draw_grid(antennas_dict, antinode_dict, row_len, col_len):
    for i in range(row_len):
        for j in range(col_len):
            antinode_values = [value for values in antinode_dict.values() for value in values]
            antennas_values = [value for values in antennas_dict.values() for value in values]
            if (i, j) in antinode_values:
                print('#', end='')
            elif (i, j) in antennas_values:
                for key, values in antennas_dict.items():
                    if (i, j) in values:
                        print(key, end='')
            else:
                print('.', end='')
        print() 

def antinode(x1, y1, x2, y2, row_len, col_len):
    antinode_set = {(x1, y1)}
    dx, dy = x2-x1, y2-y1
    while 0 <= x1+dx < row_len and 0 <= y1+dy < col_len:
        x1 += dx
        y1 += dy
        antinode_set.add((x1, y1))
    while 0 <= x1-dx < row_len and 0 <= y1-dy < col_len:
        x1 -= dx
        y1 -= dy
        antinode_set.add((x1, y1))
    return antinode_set

for antenna, positions in antennas_dict.items():
    pos_len = len(positions)
    for i in range(pos_len):
        for j in range(i+1, pos_len):
            x1, y1 = positions[i]
            x2, y2 = positions[j]
            for a in antinode(x1, y1, x2, y2, row_len, col_len):
                antinode_dict[antenna].add(a)

total_antinodes = set([value for values in antinode_dict.values() for value in values])
print(len(total_antinodes))
#draw_grid(antennas_dict, antinode_dict, row_len, col_len)