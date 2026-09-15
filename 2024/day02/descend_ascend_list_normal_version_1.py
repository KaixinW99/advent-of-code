#
# test the code: python3.11 dampener_check_2.py < input.txt
# check the time: time python3.11 dampener_check_2.py < input.txt
import numpy as np
num_safe = 0
for line in open(0):
    report = [int(x) for x in line.strip().split()]
    ascend_flag = False
    descend_flag = False
    for i in range(len(report)-1):
        if report[i] < report[i+1]:
            ascend_flag = True
            #print('ascend' ,report, report[i], report[i+1])
            if report[i+1]-report[i] > 3:
                break
        elif report[i] > report[i+1]:
            descend_flag = True
            #print('descend', report, report[i], report[i+1])
            if report[i]-report[i+1] > 3:
                break
        else:
            break
    else: # the else only runs after the loop runs without breaking
        if ascend_flag ^ descend_flag:
            num_safe += 1
            #print(report)
print(num_safe)

        
