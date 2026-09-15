#
# test the code: python3.10 hash_function_1.py < input.txt
# check the time: time python3.10 hash_function_1.py < input.txt
# by using input(), we can still apply the same situation.
def hash(s):
    val = 0
    for ch in s:
        val = ((val + ord(ch))*17)%256
    return val
print(sum(map(hash, input().split(","))))