#
# test the code: python3.10 hash_function_2.py < input.txt
# check the time: time python3.10 hash_function_2.py < input.txt
# by using input(), we can still apply the same situation.
from functools import lru_cache

@lru_cache # for saving the time for repeated calculation on the same recursion
def hash(s):
    val = 0
    for ch in s:
        val = ((val + ord(ch))*17)%256
    return val

boxes = [{} for _ in range(256)] # {label: focal number, ...} for each box number

for item in input().split(","):
    if item[-1] == "-":
        label = item[:-1]
        boxes[hash(label)].pop(label, None)
    else:
        # after python3.6, the sequence of dict is the insertion of dict
        label, focus = item[:-2], int(item[-1])
        boxes[hash(label)][label] = focus

total = 0
for i, box in enumerate(boxes, 1):
    for j, focus in enumerate(box.values(), 1):
        total += i * j * focus

print(total)