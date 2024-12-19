import sys
from utils.helpers import *
from collections import defaultdict
from functools import lru_cache

av_by_len = defaultdict(set)

@lru_cache()
def can_make_count(to_make):

    if to_make == "":
        return 1
    
    ways_to_make = 0
    for l, towels in av_by_len.items():
        if len(to_make) >= l:
            if to_make[:l] in towels:
                amount = can_make_count(to_make[l:])
                ways_to_make += amount
    
    return ways_to_make



def sol(patterns):
    total1 = 0
    total2 = 0
    for p in patterns:
        amount = can_make_count(p)
        
        total1 += 1 if amount else 0
        total2 += amount


    return total1, total2


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    available = file[0].split(", ")
    for a in available:
        av_by_len[len(a)].add(a)
    to_make = file[2:]
    

    # both parts
    s1, s2 = sol(to_make)

    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
