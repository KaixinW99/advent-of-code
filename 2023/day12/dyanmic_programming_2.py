#
# test the code: python3.10 dunamic_programming_2.py < input.txt
# check the time: time python3.10 dunamic_programming_2.py < input.txt
from functools import lru_cache

answer = 0
for line in open(0):
    cfg, nums = line.split() # cfg = contiguous forward grid
    nums = tuple(map(int, nums.split(",")))

    cfg = "?".join([cfg]*5) # join the str separated by ? for 5 times
    nums *= 5
    
    cl = len(cfg)

    @lru_cache # to decrease the calculation of recursion
    def calc(ci, ni): # ci is the index of the cfg; ni is th index of nums
        if ci >= cl:
            # end of the cfg
            return 1 if ni >= len(nums) else 0
        if ni >= len(nums):
            # end of the number
            return 0 if "#" in cfg[ci:] else 1
        
        total = 0

        if cfg[ci] != ".":
            # is pound sign # or question mark ?
            if (nums[ni] <= cl - ci) and ("." not in cfg[ci:ci+nums[ni]]) and ((nums[ni] == cl-ci) or (cfg[ci+nums[ni]] != "#")):
                # the # number < remaining length
                # not . in the block
                # the next one is absent or is not a pound sign #
                total += calc(ci + nums[ni] +1, ni + 1)
            
        if cfg[ci] != "#":
            # is a dot . or question mark ?
            total += calc(ci+1, ni)
        return total
    answer += calc(0,0)
print(answer)