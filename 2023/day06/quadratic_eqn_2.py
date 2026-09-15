#
# test the code: python3.10 quadratic_eqn_2.py < input.txt
# check the time: time python3.10 quadratic_eqn_2.py < input.txt

# ! This question is to solve (m-x)x<n
# ! so x1-x2+1 = sqrt(m^2-4*n) + 1
import re
from math import sqrt
from math import ceil,floor
from functools import reduce
time, distance = open(0).read().splitlines()
time = int(reduce(lambda x, y: x+y,re.findall("\d+",time)))
distance = int(reduce(lambda x, y: x+y,re.findall("\d+",distance)))
m, n = time, distance
delta = sqrt(m**2-4*n)
xlo = floor((m-delta)/2+1)
xhi = ceil((m+delta)/2-1)
print(xhi-xlo+1)



