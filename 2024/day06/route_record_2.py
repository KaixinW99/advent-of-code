#
# test the code: python route_record_1.py < input.txt
# check the time: time python route_record_1.py < input.txt

def draw(guards_map):
    for row in guards_map:
        print(''.join(row))

guards_map = [list(line.strip()) for line in open(0)]
start = [(i, j) for i in range (len(guards_map)) for j in range (len(guards_map[i])) if guards_map[i][j] == '^']
start_direction = -1+0j

def simulate_guard(guards_map, row, col, direction):
    visited = set()
    period_flag = False
    while True:
        row += int(direction.real)
        col += int(direction.imag)
        if (row, col, direction) in visited:
            period_flag = True
            break
        if row < 0 or row >= len(guards_map) or col < 0 or col >= len(guards_map[row]):
            break
        if guards_map[row][col] == '#':
            row -= int(direction.real)
            col -= int(direction.imag)
            direction *= -1j
            continue
        visited.add((row, col, direction))
    return visited, period_flag
            

visited, period_flag = simulate_guard(guards_map, start[0][0], start[0][1], start_direction)
visited.discard((start[0][0], start[0][1], start_direction))
visited_without_direction = {(row, col) for row, col, _ in visited}

num_obstruction = 0
for row, col in visited_without_direction:
    guards_map_change = [list(row) for row in guards_map]
    guards_map_change[row][col] = '#'
    _, period_flag = simulate_guard(guards_map_change, start[0][0], start[0][1], start_direction)
    if period_flag:
        num_obstruction += 1
print(num_obstruction)



        
