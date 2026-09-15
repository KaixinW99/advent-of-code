#
# test the code: python operation_combinatorics_2.py < input.txt
# check the time: time python operation_combinatorics_2.py < input.txt

from itertools import product

def eval_expr(elements, operators):
    result = elements[0]
    for i in range(len(operators)):
        next_element = elements[i+1]
        if operators[i] == "+":
            result += next_element
        elif operators[i] == "*":
            result *= next_element
        elif operators[i] == "||":
            result = result * 10 ** len(str(next_element)) + next_element
    return result

success_test_sum = 0
for line in open(0):
    test_str, elements_str = line.strip().split(":")
    test_val, elements_val = int(test_str), list(map(int, elements_str.strip().split()))
    for combination in product(["+", "*", "||"], repeat=len(elements_val)-1):
        if eval_expr(elements_val, combination) == test_val:
            success_test_sum += test_val
            break
print(success_test_sum)