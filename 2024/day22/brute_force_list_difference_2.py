#
# test the code: python brute_force_list_difference_2.py < input.txt
# check the time: time python brute_force_list_difference_2.py < input.txt
from collections import defaultdict
def brute_force_calculate(num):
    # 2**24 = 16777216
    num = (num<<6^num)&16777215
    num = (num>>5^num)&16777215
    num = (num<<11^num)&16777215
    return num

def main():
    length_of_seqs = 4
    seq_to_total = defaultdict(int)
    for line in open(0):
        num = int(line)
        buyer = [num%10]
        for _ in range(2000):
            num = brute_force_calculate(num)
            buyer.append(num%10)
        seen = set() # list cannot be put in the set, as it is not hashable
        for i in range(len(buyer)-length_of_seqs):
            block = buyer[i:i+length_of_seqs+1]
            seq = tuple(b-a for a, b in zip(block, block[1:]))
            if seq in seen: continue
            seen.add(seq)
            seq_to_total[seq] += block[-1]
    print(max(seq_to_total.values()))

if __name__ == "__main__":
    main()