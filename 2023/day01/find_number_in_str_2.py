#
# test the code: python3.10 find_number_in_str_2.py < input.txt
# check the time: time python3.10 find_number_in_str_2.py < input.txt
import re
all_str = [line.strip() for line in open(0)]
number_in_str = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
}
sum_first_last_digit = 0
for s in all_str:
    dig_pos_list_l = [(number_in_str[letter],s.find(letter)) for letter in number_in_str.keys() if s.find(letter)>=0]
    dig_l = min(dig_pos_list_l,key=lambda x: x[1])[0]
    dig_pos_list_r = [(number_in_str[letter],s.rfind(letter)) for letter in number_in_str.keys() if s.rfind(letter)>=0]
    dig_r = max(dig_pos_list_r,key=lambda x: x[1])[0]
    sum_first_last_digit += int(str(dig_l)+str(dig_r))
print(sum_first_last_digit)

    