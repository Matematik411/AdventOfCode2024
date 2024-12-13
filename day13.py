import sys
from utils.helpers import *
import re
import numpy as np


def sol1_math(data, part2):
    i = 0
    total = 0
    while True:
        try:
            row = data[i]
        except:
            break

        pattern = r".*X\+(.*), Y\+(.*)"
        adx, ady = map(int, re.findall(pattern, row)[0])
        i += 1
        row = data[i]
        pattern = r".*X\+(.*), Y\+(.*)"
        bdx, bdy = map(int, re.findall(pattern, row)[0])
        i += 1
        row = data[i]
        pattern = r".*X=(.*), Y=(.*)"
        sx, sy = map(int, re.findall(pattern, row)[0])
        i += 2

        if part2:
            sx += 10000000000000
            sy += 10000000000000

        # solve linear system with numpy !
        A = np.array([[adx, bdx], [ady, bdy]])
        b = np.array([sx, sy])
        x = np.linalg.solve(A, b)

        # solutions need to be integers and there can be small calculation errors so x will never have exact integers
        x1 = int(np.round(x[0]))
        x2 = int(np.round(x[1]))
        if (sx == x1 * adx + x2 * bdx) and (sy == x1 * ady + x2 * bdy):
            if part2:
                total += 3 * x1 + x2
            else:
                if x1 <= 100 and x2 <= 100:
                    total += 3 * x1 + x2

    return total


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    # part1
    s1 = sol1_math(file, False)

    # part2
    s2 = sol1_math(file, True)
    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
