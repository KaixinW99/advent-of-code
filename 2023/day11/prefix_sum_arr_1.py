#
# test the code: python3.10 prefix_sum_arr_1.py < input.txt
# check the time: time python3.10 prefix_sum_arr_1.py < input.txt

grid = open(0).read().splitlines()

row_psa = [0] # row prefix sum array
col_psa = [0] # col prefix sum array
scale = 2

for row in grid:
    if all(x=="." for x in row):
        row_psa.append(row_psa[-1] + scale)
    else:
        row_psa.append(row_psa[-1] + 1)

for col in zip(*grid):
    if all(x=="." for x in col):
        col_psa.append(col_psa[-1] + scale)
    else:
        col_psa.append(col_psa[-1] + 1)

galaxies = []
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "#":
            galaxies.append((r,c))


total = 0
for i, (r1, c1) in enumerate(galaxies):
    for r2, c2 in galaxies[:i]:
        total += row_psa[max(r1, r2)] - row_psa[min(r1, r2)]       
        total += col_psa[max(c1, c2)] - col_psa[min(c1, c2)]       

print(total)


# problems about querying the sum of a specific range
# prefix sum array: update (linear time), query (constant time)
# range sum array : update (constant time), query (n**0.5)
# Fenwick tree:update (log n), query (log n) 