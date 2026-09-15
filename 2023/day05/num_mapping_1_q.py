#
# test the code: python3.10 num_mapping_1.py < input.txt
# check the time: time python3.10 num_mapping_1.py < input.txt

seeds, *blocks = open(0).read().split("\n\n")
seeds =  list(map(int, seeds.split(":")[1].split()))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    for x in seeds:
        for a, b, c in ranges:
            if x in range(b,b+c):
                new.append(x-b+a)
                break
        else:
            new.append(x)
    seeds = new 
print(min(seeds))