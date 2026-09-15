#
# test the code: python3 NEM.py < test.dat
# check the time: time python3 NEM.py < test.dat
# ! Opt 1: We dont need the amount of resources greater than the largest requirements for each robots
# ! Opt 2: The cache will be poisonous if we care about the remaining resources
import re

def dfs(bp,maxspend,cache,time,bots,amt):
    if time == 0:
        return amt[3]
    key = tuple([time, *bots, *amt])                        # len(key)=9
    if key in cache:
        return cache[key]
    
    maxval = amt[3] + bots[3]*time                          # do nothing in this step

    for btype, recipe in enumerate(bp):
        if btype != 3 and bots[btype] >= maxspend[btype]:               # ! Opt 1: we dont build excess bots
            continue
        # ! if we dont have enough, we will see how long we need to wait
        wait = 0
        # ! calculate the state if we take the path
        for ramt, rtype in recipe:
            if bots[rtype]==0:
                break
            wait = max(wait, -(-(ramt - amt[rtype])//bots[rtype]))       # get the ceiling number
        else:                                                            # if the for loop ends normally, it will go to else clauses
            remtime = time - wait - 1
            if remtime <= 0:
                continue
            bots_ = bots[:]
            amt_ = [x+y*(wait+1) for x, y in zip(amt,bots)]
            for ramt, rtype in recipe:
                amt_[rtype] -= ramt
            bots_[btype] += 1 
            for i in range(3):                                          # ! Opt 2: we throw any extra resources that we dont need, to bring states closer to 0
                amt_[i]=min(amt_[i],maxspend[i]*remtime)
            maxval = max(maxval, dfs(bp,maxspend,cache,remtime,bots_,amt_))

    cache[key] = maxval
    return maxval

total = 1

for line in list(open(0))[:3]:                # only care about cases 1 to 3
    bp = []                                                 # blue print              
    maxspend = [0,0,0]
    for section in line.strip().split(": ")[1].split(". "):
        recipe = []
        for x, y in re.findall(r"(\d+) (\w+)",section):     # find all "number space word" 
            x = int(x)
            y = ["ore", "clay", "obsidian"].index(y)
            recipe.append((x,y))
            maxspend[y] = max(maxspend[y],x)
        bp.append(recipe)
    v = dfs(bp,maxspend,{},32,[1,0,0,0],[0,0,0,0])
    total *= v
print("Answer to Part 2:",total)
# ! The code runs 34s for default implementation Cpython, but we can use Jpython or Pypy to speed up