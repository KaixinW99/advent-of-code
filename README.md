# Advent of Code

My [Advent of Code](https://adventofcode.com) solutions in Python — every puzzle released from 2022 to 2025.

<!-- progress:begin -->
![Advent of Code](https://img.shields.io/badge/Advent%20of%20Code-174%20%E2%98%85-ffff66?style=flat-square&logo=adventofcode&logoColor=ffff66&labelColor=0f0f23)

| Year | Stars | Completion | |
| :--- | ----: | ---------: | :--- |
| [2025](https://adventofcode.com/2025) | 24 / 24 | 100% | `██████████` |
| [2024](https://adventofcode.com/2024) | 50 / 50 | 100% | `██████████` |
| [2023](https://adventofcode.com/2023) | 50 / 50 | 100% | `██████████` |
| [2022](https://adventofcode.com/2022) | 50 / 50 | 100% | `██████████` |

**Total: 174 ★**
<!-- progress:end -->

---

## Contents

<!-- years:begin -->
| Year | Days | Index | Notes |
| :--- | ---: | :--- | :--- |
| 2025 | 12 | [2025/README.md](2025/README.md) | [2025/NOTES.md](2025/NOTES.md) |
| 2024 | 25 | [2024/README.md](2024/README.md) |  |
| 2023 | 25 | [2023/README.md](2023/README.md) |  |
| 2022 | 25 | [2022/README.md](2022/README.md) |  |
<!-- years:end -->

Each year's index lists every day with the puzzle name and links to each solution file. File names describe
the technique used, and several days keep more than one approach side by side (a brute force next to the
version that scales, or two geometric methods for the same answer).

## Highlights — algorithms by puzzle

| Technique | Where |
| :--- | :--- |
| Dijkstra's algorithm, Dial's bucket queue | [2023 day 17](2023/day17/) · [2024 day 16](2024/day16/) (with path backtracking) |
| A\* search and grid BFS | [2022 day 12](2022/day12/) |
| BFS / DFS on grids and graphs | [2022 day 16](2022/day16/) · [2024 day 10](2024/day10/) · [2024 day 18](2024/day18/) · [2025 day 7](2025/day07/) |
| Dynamic programming, memoised recursion | [2023 day 12](2023/day12/) · [2024 day 11](2024/day11/) · [2024 day 19](2024/day19/) · [2025 day 11](2025/day11/) (paths in a DAG) |
| Computational geometry — shoelace formula, Pick's theorem, ray casting, flood fill, line intersections | [2023 day 10](2023/day10/) (several methods compared) · [2023 day 18](2023/day18/) · [2022 day 15](2022/day15/) |
| Graph theory — cliques, minimum edge cut (NetworkX) | [2024 day 23](2024/day23/) · [2023 day 25](2023/day25/) · [2023 day 20](2023/day20/) |
| Disjoint-set union (union–find) | [2025 day 8](2025/day08/) |
| Linear algebra — linear systems, Gaussian elimination over GF(2), integer linear programming | [2024 day 13](2024/day13/) · [2025 day 10](2025/day10/) |
| Symbolic solving with SymPy | [2023 day 24](2023/day24/) |
| Interval merging, coordinate compression | [2025 day 5](2025/day05/) · [2025 day 9](2025/day09/) |
| Cycle detection and extrapolation | [2022 day 17](2022/day17/) · [2023 day 14](2023/day14/) · [2023 day 21](2023/day21/) (quadratic fit) |
| Reverse-engineering a small virtual machine | [2024 day 17](2024/day17/) |
| Prefix sums | [2023 day 11](2023/day11/) |

## Running a solution

Puzzle inputs are **not** included (see below) — download your own from the puzzle page.

```bash
python -m pip install -r requirements.txt

# 2023–2025: read the input from standard input
python 2024/day07/operation_combinatorics_1.py < my_input.txt

# 2022: read input.dat from the solution's own folder
cd 2022/day01 && python find_max_sum.py
```

Files ending in `_1` / `part1` solve part one, `_2` / `part2` part two.

## What is (and isn't) in this repository

Advent of Code asks that puzzle text and personal inputs not be redistributed. Only my own solution code,
notes and diagrams are here; `.gitignore` excludes `input*`, `test*`, `short_input*` and `*.dat` files as a
second safeguard.

## Regenerating the progress table

The table at the top is generated from [`stars.json`](stars.json):

```bash
python tools/make_readme.py          # rewrite the table
python tools/make_readme.py --check  # exit 1 if it is stale
```

## Notes

The code is kept as written during each event — including approaches that turned out too slow or wrong
(e.g. `*_notcorrect.py`, `*_err.py`) — because the comparison between a first attempt and the version that
works is the most useful part to reread.
