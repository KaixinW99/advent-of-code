#
# test the code: python opcode_oprands_1.py < input.txt
# check the time: time python opcode_oprands_1.py < input.txt
import re

def parse_input():
    a, b, c, *program = map(int, re.findall(r'\d+', open(0).read()))
    return a, b, c, program

def combo(operand, a, b, c):
    if 0 <= operand <= 3: return operand
    if operand == 4: return a
    if operand == 5: return b
    if operand == 6: return c
    else: raise RuntimeError("Invalid combo operand")

def task(a, b, c, program):
    pointer = 0
    output = []

    while pointer < len(program):
        instruction = program[pointer]
        operand = program[pointer + 1]
        if instruction == 0: # adv
            a >>= combo(operand, a, b, c) # a // 2**operand
        elif instruction == 1: # bxl
            b ^= operand
        elif instruction == 2: # bst
            b = combo(operand, a, b, c)&7 # a % b == a & (b-1) if b is a power of 2
        elif instruction == 3: # jnz
            if a != 0:
                pointer = operand
                continue
        elif instruction == 4: # bxc
            b ^= c
        elif instruction == 5: # out
            output.append(combo(operand, a, b, c)&7)
        elif instruction == 6: # bdv
            b = a >> combo(operand, a, b, c)
        elif instruction == 7: # cdv
            c = a >> combo(operand, a, b, c)
        pointer += 2
    return output

def main():
    a, b, c, program = parse_input()
    print(*task(a, b, c, program), sep=',')

if __name__ == "__main__":
    main()