import sys
from utils.helpers import *

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def sol1(data):
    loc = (0, 0)
    dir = 0
    obstacles = set()
    for i, row in enumerate(data):
        for j, el in enumerate(row):
            if el == "^":
                loc = (i, j)
            if el == "#":
                obstacles.add((i, j))

    h = len(data)
    w = len(data[0])

    visited = set()
    while (0 <= loc[0] < h) and (0 <= loc[1] < w):
        visited.add(loc)

        next = (loc[0] + dirs[dir][0], loc[1] + dirs[dir][1])
        if next in obstacles:
            dir = (dir + 1) % 4
        else:
            loc = next

    return len(visited)


def is_looped(data, x, y):
    loc = (0, 0)
    dir = 0
    obstacles = set()
    for i, row in enumerate(data):
        for j, el in enumerate(row):
            if el == "^":
                loc = (i, j)
            if el == "#":
                obstacles.add((i, j))
    if loc != (y, x):
        obstacles.add((y, x))

    h = len(data)
    w = len(data[0])

    visited = [set() for _ in range(4)]
    while (0 <= loc[0] < h) and (0 <= loc[1] < w):
        if loc in visited[dir]:
            return True
        visited[dir].add(loc)

        next = (loc[0] + dirs[dir][0], loc[1] + dirs[dir][1])
        if next in obstacles:
            dir = (dir + 1) % 4
        else:
            loc = next

    return False


def sol2(data):
    total2 = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if is_looped(data, j, i):
                total2 += 1

    return total2


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    # part1
    s1 = sol1(file)
    print(f"Part one: {s1}")

    # # part2
    s2 = sol2(file)
    print(f"Part two: {s2}")
