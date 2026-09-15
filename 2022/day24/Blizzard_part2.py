#
# test the code: python3 Blizzard.py < test.dat
# check the time: time python3 Blizzard.py < test.dat
import math
from collections import deque

blizzards = tuple(set() for _ in range(4))

for r,line in enumerate(open(0).read().splitlines()[1:]):
    for c, item in enumerate(line[1:]):
        if item in "<>^v":
            blizzards["<>^v".find(item)].add((r,c))

queue = deque([(0, -1, 0, 0)])         # shift ourselves in the opposite direction instead of blizzards
targets = [(r, c-1),(-1,0)]

seen = set()
lcm = r*c//math.gcd(r,c)            #! Opt 1: inly consider states that differ by something that isnt a multiple of LCM

final_stage = 2                     # how many times to go one path? forth back and forth --> 2

while queue:
    time, cr, cc, stage = queue.popleft()
    time += 1
    for dr, dc in ((0,1),(0,-1),(-1,0),(1,0),(0,0)):
        nr = cr+dr
        nc = cc+dc

        if (nr,nc) == targets[stage % 2]:
            if stage == final_stage:
                print("Answer to Part 2:",time)
                exit(0)
            stage +=1
        
        if (nr<0 or nc<0 or nr>=r or nc>=c) and (nr, nc) not in targets:
            continue

        fail = False
        if (nr,nc) not in targets:     #! Noting: The blizzard check removed from starting point becasue they may think you cannot stay on the starting square
            for i, tr, tc in ((0,0,-1),(1,0,1),(2,-1,0),(3,1,0)):
                if ((nr-tr*time)%r, (nc-tc*time)%c) in blizzards[i]: #! Opt 2: shift ourselves in the opposite direction instead of blizzards
                    fail = True
                    break
        
        if not fail:
            key = (nr, nc, stage, time%lcm)    #! Opt 1: time module state is equivalent to the board state due to cycling every LCM minutes

            if key in seen:
                continue

            seen.add(key)
            queue.append((time, nr, nc, stage))