m0 = [92, 73, 86, 83, 65, 51, 55, 93]
m1 = [99, 67, 62, 61, 59, 98]
m2 = [81, 89, 56, 61, 99]
m3 = [97, 74, 68]
m4 = [78, 73]
m5 = [50]
m6 = [95, 88, 53, 75]
m7 = [50, 77, 98, 85, 94, 56, 89]
c0 = c1 = c2 = c3 = c4 = c5 = c6 = c7 = 0
def Monkey0():
    global m0
    global m3
    global m4
    global c0
    m = m0[:]
    for item in m:
        c0+=1
        worry=(item*5)//3
        if worry%11==0:
            m3.append(worry)
        else:
            m4.append(worry)
        m0=m0[1:]
def Monkey1():
    global m1
    global m6
    global m7
    global c1
    m = m1[:]
    for item in m:
        c1+=1
        worry=(item*item)//3
        if worry%2==0:
            m6.append(worry)
        else:
            m7.append(worry)
        m1=m1[1:]
def Monkey2():
    global m2
    global m1
    global m5
    global c2
    m = m2[:]
    for item in m:
        c2+=1
        worry=(item*7)//3
        if worry%5==0:
            m1.append(worry)
        else:
            m5.append(worry)
        m2=m2[1:]     
def Monkey3():
    global m3
    global m2
    global m5
    global c3
    m = m3[:]
    for item in m:
        c3+=1
        worry=(item+1)//3
        if worry%17==0:
            m2.append(worry)
        else:
            m5.append(worry)
        m3=m3[1:]
def Monkey4():
    global m4
    global m2
    global m3
    global c4
    m = m4[:]
    for item in m:
        c4+=1
        worry=(item+3)//3
        if worry%19==0:
            m2.append(worry)
        else:
            m3.append(worry)
        m4=m4[1:]
def Monkey5():
    global m5
    global m1
    global m6
    global c5
    m = m5[:]
    for item in m:
        c5+=1
        worry=(item+5)//3
        if worry%7==0:
            m1.append(worry)
        else:
            m6.append(worry)
        m5=m5[1:]  
def Monkey6():
    global m6
    global m0
    global m7
    global c6
    m = m6[:]
    for item in m:
        c6+=1
        worry=(item+8)//3
        if worry%3==0:
            m0.append(worry)
        else:
            m7.append(worry)
        m6=m6[1:]
def Monkey7():
    global m7
    global m4
    global m0
    global c7
    m = m7[:]
    for item in m:
        c7+=1
        worry=(item+2)//3
        if worry%13==0:
            m4.append(worry)
        else:
            m0.append(worry)
        m7=m7[1:]
for _ in range(20):
    Monkey0()
    Monkey1()
    Monkey2()
    Monkey3()
    Monkey4()
    Monkey5()
    Monkey6()
    Monkey7()
inspect=sorted([c0,c1,c2,c3,c4,c5,c6,c7])
print("Answer to part 1:", inspect[-1]*inspect[-2])