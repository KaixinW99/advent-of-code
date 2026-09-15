
# ! Part 1
def bi_knots():
    with open("input.dat") as f: commands=[line.strip() for line in f.readlines()]
    import numpy as np
    mat = np.zeros([500,500],dtype=int)
    Hr=Hc=Tr=Tc=250
    mat[Tr,Tc]+=1

    for command in commands:
        direction = command[0]
        for stp in range(int(command[2:])):
            # H moves
            if direction == "U":
                Hr-=1
            elif direction == "D":
                Hr+=1
            elif direction == "R":
                Hc+=1
            else:
                Hc-=1
            
            # T moves
            if Tr==Hr:
                if Hc-Tc==2:
                    Tc+=1
                    mat[Tr,Tc]+=1
                elif Tc-Hc==2:
                    Tc-=1
                    mat[Tr,Tc]+=1
            
            elif Tc==Hc:
                if Hr-Tr==2:
                    Tr+=1
                    mat[Tr,Tc]+=1
                elif Tr-Hr==2:
                    Tr-=1
                    mat[Tr,Tc]+=1
            
            else:
                if (Tc-Hc==2 and Tr-Hr==1) or (Tr-Hr==2 and Tc-Hc==1):
                    Tr-=1
                    Tc-=1
                    mat[Tr,Tc]+=1
                elif (Tc-Hc==2 and Tr-Hr==-1) or (Tr-Hr==-2 and Tc-Hc==1):
                    Tr+=1
                    Tc-=1
                    mat[Tr,Tc]+=1
                elif (Tc-Hc==-2 and Tr-Hr==1) or (Tr-Hr==2 and Tc-Hc==-1):
                    Tr-=1
                    Tc+=1
                    mat[Tr,Tc]+=1
                elif (Tc-Hc==-2 and Tr-Hr==-1) or (Tr-Hr==-2 and Tc-Hc==-1):    
                    Tr+=1
                    Tc+=1
                    mat[Tr,Tc]+=1
    print("Answer to part 1:",len(np.nonzero(mat.reshape(-1))[0]))
bi_knots()

# ! Part 2
with open("input.dat") as f: commands=[line.strip() for line in f.readlines()]
import numpy as np
def tail_moves(Hr,Hc,Tr,Tc):     
    # T moves
    if Tr==Hr:
        if Hc-Tc==2:
            Tc+=1
        elif Tc-Hc==2:
            Tc-=1
    
    elif Tc==Hc:
        if Hr-Tr==2:
            Tr+=1
        elif Tr-Hr==2:
            Tr-=1

    elif (Tc-Hc==2 and Tr-Hr==1) or (Tr-Hr==2 and Tc-Hc==1):
        Tr-=1
        Tc-=1
    elif (Tc-Hc==2 and Tr-Hr==-1) or (Tr-Hr==-2 and Tc-Hc==1):
        Tr+=1
        Tc-=1
    elif (Tc-Hc==-2 and Tr-Hr==1) or (Tr-Hr==2 and Tc-Hc==-1):
        Tr-=1
        Tc+=1
    elif (Tc-Hc==-2 and Tr-Hr==-1) or (Tr-Hr==-2 and Tc-Hc==-1):    
        Tr+=1
        Tc+=1
    
    elif (Tc-Hc==2 and Tr-Hr==2):
        Tr-=1
        Tc-=1
    elif (Tc-Hc==-2 and Tr-Hr==2):
        Tr-=1
        Tc+=1
    elif (Tc-Hc==2 and Tr-Hr==-2):
        Tr+=1
        Tc-=1
    elif (Tc-Hc==-2 and Tr-Hr==-2):
        Tr+=1
        Tc+=1
    return Tr,Tc

def multiple_knots(num,commands):
    mat = np.zeros([500,500],dtype=int)
    Hr=Hc=250
    mat[Hr,Hc]+=1
    tails = [[Hr,Hc] for _ in range(num)]
    for command in commands:
        direction = command[0]
        for stp in range(int(command[2:])):
            # H moves
            if direction == "U":
                Hr-=1
            elif direction == "D":
                Hr+=1
            elif direction == "R":
                Hc+=1
            else:
                Hc-=1
            
            tails[0][0],tails[0][1]=Hr,Hc
            for t_index in range(1,len(tails)):
                tails[t_index][0],tails[t_index][1]=tail_moves(*tails[t_index-1],*tails[t_index])
            #print(tails)
            mat[tails[-1][0],tails[-1][1]]+=1
    print("Answer to part 2:",len(np.nonzero(mat.reshape(-1))[0]))
multiple_knots(10,commands)
        

            

