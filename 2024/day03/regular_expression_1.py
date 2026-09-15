#
# test the code: python regular_expression_1.py < input.txt
# check the time: time python regular_expression_1.py < input.txt
import re
tot_mul = 0
text = open(0).read()
pattern = r"mul\(\d+,\d+\)"
matches = re.findall(pattern, text)
for mul in matches:
    a, b = map(int, mul[4:-1].split(","))
    tot_mul += a * b
print(tot_mul)