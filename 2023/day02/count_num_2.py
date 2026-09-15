#
# test the code: python3.10 count_num_2.py < input.txt
# check the time: time python3.10 count_num_2.py < input.txt
import re
import math

game_record = [line.strip().split(";") for line in open(0)]
sum_power_cubes = 0
for game_index, game in enumerate(game_record):
    bag = {
        "red":1,
        "green":1,
        "blue":1,
    }
    num_run = len(game)
    run_flag = 0
    for run_index, run in enumerate(game):
        for num, item in re.findall(r'(\d+) (\w+)',run):
            if bag[item] < int(num):
                bag[item] = int(num)
        else:
            run_flag += 1
    if run_flag == num_run:
        sum_power_cubes += math.prod(bag.values())
        
print(sum_power_cubes)