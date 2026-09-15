import operator

Rounds = 10000
Threat_Level = 1
Monkeys = 8

data = []
ops = {"+":operator.add,"*":operator.mul}
touches = [0]*Monkeys

def Process(number, operation):
    lhs = number if operation[0]=="old" else int(operation[0])
    rhs = number if operation[2]=="old" else int(operation[2])
    return ops[operation[1]](lhs,rhs) // Threat_Level

with open("input.dat") as file:
    for i in range(Monkeys):
        number = int(file.readline().split()[1][0])
        items = list(map(int,file.readline().strip()[16:].split(", ")))
        #print(list(items))
        operation = file.readline().split()[3:]
        d = int(file.readline().split()[3])
        t = int(file.readline().split()[5])
        f = int(file.readline().split()[5])
        divisible = [d,t,f]
        monkey = [items, operation, divisible]
        data.append(monkey)
        file.readline()
 
Modulus = 1
for monkey in data:
    Modulus *= monkey[2][0]

for round in range(Rounds):
    for index in range(len(data)):
        monkey = data[index]
        for item in monkey[0]:
            touches[index]+=1
            value = Process(item, monkey[1])
            if value % monkey[2][0] == 0:
                data[monkey[2][1]][0].append(value%Modulus)
            else:
                data[monkey[2][2]][0].append(value%Modulus)
        monkey[0].clear()

touches = sorted(touches, reverse=True)
print("Answer to part 2:", touches[0]*touches[1])