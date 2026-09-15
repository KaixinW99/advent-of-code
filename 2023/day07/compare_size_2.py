#
# test the code: python3.10 compare_size_1.py < input.txt
# check the time: time python3.10 compare_size_1.py < input.txt
from collections import Counter
letter_map = {"T": "A", "J": "1", "Q": "C", "K": "D", "A": "E"} # number is smaller than letter in ord()

def classify(hand):
    counts = Counter(hand) # or you can apply .count() to the list
    counts_value = sorted(counts.values(),reverse=True)

    # special case: "JJJJJ"
    if 5 in counts_value:
        return 6
    
    if 'J' in counts:
        j_value = counts['J']
        counts_value.remove(j_value)
        newmax = counts_value[0]+j_value
        counts_value = counts_value[1:]+[newmax]
    if 5 in counts_value:
        return 6
    if 4 in counts_value:
        return 5
    if 3 in counts_value:
        if 2 in counts_value:
            return 4
        else:
            return 3
    if 2 in counts_value:
        if len(counts_value)==3:
            return 2
        else:
            return 1
    return 0

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