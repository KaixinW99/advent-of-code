#!/usr/bin/env python3
import sys

def read_points():
    text = sys.stdin.read().strip()
    if not text:
        return []
    pts = []
    for line in text.splitlines():
        x, y = map(int, line.split(','))
        pts.append((x, y))
    return pts

def part1(points):
    # Your original solution style
    n = len(points)
    best = 0
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > best:
                best = area
    return best

def largest_rectangle_red_green(points):
    """
    Part 2:
    - points: list of (x, y) red tiles in path order (closed loop).
    - Returns max area rectangle with opposite corners red,
      and all tiles inside rectangle are red or green
      (i.e., rectangle is fully inside the polygon formed by the loop).
    """

    n = len(points)
    if n < 4:
        return 0

    # ----- Coordinate compression -----
    xs = sorted({x for x, y in points})
    ys = sorted({y for x, y in points})
    nx = len(xs)
    ny = len(ys)

    map_x = {x: i for i, x in enumerate(xs)}
    map_y = {y: i for i, y in enumerate(ys)}

    # ----- Build list of vertical edges of the polygon -----
    vertical_edges = []
    # polygon is given in order, wrap last -> first
    for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1]):
        if x1 == x2:
            # vertical edge at x = x1 from y1 to y2
            if y1 < y2:
                vertical_edges.append((x1, y1, y2))
            else:
                vertical_edges.append((x1, y2, y1))
        # horizontal edges are ignored for the scanline intersection

    # ----- Fill "inside" grid using horizontal scanlines -----
    # inside[j][i] == True if cell between
    # [xs[i], xs[i+1]] × [ys[j], ys[j+1]] is inside the polygon
    inside = [[False] * (nx - 1) for _ in range(ny - 1)]

    for j in range(ny - 1):
        y_mid = (ys[j] + ys[j + 1]) / 2.0

        # Collect x-intersections of the scanline with polygon
        inter_x = []
        for x, y1, y2 in vertical_edges:
            # Standard even-odd rule: include if y1 <= y_mid < y2
            if y1 <= y_mid < y2:
                inter_x.append(x)

        inter_x.sort()

        # Each pair of intersections defines an interior x-interval
        # [xL, xR], so set inside=True for cells whose x-interval lies within
        if len(inter_x) % 2 != 0:
            # For a valid simple polygon this should not happen, but
            # we don't crash if it does.
            pass

        for k in range(0, len(inter_x), 2):
            xL = inter_x[k]
            xR = inter_x[k + 1]
            iL = map_x[xL]
            iR = map_x[xR]
            # All columns from iL to iR-1 are inside in this row band
            for i in range(iL, iR):
                inside[j][i] = True

    # ----- 2D prefix sum over inside-grid -----
    # pref[r][c] = number of inside cells in rectangle [0..r)×[0..c)
    pref = [[0] * (nx) for _ in range(ny)]
    for j in range(ny - 1):
        row_sum = 0
        for i in range(nx - 1):
            row_sum += 1 if inside[j][i] else 0
            pref[j + 1][i + 1] = pref[j][i + 1] + row_sum

    def all_cells_inside(colL, colR, rowB, rowT):
        """Check if all cells in [rowB..rowT) × [colL..colR) are inside."""
        inside_cnt = (
            pref[rowT][colR]
            - pref[rowB][colR]
            - pref[rowT][colL]
            + pref[rowB][colL]
        )
        total_cells = (colR - colL) * (rowT - rowB)
        return inside_cnt == total_cells

    # ----- Try all pairs of red tiles as opposite corners -----
    max_area = 0
    for a in range(n):
        x1, y1 = points[a]
        ix1 = map_x[x1]
        iy1 = map_y[y1]

        for b in range(a + 1, n):
            x2, y2 = points[b]

            # Degenerate rectangle (line) -> area zero, skip
            if x1 == x2 or y1 == y2:
                continue

            ix2 = map_x[x2]
            iy2 = map_y[y2]

            colL = min(ix1, ix2)
            colR = max(ix1, ix2)
            rowB = min(iy1, iy2)
            rowT = max(iy1, iy2)

            # Check if that continuous rectangle is fully inside polygon
            if not all_cells_inside(colL, colR, rowB, rowT):
                continue

            # Rectangle is valid (only red/green tiles), compute tile area
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > max_area:
                max_area = area

    return max_area

def main():
    points = read_points()
    if not points:
        return

    # Part 1 (your original style)
    ans1 = part1(points)
    print("Part 1:", ans1)

    # Part 2 using coordinate compression
    ans2 = largest_rectangle_red_green(points)
    print("Part 2:", ans2)

if __name__ == "__main__":
    main()