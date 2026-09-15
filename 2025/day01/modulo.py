#!/usr/bin/env python3
dial, uplimit = 50, 100
password = 0
for line in open(0):
    direction, number = line[0], int(line[1:])
    if direction == 'L':
        dial = (dial - number) % uplimit
    else:
        dial = (dial + number) % uplimit
    if dial == 0:
        password += 1
print(password)