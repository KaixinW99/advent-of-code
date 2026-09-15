f = open("input.dat","r")
lines = f.read().strip().split("\n")
blocks= set()
for line in lines:
    coords = []
    for str_coords in line.split(" -> "):
        x,y=map(int,str_coords.split(","))
        coords.append((x,y))
    
    for i in range(1,len(coords)):
        cx, cy = coords[i]      #current
        px, py = coords[i-1]    #previous

        if cy!=py:
            assert cx==px
            for y in range(min(cy,py),max(cy,py)+1):
                blocks.add((cx,y))
        if cx!=px:
            assert cy==py
            for x in range(min(cx,px),max(cx,px)+1):
                blocks.add((x,cy))

max_y = max([coord[1] for coord in blocks])

# ! Part 1:
def simulate_sand(x,y):
    global blocks
    #global max_y  # ! list is always global
    while y<=max_y:
        if (x,y+1) not in blocks:
            y+=1
            continue
        if (x-1,y+1) not in blocks:
            x-=1
            y+=1
            continue
        if (x+1,y+1) not in blocks:
            x+=1
            y+=1
            continue
        blocks.add((x,y))
        return True
    return False

ans=0
while True:
    res = simulate_sand(500,0)
    if not res:
        break
    ans+=1
print("Answer to part 1:",ans)