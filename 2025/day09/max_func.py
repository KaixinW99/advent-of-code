#! /usr/bin/env python3
import sys
pos = [tuple(map(int, line.split(','))) for line in sys.stdin.read().strip().splitlines()]
print(max((abs(p1[0] - p2[0])+1) * (abs(p1[1] - p2[1])+1) for ip1, p1 in enumerate(pos) for p2 in pos[ip1+1:]))