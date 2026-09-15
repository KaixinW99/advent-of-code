#
# test the code: python3.10 quadratic_eqn_1.py < input.txt
# check the time: time python3.10 quadratic_eqn_1.py < input.txt

# ! This question is to solve (m-x)x<n
# ! so x1-x2+1 = sqrt(m^2-4*n) + 1
import re
from math import sqrt
from math import ceil,floor
time, distance = open(0).read().splitlines()
time = map(int,re.findall("\d+",time))
distance = map(int,re.findall("\d+",distance))
multiple = 1
for m, n in zip(time,distance):
    delta = sqrt(m**2-4*n)
    xlo = floor((m-delta)/2+1)
    xhi = ceil((m+delta)/2-1)
    multiple *= xhi-xlo+1
print(multiple)


