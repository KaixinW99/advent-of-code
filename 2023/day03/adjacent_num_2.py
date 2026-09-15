#
# test the code: python3.10 adjacent_num_1.py < input.txt
# check the time: time python3.10 adjacent_num_1.py < input.txt

grid = open(0).read().splitlines()

total_gear = 0
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch != "*":
            continue
        
        num_start = set()

        for cr in [r-1, r, r+1]:
            for cc in [c-1, c, c+1]:
                if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[cr]) or not grid[cr][cc].isdigit():
                    continue
                while cc > 0 and grid[cr][cc-1].isdigit():
                    cc -= 1
                num_start.add((cr,cc))
        
        if len(num_start) != 2:
            continue

        num_list = []
        for rs, cs in num_start:
            s = ""
            while cs < len(grid[rs]) and grid[rs][cs].isdigit():
                s += grid[rs][cs]
                cs += 1 
            num_list.append(int(s))
        
        total_gear += num_list[0]*num_list[1]
print(total_gear)