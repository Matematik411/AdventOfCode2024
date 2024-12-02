import sys
from utils.helpers import *


def sol1(data):
    pass

    return 1


def sol2(data):
    pass

    return 2


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    print(file)

    # part1
    s1 = sol1(file)

    # part2
    s2 = sol2(file)
    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
