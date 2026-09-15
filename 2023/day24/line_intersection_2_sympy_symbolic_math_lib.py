# it is very slow!
import sympy

hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in open(0)]

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr yr zr vxr vyr vzr", integer=True)

equations = []

for i, (sx, sy, sz, vx, vy, vz) in enumerate(hailstones, 1):
    equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
    equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
    if i < 3:
        #! 3 sets of equations are enough to solve for 6 unknowns
        continue
    answers = sympy.solve(equations, [xr, yr, zr, vxr, vyr, vzr], dict=True)
    if len(answers) == 1:
        #! make sure there is only one intersection point
        break

# extract the single answer from the list of answers
answers = answers[0]

print(answers[xr]+answers[yr]+answers[zr])