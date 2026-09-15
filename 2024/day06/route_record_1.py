#
# test the code: python route_record_1.py < input.txt
# check the time: time python route_record_1.py < input.txt

def draw(guards_map):
    for row in guards_map:
        print(''.join(row))

guards_map = [list(line.strip()) for line in open(0)]
row, col = [(i, j) for i in range (len(guards_map)) for j in range (len(guards_map[i])) if guards_map[i][j] == '^'][0]
guards_map[row][col] = "X"
direction = -1+0j
visited = set()

while True:
    row += int(direction.real)
    col += int(direction.imag)
    if row < 0 or row >= len(guards_map) or col < 0 or col >= len(guards_map[row]):
        break
    if guards_map[row][col] == '#':
        row -= int(direction.real)
        col -= int(direction.imag)
        direction *= -1j
        continue
    guards_map[row][col] = "X"
    visited.add((row, col))

print(sum(row.count("X") for row in guards_map))
#print(visited)
draw(guards_map)
        
