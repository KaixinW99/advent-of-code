#
# test the code: python3.10 moving_rocks_1.py < input.txt
# check the time: time python3.10 moving_rocks_1.py < input.txt

grid = open(0).read().splitlines()

total = 0

for col in zip(*grid):
    blocks = "".join(col).split("#")
    index = len(grid)
    for block in blocks:
        n = block.count("O")
        if n > 0:
            total += (index + (index-n+1))*n//2
        index -= len(block) + 1 # to avoid the occupancy of pound sign #
print(total)