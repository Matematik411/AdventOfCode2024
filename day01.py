import sys
from utils.helpers import *


def sol(data):
    left = []
    right = []

    i = 0
    while i < len(data):
        x, y = map(int, data[i].split())
        left.append(x)
        right.append(y)
        i += 1

    leftS = sorted(left)
    rightS = sorted(right)
    p1 = 0
    p2 = 0

    for i in range(len(left)):
        # part 1
        p1 += abs(leftS[i] - rightS[i])
        # part 2
        p2 += left[i] * len([x for x in right if x == left[i]])

    return p1, p2


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    # part1
    s1, s2 = sol(file)

    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
