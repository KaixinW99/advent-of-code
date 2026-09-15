#
# test the code: python3.10 find_num_1.py < input.txt
# check the time: time python3.10 find_num_1.py < input.txt

points = 0
each_line = [card.split(":")[1].strip() for card in open(0).read().splitlines()]
for nums in [run.split("|") for run in each_line]:
    elf, you = nums
    elf, you = set(elf.strip().split()), set(you.strip().split())
    if len(elf&you) == 0:
        continue
    else:
        points += 2**(len(elf&you)-1)
print(points)

