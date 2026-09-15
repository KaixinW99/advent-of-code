#
# test the code: python brute_force_pseudorandom_1.py < input.txt
# check the time: time python brute_force_pseudorandom_1.py < input.txt
def brute_force_calculate(num):
    # 2**24 = 16777216
    num = (num<<6^num)&0xFFFFFF
    num = (num>>5^num)&0xFFFFFF
    num = (num<<11^num)&0xFFFFFF
    return num

def main():
    total = 0
    for line in open(0):
        num = int(line)
        for _ in range(2000):
            num = brute_force_calculate(num)
        total += num
    print(total)
if __name__ == "__main__":
    main()