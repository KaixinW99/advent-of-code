f = open("input.dat","r")
each_sum = 0
list_sum = []
for line in f:
    if line=="\n":
        list_sum.append(each_sum)
        each_sum = 0
    else:
        each_sum += eval(line[:-1])
f.close()
# ! Part 1
print(max(list_sum))
# ! Part 2
print(sum(sorted(list_sum)[-3:]))