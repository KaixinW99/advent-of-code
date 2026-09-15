#! /usr/bin/env python3
import sys
manifolds = [list(line) for line in sys.stdin.read().strip().splitlines()]
split_times = 0
for i in range(1, len(manifolds)):
    for h in range(len(manifolds[i])):
        if manifolds[i-1][h] == '|' or manifolds[i-1][h] == 'S':
            if manifolds[i][h] == '^':
                if h-1 >= 0:
                    manifolds[i][h-1] = '|'
                if h+1 < len(manifolds[i]):
                    manifolds[i][h+1] = '|'
                split_times += 1
            else:
                manifolds[i][h] = '|'

#print('\n'.join(''.join(row) for row in manifolds))
print(split_times)    