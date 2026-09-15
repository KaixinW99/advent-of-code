#
# test the code: python3.10 find_number_in_str.py < input.txt
# check the time: time python3.10 find_number_in_str.py < input.txt
import re
all_str = [line.strip() for line in open(0)]
sum_first_last_digit = 0
for s in all_str:
    all_digit = re.findall('[0-9]',s) # Here we can also use "\d"
    sum_first_last_digit += int(all_digit[0]+all_digit[-1])
print(sum_first_last_digit)

    