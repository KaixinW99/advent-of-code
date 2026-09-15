#!/usr/bin/env python3
from __future__ import annotations

import re
from dataclasses import dataclass
from functools import lru_cache
from typing import List, Tuple, Dict


# -------------------------
# Data structures
# -------------------------
@dataclass(frozen=True)
class Orient:
    # cells normalized so min corner is (0,0)
    cells: Tuple[Tuple[int, int], ...]
    w: int
    h: int
    area: int


# -------------------------
# Parsing
# -------------------------
def parse_input(path: str) -> Tuple[Dict[int, List[str]], List[Tuple[int, int, Tuple[int, ...]]]]:
    lines = open(path, "r", encoding="utf-8").read().splitlines()

    # Find first region line
    region_start = None
    for i, line in enumerate(lines):
        if re.match(r"^\s*\d+x\d+:", line):
            region_start = i
            break
    if region_start is None:
        raise ValueError("No region lines like 'WxH:' found.")

    # Parse shapes
    shapes_raw: Dict[int, List[str]] = {}
    i = 0
    while i < region_start:
        st = lines[i].strip()
        if not st:
            i += 1
            continue

        m = re.match(r"^(\d+):$", st)
        if not m:
            raise ValueError(f"Unexpected line in shapes section: {lines[i]!r}")

        sid = int(m.group(1))
        i += 1

        grid: List[str] = []
        while i < region_start:
            s = lines[i].rstrip("\n")
            st2 = s.strip()
            if st2 == "":
                break
            if re.match(r"^\d+:$", st2):      # next shape header
                break
            if re.match(r"^\d+x\d+:", st2):   # region section begins
                break
            grid.append(s)
            i += 1

        shapes_raw[sid] = grid

        # consume optional blank lines
        while i < region_start and lines[i].strip() == "":
            i += 1

    # Parse regions
    regions: List[Tuple[int, int, Tuple[int, ...]]] = []
    for line in lines[region_start:]:
        st = line.strip()
        if not st:
            continue
        m = re.match(r"^(\d+)x(\d+):\s*(.*)$", st)
        if not m:
            raise ValueError(f"Bad region line: {line!r}")
        w, h = int(m.group(1)), int(m.group(2))
        rest = m.group(3).strip()
        counts = tuple(map(int, rest.split())) if rest else tuple()
        regions.append((w, h, counts))

    # Sanity
    shape_ids = sorted(shapes_raw.keys())
    if shape_ids != list(range(len(shape_ids))):
        raise ValueError(f"Shape ids must be 0..K-1, got {shape_ids}")
    K = len(shape_ids)
    for w, h, counts in regions:
        if len(counts) != K:
            raise ValueError(f"Region {w}x{h} has {len(counts)} counts, expected {K}.")

    return shapes_raw, regions


# -------------------------
# Shape orientations (rotations + flips)
# -------------------------
def _normalize(cells: List[Tuple[int, int]]) -> Tuple[Tuple[Tuple[int, int], ...], int, int]:
    minx = min(x for x, _ in cells)
    miny = min(y for _, y in cells)
    shifted = [(x - minx, y - miny) for x, y in cells]
    shifted.sort()
    w = max(x for x, _ in shifted) + 1
    h = max(y for _, y in shifted) + 1
    return tuple(shifted), w, h


def gen_orients(grid: List[str]) -> List[Orient]:
    base = [(x, y) for y, row in enumerate(grid) for x, ch in enumerate(row) if ch == "#"]
    if not base:
        raise ValueError("Empty shape?")
    area = len(base)

    def rot90(cs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        # (x,y) -> (y, -x)
        return [(y, -x) for x, y in cs]

    def flipx(cs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        # reflect x -> -x
        return [(-x, y) for x, y in cs]

    out: List[Orient] = []
    seen = set()
    cur = base
    for _ in range(4):
        for f in (0, 1):
            cs = cur if f == 0 else flipx(cur)
            norm_cells, w, h = _normalize(cs)
            if norm_cells not in seen:
                seen.add(norm_cells)
                out.append(Orient(norm_cells, w, h, area))
        cur = rot90(cur)
    return out


# -------------------------
# Bitboard helpers
# -------------------------
def make_mask(cells: Tuple[Tuple[int, int], ...], W: int) -> int:
    m = 0
    for x, y in cells:
        m |= 1 << (y * W + x)
    return m


def lowest_empty_index(occ: int, FULL: int) -> int:
    empty = (~occ) & FULL
    lsb = empty & -empty
    return lsb.bit_length() - 1


# -------------------------
# Count packing (fast state encoding)
# 7 bits per shape supports counts up to 127 (your max is 81)
# -------------------------
BITS_PER = 7
MASK_PER = (1 << BITS_PER) - 1


def pack_counts(counts: Tuple[int, ...]) -> int:
    x = 0
    shift = 0
    for c in counts:
        x |= (c & MASK_PER) << shift
        shift += BITS_PER
    return x


def get_count(packed: int, sid: int) -> int:
    return (packed >> (sid * BITS_PER)) & MASK_PER


def dec_packed(packed: int, sid: int) -> int:
    # assumes count > 0
    return packed - (1 << (sid * BITS_PER))


# -------------------------
# Solver for one region: "pack" all pieces; leftover space allowed
# Strategy: pick first empty cell p, either:
#   (a) place some piece that covers p, or
#   (b) mark p as unused (leave it empty)
# -------------------------
def can_pack(W: int, H: int, counts: Tuple[int, ...], shape_orients: List[List[Orient]]) -> bool:
    K = len(counts)
    N = W * H
    FULL = (1 << N) - 1

    # Precompute per-shape orientation base masks (at origin) for this W
    o_masks: List[List[int]] = [[] for _ in range(K)]
    o_cells: List[List[Tuple[Tuple[int, int], ...]]] = [[] for _ in range(K)]
    o_wh: List[List[Tuple[int, int]]] = [[] for _ in range(K)]
    areas: List[int] = [0] * K

    for sid in range(K):
        orients = shape_orients[sid]
        areas[sid] = orients[0].area
        for o in orients:
            o_masks[sid].append(make_mask(o.cells, W))
            o_cells[sid].append(o.cells)
            o_wh[sid].append((o.w, o.h))

    packed0 = pack_counts(counts)

    @lru_cache(maxsize=None)
    def rem_area(packed: int) -> int:
        total = 0
        for sid in range(K):
            c = get_count(packed, sid)
            if c:
                total += c * areas[sid]
        return total

    @lru_cache(maxsize=None)
    def dfs(occ: int, packed: int) -> bool:
        # All pieces placed -> success (leftover empty allowed)
        if packed == 0:
            return True

        # Not enough free cells left for remaining area -> fail
        free = (FULL ^ occ).bit_count()
        if rem_area(packed) > free:
            return False

        # If no empty cells but still pieces -> fail
        if occ == FULL:
            return False

        # Choose the first empty cell
        p = lowest_empty_index(occ, FULL)
        x0, y0 = p % W, p // W

        # Pick a shape (remaining>0) with the fewest candidate placements covering p
        best_sid = -1
        best_cands: List[int] | None = None

        for sid in range(K):
            if get_count(packed, sid) == 0:
                continue

            cands: List[int] = []
            # Generate placements that cover (x0,y0) by anchoring each # cell onto it
            for oi in range(len(o_masks[sid])):
                sw, sh = o_wh[sid][oi]
                base = o_masks[sid][oi]
                for (cx, cy) in o_cells[sid][oi]:
                    ox = x0 - cx
                    oy = y0 - cy
                    if ox < 0 or oy < 0 or ox > W - sw or oy > H - sh:
                        continue
                    pmask = base << (oy * W + ox)
                    cands.append(pmask)

            if not cands:
                continue
            if best_cands is None or len(cands) < len(best_cands):
                best_sid = sid
                best_cands = cands
                if len(best_cands) == 1:
                    break

        # Try placing a piece covering p
        if best_cands is not None:
            new_packed = dec_packed(packed, best_sid)
            for pmask in best_cands:
                if (occ & pmask) == 0:
                    if dfs(occ | pmask, new_packed):
                        return True

        # Or: leave p empty (block it)
        return dfs(occ | (1 << p), packed)

    return dfs(0, packed0)


def solve_file(path: str) -> int:
    shapes_raw, regions = parse_input(path)
    K = len(shapes_raw)
    shape_orients = [gen_orients(shapes_raw[sid]) for sid in range(K)]

    ok = 0
    for W, H, counts in regions:
        if can_pack(W, H, counts, shape_orients):
            ok += 1
    return ok


if __name__ == "__main__":
    # Change to your actual filename if needed
    print(solve_file("input"))
