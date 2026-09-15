#
# test the code: python networkx_graph_interconnect_1.py < input.txt
# check the time: time python networkx_graph_interconnect_1.py < input.txt

def count_hashtags(a):
    return sum([x=="#" for x in a])

keys = set()
lockers = set()
file = open(0).read().strip().split("\n\n")
for frame in file:
    heights = tuple(map(count_hashtags,zip(*frame.split("\n"))))
    if frame[0][0] == "#":
        lockers.add(heights)
    else:
        keys.add(heights)
max_height = len(frame.split("\n"))

fit = 0
for key in keys:
    for locker in lockers:
        assert len(key) == len(locker)
        if all(k+l<=max_height for k, l in zip(key, locker)):
            fit += 1
print(fit)
