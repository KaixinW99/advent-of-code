#
# test the code: python similar_score_2.py < input.txt
# check the time: time python similar_score_2.py < input.txt
from collections import Counter
similar_score= 0
col1, col2= zip(*[[int(x) for x in line.strip().split()] for line in open(0)])
col2_dict = Counter(col2)
for num in col1:
    similar_score += num*col2_dict.get(num,0)
print(similar_score)