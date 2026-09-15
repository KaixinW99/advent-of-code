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
2025/  2024/  2023/  2022/
  README.md        # index of the year: puzzle, approach notes, links to each file
  NOTES.md         # (2025) short write-up of the idea behind each day
  day01/ … day25/
    *_1.py, *_2.py # part 1 and part 2; several days keep more than one approach
tools/
  make_readme.py   # regenerates the progress table above from stars.json
stars.json         # star counts per event
```

File names describe the technique used (`dijkstras_algorithm_2.py`, `shoelace_formula_picks_theorem.py`,
`disjoint-set_union.py`, …), so the year indexes double as a map of which algorithm solved which puzzle.

## Running a solution

Puzzle inputs are not included — download your own from the puzzle page. Most solutions read standard input;
the 2022 ones read `input.dat` from their own folder:

```bash
python 2024/day07/operation_combinatorics_1.py < my_input.txt
cd "2022/day01" && python find_max_sum.py      # expects input.dat here
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
