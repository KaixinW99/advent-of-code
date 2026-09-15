#
# test the code: python recusion_not_dfs_1.py < input.txt
# check the time: time python recusion_not_dfs_1.py < input.txt
from functools import cache

def parse_input():
    patterns, targets = open(0).read().split("\n\n")
    patterns = tuple(patterns.split(", "))
    targets = targets.strip().split("\n")
    return patterns, targets

# tuple and string are hashable, so we can use @cache
@cache
def can_obtain_count(target, patterns, maxlen):
    if target == "": return 1
    count = 0
    for i in range(min(maxlen, len(target))+1):
        if target[:i] in patterns:
            count += can_obtain_count(target[i:], patterns, maxlen)
    return count

def main():
    patterns, targets = parse_input()
    maxlen = max(map(len, patterns))
    print(sum(can_obtain_count(target, patterns, maxlen) for target in targets))

if __name__ == "__main__":
    main()