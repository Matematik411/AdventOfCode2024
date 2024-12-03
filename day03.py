import sys
import re
from utils.helpers import *


def sol1(data):
    sum = 0

    for r in data:
        res = r"mul\((\d{1,3}),(\d{1,3})\)"
        hits = re.findall(res, r)
        for h in hits:
            sum += int(h[0]) * int(h[1])

    return sum


def sol2(data):
    sum = 0

    enabled = True
    for r in data:
        res = r"mul\((\d{1,3}),(\d{1,3})\)|(don't\(\))|(do\(\))"
        hits = re.findall(res, r)
        for h in hits:
            if h[3] == "do()":
                enabled = True
            elif h[2] == "don't()":
                enabled = False
            elif enabled:
                sum += int(h[0]) * int(h[1])

    return sum


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    # part1
    s1 = sol1(file)

    # part2
    s2 = sol2(file)
    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
