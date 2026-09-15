#!/usr/bin/env python3
import sys
from collections import defaultdict
from functools import lru_cache

# dac: digital-to-analog converter
# fft: fast fourier transform

# DAG: directed acyclic graph
# Dynamic Programming with memoization (lru_cache)

# mask bits: 1 = saw dac, 2 = saw fft
SPECIAL = {"dac": 1, "fft": 2}

def parse_digraph(f: str) -> dict[str, list[str]]:
    g = defaultdict(list)
    nodes = set()
    for line in f:
        line = line.strip()
        if not line:
            continue
        u, rhs = line.split(":")
        u = u.strip()
        vs = rhs.strip().split() if rhs.strip() else []
        g[u].extend(vs)
        nodes.add(u)
        nodes.update(vs)
    for n in nodes:
        g.setdefault(n, [])
    return g

def count_paths_visit_dac_fft(f: str, start="svr", end="out") -> int:
    g = parse_digraph(f)

    @lru_cache(None)
    def dp(u: str, mask: int) -> int:
        if u == end:
            return 1 if mask == 3 else 0
        total = 0
        for v in g[u]:
            nm = mask | SPECIAL.get(v, 0)
            total += dp(v, nm)
        return total

    init = SPECIAL.get(start, 0)
    return dp(start, init)

print(count_paths_visit_dac_fft(sys.stdin))