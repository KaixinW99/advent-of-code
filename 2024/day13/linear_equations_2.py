#
# test the code: python linear_equations_2.py < input.txt
# check the time: time python linear_equations_2.py < input.txt

import re
total = 0
uplimit = 100
err = 10000000000000
for block in open(0).read().split("\n\n"):
    ax, ay, bx, by, cx, cy = map(int, re.findall(r"(\d+)", block))
    cx += err
    cy += err
    D = ax*by - ay*bx
    Dx = cx*by - cy*bx
    Dy = ax*cy - ay*cx
    if D == 0:
        if Dx == Dy == 0:
            total += min(3*cx//ax + cy//ay, 3*cx//bx + cy//by)
    else:
        if Dx % D == Dy % D == 0:
            x = Dx // D
            y = Dy // D
            if x >= 0 and y >= 0:
                total += 3*x + y

print(total)