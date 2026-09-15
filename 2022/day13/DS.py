""" Part 1 """
f = open("input.dat","r")
parts = f.read().strip().split("\n\n")
f.close()

def compare(a,b):
    # ! you cannot use if elif and else, for it will skep some processes.
    if isinstance(a,list) and isinstance(b,int):
        b = [b]
    if isinstance(a,int) and isinstance(b,list):
        a = [a]
    if isinstance(a,int) and isinstance(b,int):
        if a<b:
            return 1
        elif a==b:
            return 0
        return -1
    if isinstance(a,list) and isinstance(b,list):
        i=0
        while i<len(a) and i<len(b):
            x = compare(a[i],b[i])
            if x==1:
                return 1
            elif x == -1:
                return -1
            i+=1
        if i == len(a):
            if len(a)==len(b):
                return 0
            return 1 # a ended first
        # if it didnt hit the end of a, it hit the end of b
        return -1

ans = 0
for i, block in enumerate(parts):
    #print(i)
    a, b = map(eval,block.split("\n"))
    if compare(a,b) == 1:
        ans += i+1
print("Answer to part 1:",ans)

""" Part 2 """
from functools import cmp_to_key
f = open("input.dat","r")
parts = f.read().strip().replace("\n\n","\n").split("\n")
lists = list(map(eval,parts))
lists.append([[2]])
lists.append([[6]])

def compare(a,b):
    if isinstance(a,list) and isinstance(b,int):
        b = [b]
    if isinstance(a,int) and isinstance(b,list):
        a = [a]
    if isinstance(a,int) and isinstance(b,int):
        if a<b:
            return 1
        elif a==b:
            return 0
        else:
            return -1
    if isinstance(a,list) and isinstance(b,list):
        i=0
        while i<len(a) and i<len(b):
            x = compare(a[i],b[i])
            if x==1:
                return 1
            elif x==-1:
                return -1
            i+=1
        if i == len(a):
            if len(a) == len(b):
                return 0
            else:
                return 1
        return -1

lists = sorted(lists,key=cmp_to_key(compare),reverse=True)
for index, item in enumerate(lists):
    if item == [[2]]:
        a = index+1
    elif item == [[6]]:
        b = index+1
print("Answer to part 2:",a*b)
