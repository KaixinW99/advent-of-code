#! /usr/bin/env python3
import sys

def main():
    grid = [list(line) for line in sys.stdin.read().strip().splitlines()]
    if not grid:
        print(0)
        return

    R = len(grid)
    C = len(grid[0])

    # find the starting position 'S'
    start_r = start_c = None
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'S':
                start_r, start_c = r, c
                break
        if start_r is not None:
            break

    if start_r is None:
        print(0)
        return

    # counts for current row: number of timelines arriving at each column
    counts = [0] * C
    counts[start_c] = 1

    # propagate from the row after the start downwards
    for r in range(start_r + 1, R):
        next_counts = [0] * C
        for c in range(C):
            if counts[c] == 0:
                continue
            ch = grid[r][c]
            if ch == '^':
                # splitter: timelines split to left and right cells on the same row
                if c - 1 >= 0:
                    next_counts[c - 1] += counts[c]
                if c + 1 < C:
                    next_counts[c + 1] += counts[c]
            else:
                # otherwise the timeline continues straight down into same column
                next_counts[c] += counts[c]
        counts = next_counts

    # total timelines after completing all journeys: sum of counts at last processed row
    print(sum(counts))


if __name__ == '__main__':
    main()