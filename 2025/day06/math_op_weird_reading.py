#! /usr/bin/env python
import sys
from functools import reduce

sum_all = 0
# allow reading from a filename argument 
# (easier to run from different shells)
data = None
if len(sys.argv) > 1:
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        data = f.read()
else:
    data = sys.stdin.read()

lines = data.splitlines()
if not lines:
    print(0)
    sys.exit(0)

# pad lines to the same length (preserve spaces)
max_len = max(len(l) for l in lines)
# The ljust() method returns a new string that is left-aligned 
# and padded to the specified width
rows = [l.ljust(max_len) for l in lines]

# operator row is the bottom line
op_row = rows[-1]
digit_rows = rows[:-1]

col = max_len - 1
while col >= 0:
    # find next non-empty column (a column that isn't all spaces in all rows)
    # treat a column as empty if every row has a space at that column
    if all(r[col] == ' ' for r in rows):
        col -= 1
        continue

    # found the right boundary of a block; find the left boundary
    right = col
    left = col
    while left - 1 >= 0 and not all(r[left - 1] == ' ' for r in rows):
        left -= 1

    # process block columns from right to left (cephalopod order)
    # find operator in the op_row within block (first non-space)
    block_op = None
    for c in range(right, left - 1, -1):
        ch = op_row[c]
        if ch.strip():
            block_op = ch
            break
    if block_op is None:
        # no operator found; skip block
        col = left - 1
        continue

    nums = []
    for c in range(right, left - 1, -1):
        s = ''.join(r[c] for r in digit_rows).strip()
        if s:
            nums.append(int(s))

    if nums:
        if block_op == '+':
            result = sum(nums)
        elif block_op == '*':
            result = reduce(lambda x, y: x * y, nums)
        else:
            # unknown operator: skip
            result = 0
        sum_all += result

    # move past this block
    col = left - 1

print(sum_all)