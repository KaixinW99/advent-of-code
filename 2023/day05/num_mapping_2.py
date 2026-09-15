#
# test the code: python3.10 num_mapping_2.py < input.txt
# check the time: time python3.10 num_mapping_2.py < input.txt


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
seeds_st_ran = list(map(int,re.findall("\d+",lines[0])))
seeds_st, seeds_ran = seeds_st_ran[::2], seeds_st_ran[1::2]

def mapping_func(mapping):
    mapping_prot = mapping.strip("\n").split("\n")[1:]
    return [list(map(int,run.split(" "))) for run in mapping_prot]

smallest_last_map = min(mapping_func(lines[-1]),key=lambda x: x[0])
if smallest_last_map[0] != 0:
    st = min(mapping_func(lines[-1]),key=lambda x: x[1])[1]
    smallest_last_map = [0,0,st]

def find_smallest_mapping(smallest_last_map):
    for obj_num in range(smallest_last_map[-1]):
        num = obj_num
        for mapping in lines[1:][::-1]:
            mapping_numb = mapping_func(mapping)
            for run in mapping_numb:
                des, sou, ran = run
                if des <= num <= des+ran-1:
                    num += sou-des
                    break
            else:
                num = num
        for st, ed in zip(seeds_st,seeds_ran):
            if st <= num < st+ed:
                return obj_num
print(find_smallest_mapping(smallest_last_map))