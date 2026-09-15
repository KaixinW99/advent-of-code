# it takes about 1 and a half minutes to run this code due to the symbolic math library!
import sympy

hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in open(0)]

total = 0 

for i, hs1 in enumerate(hailstones):
    for hs2 in hailstones[:i]:
        #! by implementing floating numbers, we dont need to use .evalf() anymore
        px, py = sympy.symbols("px py")#, float=True)
        answers = sympy.solve([vy *(px - sx) - vx * (py - sy) for sx, sy, _, vx, vy, _ in [hs1, hs2]], [px, py], dict=False)
        if not answers:
            continue
        x, y = answers[px], answers[py]
        if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
            if all( (x - sx) * vx >= 0 and (y - sy) * vy >= 0 for sx, sy, _, vx, vy, _ in [hs1, hs2] ):
                total += 1
print(total)