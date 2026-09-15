#
# test the code: python3.10 adjacent_num_1.py < input.txt
# check the time: time python3.10 adjacent_num_1.py < input.txt

grid = open(0).read().splitlines()
num_start = set()
#print(grid)

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch.isdigit() or ch == ".":
            continue
        for cr in [r-1, r, r+1]:
            for cc in [c-1, c, c+1]:
                if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[cr]) or not grid[cr][cc].isdigit():
                    continue
                while cc > 0 and grid[cr][cc-1].isdigit():
                    cc -= 1
                num_start.add((cr,cc))

num_list = []
for r, c in num_start:
    s = ""
    while c < len(grid[r]) and grid[r][c].isdigit():
        s += grid[r][c]
        c += 1 
    num_list.append(int(s))
print(sum(num_list))