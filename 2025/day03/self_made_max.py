#! /usr/bin/env python3
import sys

def max_subsequence_value(digits, k):
    """Return integer value of the lexicographically largest subsequence of length k.

    digits: list of digit characters (e.g., ['1','2','3'])
    """
    n = len(digits)
    if n <= k:
        return int(''.join(digits)) if n > 0 else 0

    res = []
    pos = 0
    # We need to pick k digits. For each pick, search the window
    for remaining in range(k, 0, -1):
        # we can search up to index n-remaining inclusive
        end = n - remaining
        # find the maximum digit and its first occurrence in the window
        best = '0'
        best_idx = pos
        for i in range(pos, end + 1):
            d = digits[i]
            if d > best:
                best = d
                best_idx = i
                if best == '9':
                    break
        res.append(best)
        pos = best_idx + 1

    return int(''.join(res))

def main():
    total = 0
    data = sys.stdin.read().strip()
    if not data:
        print(0)
        return
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue
        digits = list(line)
        total += max_subsequence_value(digits, 12)
    print(total)

if __name__ == '__main__':
    main()