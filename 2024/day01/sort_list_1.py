#
# test the code: python sort_list_1.py < input.txt
# check the time: time python sort_list_1.py < input.txt
tot_distance = 0
col1, col2= zip(*[[int(x) for x in line.strip().split()] for line in open(0)])
col1, col2 = list(col1), list(col2)
col1.sort(); col2.sort()
for i in range(len(col1)):
    tot_distance += abs(col1[i] - col2[i])
print(tot_distance)