#
# test the code: python3.10 compare_size_1.py < input.txt
# check the time: time python3.10 compare_size_1.py < input.txt
from collections import Counter
letter_map = {"T": "A", "J": ".", "Q": "C", "K": "D", "A": "E"} # number is smaller than letter in ord()

def score(hand):
    counts = Counter(hand).values() # or you can apply .count() to the list
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        else:
            return 3
    if 2 in counts:
        if len(counts)==3:
            return 2
        else:
            return 1
    return 0

# ! replace the letter recursively
def replacement(hand):
    if hand == "":
        return [""]
    return [x+y 
            for x in ("23456789TQKA" if hand[0]=="J" else hand[0])
            for y in replacement(hand[1:])]

def classify(hand):
    return max(map(score,replacement(hand)))

def strength(hand):
    return (classify(hand), [letter_map.get(char,char) for char in hand])

plays = []
for line in open(0):
    hand, bid = line.split()
    plays.append((hand,int(bid)))

plays.sort(key = lambda play: strength(play[0]))

total = 0 
for rank, play in enumerate(plays,1): # enumerate(iterable,start=0)
    total += rank*play[1]
print(total)