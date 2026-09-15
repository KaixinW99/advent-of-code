#! /usr/bin/env python3
import sys
from math import prod


def read_points(lines):
    pts = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        pts.append(tuple(map(int, line.split(','))))
    return pts


class DSU:
    # Disjoint-Set Union (Union-Find) data structure with path compression and union by size.
    def __init__(self, n):
        # parent pointers: self.p[x] is the parent of x in the disjoint-set forest.
        # If self.p[x] == x then x is a root.
        self.p = list(range(n))
        # size array: self.sz[root] is the size of the component whose root is `root`.
        # Used to attach the smaller tree under the larger one (union by size).
        self.sz = [1] * n

    def find(self, x):
        # find root with path-halving compression: while walking up the tree
        # set each node's parent to its grandparent (self.p[self.p[x]]),
        # which shortens paths and amortizes future finds.
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            # a and b are already in the same component; union would create a cycle
            # (no change). Return False so callers can detect and skip counting it.
            return False
        if self.sz[ra] < self.sz[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        self.sz[ra] += self.sz[rb]
        return True


def squared_dist(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))


def main():
    import sys as _sys
    argv = _sys.argv[1:]
    # Usage:
    #   python3 disjoint-set_union.py [K] [mode]
    # mode: 'pairs' (default) -> take the first K shortest pairs
    #       'unions' -> perform K successful unions, skipping redundant edges
    K = 1000
    mode = 'pairs'
    if argv:
        # try interpret first arg as integer K
        try:
            K = int(argv[0])
            if len(argv) > 1:
                mode = argv[1]
        except ValueError:
            # first arg is not an int, treat it as mode
            mode = argv[0]
            if len(argv) > 1:
                try:
                    K = int(argv[1])
                except ValueError:
                    pass

    pts = read_points(_sys.stdin.read().splitlines())
    n = len(pts)
    if n == 0:
        print(0)
        return

    # build all pairwise edges with squared distances
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((squared_dist(pts[i], pts[j]), i, j))

    edges.sort()

    take = min(K, len(edges))
    dsu = DSU(n)

    if mode.lower() in ('pairs', 'first', 'edges'):
        # Take the first `take` edges (even if some are redundant).
        for k in range(take):
            _, i, j = edges[k]
            dsu.union(i, j)
    else:
        # 'unions' mode: perform `take` successful unions, skipping edges
        # that connect already-connected nodes.
        unions_done = 0
        idx = 0
        while unions_done < take and idx < len(edges):
            _, i, j = edges[idx]
            if dsu.union(i, j):
                unions_done += 1
            idx += 1

    # compute component sizes
    comp = {}
    for i in range(n):
        r = dsu.find(i)
        comp[r] = comp.get(r, 0) + 1

    sizes = sorted(comp.values(), reverse=True)
    # multiply top 3 sizes (if less than 3 components, multiply available ones)
    top3 = sizes[:3]
    result = prod(top3) if top3 else 0
    print(result)


if __name__ == '__main__':
    main()
    def debug_ops():
        d = DSU(6)
        print("initial p", d.p, "sz", d.sz)
        print("union(0,1):", d.union(0,1), "-> p", d.p, "sz", d.sz)
        print("union(2,3):", d.union(2,3), "-> p", d.p, "sz", d.sz)
        print("union(1,2):", d.union(1,2), "-> p", d.p, "sz", d.sz)
        print("union(3,0):", d.union(3,0), "-> p", d.p, "sz", d.sz)  # should be False
        print("find(5):", d.find(5), "p", d.p)
        print("find(3):", d.find(3), "p", d.p)
        comp = {}
        for i in range(6):
            r = d.find(i)
            comp[r] = comp.get(r, 0) + 1
        print("component sizes:", comp)
    
    debug_ops()