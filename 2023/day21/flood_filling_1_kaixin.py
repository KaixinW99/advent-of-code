#
# test the code: python3.10 flood_filling_1_kaixin.py < input.txt
# check the time: time python3.10 flood_filling_1_kaixin.py < input.txt
grid = [row.strip() for row in open(0)]
((sr, sc), ) = [(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch =="S"]

steps = 64
q = [(sr, sc)]
for _ in range(steps):
    nq = []
    while q:
        pr, pc = q.pop()
        for nr, nc in [(pr + 1, pc), (pr - 1, pc), (pr, pc + 1), (pr, pc - 1)]:
            if grid[nr][nc] != "#" and [nr, nc] not in nq:
                nq.append([nr, nc])
    q = nq
print(len(q))