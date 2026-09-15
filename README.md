# Advent of Code

My [Advent of Code](https://adventofcode.com) solutions, in Python.

Puzzle inputs and puzzle text are deliberately **not** in this repository — Advent of Code asks
that they not be redistributed. Only my own solution code is here.

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

## Layout

```
2025/
  day01/
    solution.py      # both parts; reads input.txt from the same folder
    notes.md         # optional: the idea, and why the naive approach was too slow
  day02/
  ...
2024/
2023/
2022/
tools/
  make_readme.py     # regenerates the progress table above from stars.json
stars.json           # star counts per event
```

## Running a solution

Each day is self-contained and reads `input.txt` from its own folder. Put your own puzzle input
there (it is gitignored), then:

```bash
cd 2024/day07
python solution.py
```

## Regenerating the progress table

The table above is generated, not hand-maintained. After an event, update `stars.json` and run:

```bash
python tools/make_readme.py          # rewrite README.md
python tools/make_readme.py --check  # exit 1 if stale (useful in CI)
```

## Notes

Advent of Code is a good yearly exercise in the part of programming that research code usually lets
you skip: reading a specification exactly, choosing a data structure before writing anything, and
noticing when an O(n²) approach will not finish. A few days each year are genuinely about algorithms
— graph search, interval arithmetic, cycle detection, dynamic programming — and those are the ones
worth the `notes.md`.
