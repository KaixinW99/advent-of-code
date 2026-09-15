#
# ! Use conplex number to show the position
# test the code: python3 PV_part2.py < test.dat
# check the time: time python3 PV_part2.py < test.dat

# origin locates at bottom left
rocks = [
    [0,1,2,3],
    [1,1j,1+1j,2+1j,1+2j],
    [0,1,2,2+1j,2+2j],
    [0,1j,2j,3j],
    [0,1,1j,1+1j],
]

jets = [1 if x==">" else -1 for x in input()]

solid = {x-1j for x in range(7)}
height = 0

rc = 0                                              # count rocks

ri = 0                                              # rock index
rock = {x+2+(height+3)*1j for x in rocks[ri]}       # position of falling rocks

increment = []
T = 20
while rc < T:
    for jet in jets:
        moved = {x+jet for x in rock}
        if all(0 <=x.real< 7 for x in moved) and not (moved & solid): # all in the scope and no intersection bwt wall and falling rocks
            rock = moved
        moved = {x-1j for x in rock}
        if moved & solid:
            solid |= rock
            rc += 1
            o_height = height
            height = max(x.imag for x in solid) + 1         # update the height in the real space before the break
            increment.append(int(height-o_height))

            if rc>=T:                                    # This is the loop of jets. The fact that finally rocks 
                break                                       # fell in the half jets.                                  
            ri = (ri+1)%5                                   # repeat 4 kinds of falling rocks
            rock = {x+2+(height+3)*1j for x in rocks[ri]}
        else:
            rock = moved

# ! the length of jets is 10091, and it's too large for it to track


# A Python program to check if a string is 'n' times
# repetition of one of its substrings

# A utility function to fill lps[] or compute prefix function
# used in KMP string matching algorithm. Refer
# https://www.geeksforgeeks.org/archives/11902 for details
def computeLPSArray(string, M, lps):
	length = 0	 # length of the previous longest prefix suffix
	i = 1

	lps[0] = 0 # lps[0] is always 0

	# the loop calculates lps[i] for i = 1 to M-1
	while i < M:
		if string[i] == string[length]:
			length += 1
			lps[i] = length
			i += 1
		else:
			if length != 0:			
				# This is tricky. Consider the example AAACAAAA
				# and i = 7.
				length = lps[length-1]

				# Also, note that we do not increment i here
			else:
				lps[i] = 0
				i += 1


# Returns true if string is repetition of one of its substrings
# else return false.
def isRepeat(string):
	# Find length of string and create an array to
	# store lps values used in KMP
	n = len(string)
	lps = [0] * n

	# Preprocess the pattern (calculate lps[] array)
	computeLPSArray(string, n, lps)

	# Find length of longest suffix which is also
	# prefix of str.
	length = lps[n-1]

	# If there exist a suffix which is also prefix AND
	# Length of the remaining substring divides total
	# length, then str[0..n-len-1] is the substring that
	# repeats n/(n-len) times (Readers can print substring
	# and value of n/(n-len) for more clarity.
	if length > 0 and n%(n-length) == 0:
		return True
	else:
		False



