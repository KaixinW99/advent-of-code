def part1():
    f = open("input.dat","r")
    priority=0
    compare_list=[set(item[:len(item)//2])&set(item[len(item)//2:]) for item in f.read().strip("\n").split("\n")]
    f.close()
    for x in compare_list:
        for y in x:
            if ord(y)>=97:
                priority+=ord(y)-96 # ord("a")=97 -> 1
            elif ord(y)>=65:
                priority+=ord(y)-38 # ord("A")=65 -> 27
    print(priority)

def part2():
    f = open("input.dat","r")
    priority=0
    elf_list=f.read().strip("\n").split("\n")
    f.close()
    compare_list=[]
    for x in range(0,len(elf_list),3):
        it = set(elf_list[x])&set(elf_list[x+1])&set(elf_list[x+2])
        compare_list.append(it)
    
    for x in compare_list:
        for y in x:
            if ord(y)>=97:
                priority+=ord(y)-96 # ord("a")=97 -> 1
            elif ord(y)>=65:
                priority+=ord(y)-38 # ord("A")=65 -> 27
    print(priority)
part2()