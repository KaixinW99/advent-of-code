#
# test the code: python simulator_1.py < input.txt
# check the time: time python simulator_1.py < input.txt

initial_arr = open(0).read().strip().split()
for _ in range(25):
    new_arr = []
    for stone in initial_arr:
        digit_len = len(stone)
        if stone == '0':
            new_arr.append('1')
        elif not digit_len&1:
            new_arr.append('%d'%int(stone[:digit_len//2]))
            new_arr.append('%d'%int(stone[digit_len//2:]))
        else:
            new_arr.append('%d'%(int(stone)*2024))
    #print(new_arr)
    initial_arr = new_arr
print(len(initial_arr))