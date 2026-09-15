#
# test the code: python networkx_graph_interconnect_1.py < input.txt
# check the time: time python networkx_graph_interconnect_1.py < input.txt

# other overlapping techniques: 11:40 https://www.youtube.com/watch?v=oPIn8VDVmME
locks = []
keys = []

for block in open(0).read().split("\n\n"):
    grid = list(zip(*block.splitlines()))
    if grid[0][0] == "#":
        locks.append([row.count("#")-1 for row in grid])
    else:
        keys.append([row.count("#")-1 for row in grid])

print(sum(all(k+l <= 5 for k, l in zip(key, lock)) for key in keys for lock in locks))