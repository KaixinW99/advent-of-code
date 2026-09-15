#
# test the code: python3 MMath.py < test.dat
# check the time: time python3 MMath.py < test.dat
monkeys = {}

x = [line.strip() for line in open(0)]

for a in x:
    name, expr = a.split(": ")
    if expr.isdigit():                  # python string isdigit, including "\u00B2" for exponent
        monkeys[name]=int(expr)
    else:
        left, op, right = expr.split()
        if left in monkeys and right in monkeys:
            monkeys[name] = eval(f"{monkeys[left]} {op} {monkeys[right]}")
        else:
            x.append(a)                 # append those which do not have anws yet

print("Anwswer to Part 1:", monkeys["root"])
