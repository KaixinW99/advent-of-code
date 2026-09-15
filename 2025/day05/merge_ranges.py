#! /usr/bin/env python3
import sys

data = sys.stdin.read().strip()
if not data:
    print(0)
    sys.exit(0)

# take only the first section (fresh ranges). If there's no second section,
# treat the whole input as the ranges block.
if "\n\n" in data:
    fresh_ranges = data.split("\n\n", 1)[0]
else:
    fresh_ranges = data

intervals = []
for r in fresh_ranges.splitlines():
    r = r.strip()
    if not r:
        continue
    start, end = map(int, r.split("-"))
    if start > end:
        start, end = end, start
    intervals.append((start, end))

if not intervals:
    print(0)
    sys.exit(0)

# sort and merge overlapping/adjacent intervals
intervals.sort()
merged = []
cur_s, cur_e = intervals[0]
for s, e in intervals[1:]:
    if s <= cur_e + 1:
        cur_e = max(cur_e, e)
    else:
        merged.append((cur_s, cur_e))
        cur_s, cur_e = s, e
merged.append((cur_s, cur_e))

total = sum(e - s + 1 for s, e in merged)
print(total)