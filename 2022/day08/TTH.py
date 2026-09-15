import numpy as np
with open("input.dat") as f: l = len(f.readline().strip())
mat = np.genfromtxt("input.dat",dtype=int,delimiter=[1 for _ in range(l)])
lr,lc=len(mat),l
vis = 0

# ! Part 1
for i in range(lr):
    for j in range(lc):
        if (i==0) or (j==0) or (i==lr-1) or (j==lc-1):
            vis+=1
        elif mat[i,j] > min(max(mat[i,:j]),max(mat[i,j+1:]),max(mat[:i,j]),max(mat[i+1:,j])):
            vis+=1
print("Answer to part 1:",vis)

# ! Part 2
dis = []

def pos(arr,val):
    p_lst = np.where(arr>=val)[0]
    if list(p_lst):
        return p_lst[0]+1
    else:
        return 0

for i in range(1,lr-1):
    for j in range(1,lc-1):
        val = mat[i,j]
        left, right = mat[i,:j][::-1], mat[i,j+1:]
        up, down = mat[:i,j][::-1], mat[i+1:,j]
        lpos,rpos=pos(left,val) or j, pos(right,val) or lc-1-j
        upos,dpos=pos(up,val) or i, pos(down,val) or lr-1-i
        dis.append(lpos*upos*rpos*dpos)
print("Answer to part 2:",max(dis))

        