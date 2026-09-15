#
# test the code: python extrapolate_linearity_1.py < input.txt
# check the time: time python extrapolate_linearity_1.py < input.txt

from collections import defaultdict
antennas_dict = defaultdict(list)
antinode_dict = defaultdict(list)
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

def antinode(x1, y1, x2, y2):
    return (x2+x2-x1, y2+y2-y1), (x1+x1-x2, y1+y1-y2)
for antenna, positions in antennas_dict.items():
    pos_len = len(positions)
    for i in range(pos_len):
        for j in range(i+1, pos_len):
            x1, y1 = positions[i]
            x2, y2 = positions[j]
            a, b = antinode(x1, y1, x2, y2)
            if 0 <= a[0] < row_len and 0 <= a[1] < col_len:
                antinode_dict[antenna].append(a)
            if 0 <= b[0] < row_len and 0 <= b[1] < col_len:
                antinode_dict[antenna].append(b)

total_antinodes = set([value for values in antinode_dict.values() for value in values])
print(len(total_antinodes))
#draw_grid(antennas_dict, antinode_dict, row_len, col_len)