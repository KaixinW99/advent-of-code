#! /usr/bin/env python
import sys
from functools import reduce
sum_all = 0
math_hw = sys.stdin.read().strip().splitlines()
math_hw = zip(*[line.strip().split() for line in math_hw])
for *n, op in math_hw:
    result = reduce(lambda x, y: eval(f"{x}{op}{y}"), map(int, n))
    sum_all += result
print(sum_all)