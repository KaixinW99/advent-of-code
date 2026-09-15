#
# test the code: python regular_expression_1.py < input.txt
# check the time: time python regular_expression_1.py < input.txt
import re
tot_mul = 0
text = open(0).read()
pattern = r"don't\(\)|do\(\)|mul\(\d+,\d+\)"
matches = re.findall(pattern, text)
do_flag = True
for instance in matches:
    if instance == "don't()":
        do_flag = False
    elif instance == "do()":
        do_flag = True
    else:
        if do_flag:
            mul = instance.split("(")[1].split(")")[0].split(",")
            tot_mul += int(mul[0]) * int(mul[1])
print(tot_mul)