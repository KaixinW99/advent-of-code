#
# test the code: python3.11 descend_ascend_list_1.py < input.txt
# check the time: time python3.11 descend_ascend_list_1.py < input.txt
import numpy as np
num_safe = 0
for line in open(0):
    report = np.array([int(x) for x in line.strip().split()])
    report_diff = np.diff(report)
    if np.all((report_diff >= 1)&(report_diff <= 3)) or np.all((report_diff <= -1)&(report_diff >= -3)):
        num_safe += 1
print(num_safe)