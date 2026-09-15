#
# test the code: python3.10 flood_filling_2_kaixin.py < input.txt
# check the time: time python3.10 flood_filling_2_kaixin.py < input.txt

#! Interpretation: the increament of the area (reachable position) follows a quadratic function
#! as the rate of growth on each direction is the same
from collections import deque

grid = open(0).read().splitlines()

sr, sc = next((r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "S")

steps = 26501365
rl = len(grid)
cl = len(grid[0])
original = steps % (2 * rl) # to have the same parity

def f(x):
    # here f(x) is the place it can explore
    # x represents the number of 2 total grids it passed
    ans = set()
    seen = {(sr, sc)}
    q = deque([(sr, sc, original + 2 * rl * x)])

    while q:
        r, c, s = q.popleft()

        if s % 2 == 0:
            # it will flip back and forth on even and odd remaining steps
            ans.add((r, c))
        if s == 0:
            continue

        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if grid[nr % rl][nc % cl] == "#" or (nr, nc) in seen:
                # python %(module operator): you will get the sign on the right side
                # Java, C++, or other languages %(remainder operator): you will get the sign on the left side
                continue
            seen.add((nr, nc))
            q.append((nr, nc, s - 1))
    return len(ans)

x = 0
values = []

while True:
    values.append(f(x))
    x += 1

    if len(values) >= 4:
        # first differences
        fd = [values[1]-values[0], values[2]-values[1], values[3]-values[2]]
        # second differences
        sd = [fd[1]-fd[0], fd[2]-fd[1]]
        if sd[0] == sd[1]:
            break
        else:
            values.pop(0)

offset = x - 4 # to change the offset to make the fitting for quadratic eqn much easier
alpha, beta, gamma, _ = values
c = alpha
a = (gamma - 2 * beta + c) / 2
b = beta - c - a

def f_sim(x):
    return int(a*x**2 + b*x + c)

print(f_sim(steps//(2*rl) - offset))
