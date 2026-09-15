#! /usr/bin/env python3
import sys
fresh_ranges, available_id = sys.stdin.read().strip().split('\n\n')

all_ranges = []
for r in fresh_ranges.splitlines():
    start, end = map(int, r.split('-'))
    all_ranges.append(range(start, end + 1))

all_fresh = 0
for avail in available_id.splitlines():
    avail_id = int(avail)
    for r in all_ranges:
        if avail_id in r:
            all_fresh += 1
            break
print(all_fresh)