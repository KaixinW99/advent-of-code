#
# test the code: python3 GPS.py < test.dat
# check the time: time python3 GPS.py < test.dat
class Node:
    def __init__(self,n) -> None:
        self.n = n
        self.left = None
        self.right = None

x = [Node(int(x)) for x in open(0)]
l = len(x)

for i in range(l):
    x[i].right = x[(i+1)%l]
    x[i].left = x[(i-1)%l]

m = l-1

for k in x:                             # k is the current node
    if k.n == 0:                        # find the node of 0
        z = k                           # z is the node of 0
        continue
    p = k                               # p is the node we are targeting
    if k.n > 0:
        for _ in range((k.n)%m):        # circular
            p = p.right
        if k==p:
            continue
        k.right.left = k.left
        k.left.right = k.right
        p.right.left = k
        k.right = p.right
        p.right = k
        k.left = p
    else:
        for _ in range((-k.n)%m):       # circular
            p = p.left
        if k==p:
            continue
        k.left.right = k.right
        k.right.left = k.left
        p.left.right = k
        k.left = p.left
        p.left = k
        k.right = p

t = 0
for _ in range(3):
    for _ in range(1000):
        z = z.right
    t += z.n

print("Anwswer to Part 1:", t)
