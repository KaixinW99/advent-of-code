#
# test the code: python linear_equations_brute_force_1.py < input.txt
# check the time: time python linear_equations_brute_force_1.py < input.txt

import re
total = 0
uplimit = 100
for block in open(0).read().split("\n\n"):
    ax, ay, bx, by, cx, cy = map(int, re.findall(r"(\d+)", block))
    min_score = float('inf')
    for i in range(uplimit+1):
        for j in range(uplimit+1):
            if ax*i + bx*j == cx and ay*i + by*j == cy:
                min_score = min(min_score, 3*i+j)
    if min_score != float('inf'):
        total += min_score
print(total)