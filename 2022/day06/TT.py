def part1and2(distinct):
    f = open("input.dat","r")
    signal=f.readline()
    for i in range(len(signal)):
        char_set=set()
        for j in range(i,i+distinct):
            char_set.add(signal[j])
        if len(char_set)==distinct:
            return j+1     
print(part1and2(4))
print(part1and2(14))