#! /usr/bin/env python3
import sys
sum_invalid_IDs = 0
for r in sys.stdin.readline().strip().split(','):
    s, e = map(int, r.split('-'))
    ls, le = len(str(s)), len(str(e))
    s = int(10**ls) if ls%2 else s
    e = int(10**(le-1)) if le%2 else e
    for n in range(s, e+1):
        strn = str(n)
        lenn = len(strn)
        if strn[:lenn//2] == strn[lenn//2:]:
            sum_invalid_IDs += n
print(sum_invalid_IDs)