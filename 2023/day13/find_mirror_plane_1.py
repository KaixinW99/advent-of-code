#
# test the code: python3.10 find_mirror_plane_1.py < input.txt
# check the time: time python3.10 find_mirror_plane_1.py < input.txt

grids = [island.split() for island in open(0).read().split("\n\n")]

def to_bin(array):
    return sum(2**i if ch == "#" else 0 for i, ch in enumerate(array))

def find_mirror(nums):
    for i in range(1,len(nums)):
        original = i
        j = i - 1
        while i<len(nums) and j>=0:
            if nums[i] != nums[j]:
                break
            i += 1
            j -= 1
        else:
            return original
    else:
        return 0

total = 0
for island in grids:
    rows = list(map(to_bin,island))
    cols = list(map(to_bin,zip(*island)))
    #print(find_mirror(rows) or find_mirror(cols))
    total += 100*find_mirror(rows) or find_mirror(cols)
print(total)
    