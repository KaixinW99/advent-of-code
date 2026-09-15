from tqdm import tqdm
f = open("input.dat","r")
lines = f.read().strip().split("\n")

sensors = []
beacons = []
for line in lines:
    parts = line.split(" ")
    sx = int(parts[2][2:-1])
    sy = int(parts[3][2:-1])
    bx = int(parts[-2][2:-1])
    by = int(parts[-1][2:])
    sensors.append((sx,sy))
    beacons.append((bx,by))

N = len(sensors)
dists = []

def Manhattan_dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

for i in range(N):
    dists.append(Manhattan_dist(sensors[i],beacons[i]))

pos_k=[]
neg_k=[]

for i,s in enumerate(sensors):
    d = dists[i]
    neg_k.extend([s[0]+s[1]-d,s[0]+s[1]+d]) # extend all the values of x+y
    pos_k.extend([s[0]-s[1]-d,s[0]-s[1]+d]) # extend all the values of x-y

pos = None
neg = None

for i in range(2*N): 
    for j in range(i+1,2*N):
        a,b=pos_k[i],pos_k[j]
        if 2<=abs(a-b)<=4: # ! actually I guess that the only point created when both abs dist are 2
            pos = min(a,b)+1 # ! Here just shift the line to the middle
        a,b=neg_k[i],neg_k[j]
        if 2<=abs(a-b)<=4:
            neg = min(a,b)+1
x, y = (neg+pos)//2, (neg-pos)//2 # ! The intersection of line "x+y=neg" and "x-y=pos"
ans = x*4000000+y
print("Answer to Part 2:",ans)
# ! The Desmos page: https://www.desmos.com/calculator/my4sfl38d5 