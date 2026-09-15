#
# test the code: python3.10 moving_rocks_2.py < input.txt
# check the time: time python3.10 moving_rocks_2.py < input.txt

grid = tuple(open(0).read().splitlines())

def cycle():
    global grid
    for _ in range(4):
        grid = tuple(zip(*grid)) #transpose the grid
        grid = ("#".join(("".join(sorted(block, reverse=True)) for block in "".join(row).split("#"))) for row in grid)
        grid = tuple([row[::-1] for row in grid])
        # to make it rotate clockwise

states = []
seen = set()
index = 0

# the tuple in python is already HASH, not need to use hash function (treat str into num)
while grid not in seen:
    states.append(grid)
    seen.add(grid)
    cycle()
    index += 1

offset = states.index(grid)
cycle_length = index - offset
grid = states[(1_000_000_000 - offset)%cycle_length+offset]

L = len(grid)
print(sum(row.count("O")*(L-r) for r, row in enumerate(grid)))