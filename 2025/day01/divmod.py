#!/usr/bin/env python3
import sys

# Concise corrected version: counts both end-of-rotation hits and any-click hits
dial, N = 50, 100
part_any = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    d, steps = line[0], int(line[1:])

    # first click (1..N) that hits 0 during this rotation
    first = (N - dial) % N if d == 'R' else dial

    # adjust for zero case
    if first == 0:
        first = N

    if first <= steps:
        part_any += 1 + (steps - first) // N

    # update dial position
    if d == 'R':
        dial = (dial + steps) % N
    else:
        dial = (dial - steps) % N

print(part_any)