def part1_fully_overlap():
    import re 
    f = open("input.dat","r")
    extract_number_list=[re.split(r'\W+',item,4) for item in f.read().strip("\n").split("\n")]
    f.close()
    fully_contain=0
    for x in extract_number_list:
        if int(x[0])>int(x[2]):
            if int(x[1])<=int(x[3]):
                fully_contain+=1
        elif int(x[0])<int(x[2]):
            if int(x[1])>=int(x[3]):
                fully_contain+=1
        else:
            fully_contain+=1
    print(fully_contain)
part1_fully_overlap()

def part2_general_overlap():
    import re 
    f = open("input.dat","r")
    extract_number_list=[re.split(r'\W+',item,4) for item in f.read().strip("\n").split("\n")]
    f.close()
    general_contain=0
    for x in extract_number_list:
        if int(x[0])>int(x[2]):
            if int(x[3])>=int(x[0]):
                general_contain+=1
        elif int(x[0])<int(x[2]):
            if int(x[1])>=int(x[2]):
                general_contain+=1
        else:
            general_contain+=1
    print(general_contain)   
part2_general_overlap()