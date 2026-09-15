#
# test the code: python3.11 dampener_check_2.py < input.txt
# check the time: time python3.11 dampener_check_2.py < input.txt
import numpy as np
num_safe = 0
for line in open(0):
    report = np.array([int(x) for x in line.strip().split()])
    for i in range(len(report)):
        c_report = report[:]
        c_report = np.delete(c_report, i)
        report_diff = np.diff(c_report)
        if np.all((report_diff >= 1)&(report_diff <= 3)) or np.all((report_diff <= -1)&(report_diff >= -3)):
            num_safe += 1
            break
print(num_safe)

        
