#
# test the code: python opcode_oprands_reverse_engineering_2.py < input.txt
# check the time: time python opcode_oprands_reverse_engineering_2.py < input.txt

# based on input_math.txt
import re

def parse_input():
    a, b, c, *program = map(int, re.findall(r'\d+', open(0).read()))
    assert program[-2:] == [3, 0]
    return a, b, c, program

def find(program, ans):
    if program == []:
        return ans
    for t in range(8):
        a = ans << 3 | t
        b = a%8
        b = b^7
        c = a >> b
        b = b ^ c
        b = b^7
        if b%8 == program[-1]:
            sub = find(program[:-1], a)
            if sub is not None:
                return sub

def main():
    a, b, c, program = parse_input()
    print(find(program, 0))

if __name__ == "__main__":
    main()