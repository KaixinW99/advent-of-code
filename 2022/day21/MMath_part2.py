#
# test the code: python3 MMath.py < test.dat
# check the time: time python3 MMath.py < test.dat
import sympy                            # ! sympy helps you set up the variables and solution
                                        # ! without sympy, a recursion tree and class should be built to trace back the variable.
monkeys = {"humn": sympy.Symbol("x")}

x = [line.strip() for line in open(0)]

ops = {
    "+": lambda x, y: x+y,
    "-": lambda x, y: x-y,
    "*": lambda x, y: x*y,
    "/": lambda x, y: x/y,
}
for a in x:
    name, expr = a.split(": ")
    if name in monkeys:
        continue
    if expr.isdigit():                  # python string isdigit, including "\u00B2" for exponent
        monkeys[name]=sympy.Integer(expr)
    else:
        left, op, right = expr.split()
        if left in monkeys and right in monkeys:
            if name == "root":
                print("Anwswer to Part 2:",sympy.solve(monkeys[left]-monkeys[right])[0])
                break
            monkeys[name] = ops[op](monkeys[left],monkeys[right])
        else:
            x.append(a)                 # append those which do not have anws yet
