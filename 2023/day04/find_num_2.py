#
# test the code: python3.10 find_num_2.py < input.txt
# check the time: time python3.10 find_num_2.py < input.txt

each_line = [card.split(":")[1].strip() for card in open(0).read().splitlines()]
scratchcards = [1]*len(each_line)
for run, nums in enumerate([run.split("|") for run in each_line]):
    elf, you = nums
    elf, you = set(elf.strip().split()), set(you.strip().split())
    num_wins = len(elf&you)
    if num_wins == 0:
        continue
    else:
        for win_card in range(1,num_wins+1):
            scratchcards[run+win_card] += scratchcards[run]
print(sum(scratchcards))