
# test the code: python3 BB.py < test.dat
# check the time: time python3 BB.py < test.dat
from collections import deque
faces = {}
offsets = [(0,0,0.5),(0,0.5,0),(0.5,0,0),(-0.5,0,0),(0,-0.5,0),(0,0,-0.5)]
mx = my = mz = float("inf")     # outer bounding of box
Mx = My = Mz = -float("inf")    # outer bounding of box

droplet = set()

for line in open(0):
    x,y,z = cell = tuple(map(int, line.split(",")))

    droplet.add(cell)

    mx = min(mx,x)
    my = min(my,y)
    mz = min(mz,z)
    
    Mx = max(Mx, x)
    My = max(My, y)
    Mz = max(Mz, z)

    for dx,dy,dz in offsets:
        k = (x+dx,y+dy,z+dz)
        if k not in faces:
            faces[k]=0
        faces[k]+=1

# Make sure we dont accidentally start inside the droplet
# Make sure we cover all the air space around the other side
mx -= 1
my -= 1
mz -= 1

Mx += 1
My += 1
Mz += 1

queue = deque([(mx,my,mz)])
air = {(mx,my,mz)}

while queue:
    x, y, z = queue.popleft()
    for dx, dy, dz in offsets:
        nx, ny, nz = k = (x+dx*2, y+dy*2, z+dz*2)

        if not (mx<=nx<=Mx and my<=ny<=My and mz<=nz<=Mz):
            continue

        if k in droplet or k in air:
            continue
        air.add(k)
        queue.append(k)

free = set()

for x, y, z in air:
    for dx, dy, dz in offsets:
        free.add((x+dx,y+dy,z+dz))

print("Answer to Part 2:",len(set(faces) & free))