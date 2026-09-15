#
# test the code: python3.10 predict_series_1.py < input.txt
# check the time: time python3.10 predict_series_1.py < input.txt

total = 0

def extrapolate(nums):
    if all(x==0 for x in nums):
        return 0
    else:
        return nums[-1] + extrapolate([y-x for x, y in zip(nums,nums[1:])])

for line in open(0):
    nums = list(map(int,line.split()))
    total += extrapolate(nums)
print(total)