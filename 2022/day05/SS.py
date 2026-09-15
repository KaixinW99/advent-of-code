def part1():
    import re
    f = open("input.dat","r")
    pos_matrix = []
    pos_t_matrix = [] # ! this is the final matrix to move
    for _ in range(8): # get all position matrix
        pos_matrix.append([it for it in f.readline().strip("\n")][1::4]) # period is 4 without parenthesis and space
    for it in zip(*pos_matrix[::-1]):
        pos_t_matrix.append([i for i in it if i!=" "])
    for _ in range(2): f.readline() # skip two lines
    move_list = [re.split(r'\D+',item,3)[1:] for item in f.read().strip("\n").split("\n")]
    f.close()

    for m in move_list:
        for _ in range(int(m[0])):
            pop_num = pos_t_matrix[int(m[1])-1].pop(-1)
            pos_t_matrix[int(m[2])-1].append(pop_num)
    
    for x in pos_t_matrix:
        print(x[-1],end='')
    print()
part1()

def part2():
    import re
    f = open("input.dat","r")
    pos_matrix = []
    pos_t_matrix = [] # ! this is the final matrix to move
    for _ in range(8): # get all position matrix
        pos_matrix.append([it for it in f.readline().strip("\n")][1::4]) # period is 4 without parenthesis and space
    for it in zip(*pos_matrix[::-1]):
        pos_t_matrix.append([i for i in it if i!=" "])
    for _ in range(2): f.readline() # skip two lines
    move_list = [re.split(r'\D+',item,3)[1:] for item in f.read().strip("\n").split("\n")]
    f.close()

    for m in move_list:
        pop_list = pos_t_matrix[int(m[1])-1][-int(m[0]):]
        pos_t_matrix[int(m[1])-1]=pos_t_matrix[int(m[1])-1][:-int(m[0])]
        pos_t_matrix[int(m[2])-1]+=pop_list
    
    for x in pos_t_matrix:
        print(x[-1],end='')
    print()
part2()
    
