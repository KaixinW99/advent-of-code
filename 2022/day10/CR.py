with open("input.dat") as f: commands = [command.strip() for command in f.readlines()]
# ! Part 1
stp = 1
val = 1
X = {stp:val}
for command in commands:
    if command=="noop":
        stp+=1
        X.update({stp:val})
    else:
        stp+=2
        val+=int(command[5:])
        X.update({stp:val})
total = 0
for c_point in range(20,221,40):
    c_val = X.get(c_point,None)
    if c_val:
        total+=c_point*c_val
    else:
        total+=c_point*X[c_point-1]
print("Answer to Part 1:",total)

# ! Part 2
stp = 1
val = 1
X = {stp:range(val-1,val+2)}

# handle the command
for command in commands:
    if command=="noop":
        stp+=1
        X.update({stp:range(val-1,val+2)})
    else:
        stp+=2
        val+=int(command[5:])
        X.update({stp:range(val-1,val+2)})

# make up for all of the timestep
for i in range(1,max(X.keys())):
    if not X.get(i,None):
        X.update({i:X[i-1]})
#X = dict(sorted(X.items(),key=lambda a: a[0]))

lr, lc= 6, 40
print("Answer to part 2:")
for i in range(1,lr+1):
    for j in range(1,lc+1):
        pos = int((i-1)*lc+j)
        if j-1 in X[pos]:
            print("#",end="")
        else:
            print(".",end="")
    print()

