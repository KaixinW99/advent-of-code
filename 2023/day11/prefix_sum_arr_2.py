#
# test the code: python3.10 prefix_sum_arr_2.py < input.txt
# check the time: time python3.10 prefix_sum_arr_2.py < input.txt

grid = open(0).read().splitlines()

scale = 1000000
def construct_psa(grid, scale):
    psa = [0 for _ in range(len(grid)+1)]
    for i, row in enumerate(grid):
        psa[i] = psa[i-1] + (scale if all(x=="." for x in row) else 1)
    return psa

row_psa = construct_psa(grid,scale) # row prefix sum array
col_psa = construct_psa(list(zip(*grid)),scale) # col prefix sum array

#! optimize the O(#^2) to O(#), where # is the number of galaxies
""" 0 1 2 3 4 5 6 7 8
    # . . . # # . . #
    . . . . # . . . #
    . . . . . . . . #
    (psa[5] - psa[0]) + (psa[5] - psa[4])
                      + (psa[5] - psa[4]) = 3* psa[5] - (previous sum)
""" 
def count_galaxy_in_line(grid, symbol="#"):
    rows = []
    for r, row in enumerate(grid):
        cont = row.count(symbol)
        if cont > 0:
            rows.append((r, cont))
    return rows

rows = count_galaxy_in_line(grid,"#")
cols = count_galaxy_in_line(zip(*grid),"#")

total = 0
def compute(indices, psa):
    global total
    cumulative = num_seen = 0
    for index, cont in indices:
        total += (num_seen * psa[index] - cumulative) * cont
        cumulative += psa[index] * cont
        num_seen += cont
compute(rows, row_psa)
compute(cols, col_psa)
print(total)

# problems about querying the sum of a specific range
# prefix sum array: update (linear time), query (constant time)
# range sum array : update (constant time), query (n**0.5)
# Fenwick tree:update (log n), query (log n) 
