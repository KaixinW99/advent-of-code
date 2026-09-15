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

while rc < 2022:
    for jet in jets:
        moved = {x+jet for x in rock}
        if all(0 <=x.real< 7 for x in moved) and not (moved & solid): # all in the scope and no intersection bwt wall and falling rocks
            rock = moved
        moved = {x-1j for x in rock}
        if moved & solid:
            solid |= rock
            rc += 1
            height = max(x.imag for x in solid) + 1         # update the height in the real space before the break
            if rc>=2022:                                    # This is the loop of jets. The fact that finally rocks 
                break                                       # fell in the half jets.                                  
            ri = (ri+1)%5                                   # repeat 4 kinds of falling rocks
            rock = {x+2+(height+3)*1j for x in rocks[ri]}
        else:
            rock = moved
print("Answer to Part 1:",int(height))