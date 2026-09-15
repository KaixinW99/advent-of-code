#! /usr/bin/env python3
import sys
joltage = 0
for line in sys.stdin.read().strip().splitlines():
    numbers = list(map(int, list(line)))
    joltage += max(10*x+y for ix, x in enumerate(numbers) 
                   for y in numbers[ix+1:])
print(joltage)