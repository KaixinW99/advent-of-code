#
# test the code: python3.10 shorelace_formula_2.py < input.txt
# check the time: time python3.10 shorelace_formula_2.py < input.txt


xs, ys = [0], [0]
x, y = 0, 0
b = 0

for line in open(0):
    _, _, color = line.split()
    color = color[2:-1] # ex: (#70c710)
    d = "RDLU"[int(color[-1])]
    n = int(color[:-1], 16)
    b += n

    if d == "R":
        x += n
    elif d == "L":
        x -= n
    elif d == "U":
        y += n
    elif d == "D":
        y -= n
    
    xs.append(x)
    ys.append(y)

#! Shoelace's formula: A = area -> it can work for self-intersecting polygon
A = abs(sum((ys[i] + ys[i+1])*(xs[i] - xs[i+1]) for i in range(len(xs)-1))) // 2
#! Pick's theorem: b is the edges -> it cannot work on self-intersecting polygon or with holes
print(A + b//2 + 1)
