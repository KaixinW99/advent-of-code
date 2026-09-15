#
# test the code: python3.10 num_mapping_1.py < input.txt
# check the time: time python3.10 num_mapping_1.py < input.txt


# too slow
"""
import re
lines = open(0).read().split("\n\n")
seeds = map(int,re.findall("\d+",lines[0]))
for mapping in lines[1:]:
    mapping_prot = mapping.split("\n")[1:]
    mapping_numb = [list(map(int,run.split(" "))) for run in mapping_prot]
    mapping_dict = dict()
    for run in mapping_numb:
        des, sou, ran = run
        for stp in range(ran):
            mapping_dict[sou]=des
            sou += 1
            des += 1
    seeds = [mapping_dict.get(num,num) for num in seeds]
print(min(seeds))
"""

import re
lines = open(0).read().split("\n\n")
seeds = map(int,re.findall("\d+",lines[0]))
for mapping in lines[1:]:
    mapping_prot = mapping.strip("\n").split("\n")[1:]
    #print(mapping_prot)
    mapping_numb = [list(map(int,run.split(" "))) for run in mapping_prot]
    new_seeds = []
    for num in seeds:
        for run in mapping_numb:
            des, sou, ran = run
            if sou <= num <= sou+ran-1:
                new_seeds.append(des-sou+num)
                break
        else:
            new_seeds.append(num)
    seeds=new_seeds
print(min(seeds))
