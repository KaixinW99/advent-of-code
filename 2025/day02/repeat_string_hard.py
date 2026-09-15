#! /usr/bin/env python3
import sys

def is_repeated_sequence(s: str) -> bool:
    """Return True if string s is composed of a smaller substring repeated >= 2 times."""
    L = len(s)
    # A repeated sequence must repeat at least twice, so substring length <= L//2
    for d in range(1, L // 2 + 1):
        if L % d == 0:
            if s == s[:d] * (L // d):
                return True
    return False

def main():
    total = 0
    data = sys.stdin.read().strip()
    if not data:
        return
    # Input expected as comma-separated ranges like "11-22,95-115,..."
    for r in data.split(','):
        r = r.strip()
        if not r:
            continue
        s, e = map(int, r.split('-'))
        # iterate through the range and sum invalid IDs
        for n in range(s, e + 1):
            sn = str(n)
            if is_repeated_sequence(sn):
                total += n
    print(total)

if __name__ == '__main__':
    main()