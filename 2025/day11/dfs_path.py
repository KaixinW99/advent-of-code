#!/usr/bin/env python3
import sys
from collections import defaultdict
path_dict = defaultdict(list)
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    key, values = line.split(': ')
    for v in values.split(' '):
        path_dict[key].append(v)

def dfs_paths(path, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(path_dict[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def dfs_paths_count(path, start, goal):
    count = 0
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(path_dict[vertex]) - set(path):
            if next == goal:
                count += 1
            else:
                stack.append((next, path + [next]))
    return count

show_path = False
if show_path:
    for p in dfs_paths(path_dict, 'you', 'out'):
        print(' -> '.join(p))

print(dfs_paths_count(path_dict, 'you', 'out'))