import sys
from utils.helpers import *

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def trailheads(map, y, x, current_h):
    h = len(map)
    w = len(map[0])

    if current_h == 9:
        return {(y, x)}

    upper = set()
    for i in range(4):
        y_new = y + dirs[i][0]
        x_new = x + dirs[i][1]

        if (0 <= y_new < h) and (0 <= x_new < w):
            if map[y_new][x_new] == current_h + 1:
                for r in trailheads(map, y_new, x_new, current_h + 1):
                    upper.add(r)

    return upper


def trailheads_part2(map, y, x, current_h):
    h = len(map)
    w = len(map[0])

    if current_h == 9:
        return 1

    upper = 0
    for i in range(4):
        y_new = y + dirs[i][0]
        x_new = x + dirs[i][1]

        if (0 <= y_new < h) and (0 <= x_new < w):
            if map[y_new][x_new] == current_h + 1:
                upper += trailheads_part2(map, y_new, x_new, current_h + 1)

    return upper


def sol(data):
    total1 = 0
    total2 = 0

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 0:
                total1 += len(trailheads(data, i, j, 0))
                total2 += trailheads_part2(data, i, j, 0)

    return total1, total2


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    # both parts
    s1, s2 = sol([[int(x) for x in r] for r in file])

    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
