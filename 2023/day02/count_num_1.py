#
# test the code: python3.10 count_num_1.py < input.txt
# check the time: time python3.10 count_num_1.py < input.txt
import re

bag = {
    "red":12,
    "green":13,
    "blue":14,
}

game_record = [line.strip().split(";") for line in open(0)]
sum_game_index = 0
for game_index, game in enumerate(game_record):
    num_run = len(game)
    run_flag = 0
    for run_index, run in enumerate(game):
        for num, item in re.findall(r'(\d+) (\w+)',run):
            if bag[item] < int(num):
                break
        else:
            run_flag += 1
    if run_flag == num_run:
        sum_game_index += game_index + 1
print(sum_game_index)