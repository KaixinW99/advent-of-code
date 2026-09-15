def part1():
    f = open("input.dat","r")
    score=0
    score_dict={"X":1,"Y":2,"Z":3}
    lose_dict={"X":"B","Y":"C","Z":"A"}
    win_dict={"X":"C","Y":"A","Z":"B"}
    for line in f:
        if line=="\n":
            continue
        each_run=line.strip("\n").split(" ")
        score+=score_dict[each_run[1]]
        if win_dict[each_run[1]]==each_run[0]:
            score+=6
        elif lose_dict[each_run[1]]==each_run[0]:
            continue
        else:
            score+=3
    f.close()
    print(score)
part1()

def part2():
    f = open("input.dat","r")
    score=0
    score_dict={"A":1,"B":2,"C":3}
    win_dict={"B":"C","C":"A","A":"B"}
    lose_dict={"A":"C","B":"A","C":"B"}
    for line in f:
        if line=="\n":
            continue
        each_run=line.strip("\n").split(" ")
        if each_run[1]=="X":
            score+=score_dict[lose_dict[each_run[0]]]
        elif each_run[1]=="Y":
            score+=3+score_dict[each_run[0]]
        else:
            score+=6+score_dict[win_dict[each_run[0]]]
    f.close()
    print(score)
part2()