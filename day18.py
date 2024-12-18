import sys
from utils.helpers import *
from queue import Queue


dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def sol1(data, limit):

    w, h = 71, 71
    grid = [["." for _ in range(w)] for _ in range(h)]

    for r in data[:limit]:
        x, y = map(int, r.split(","))
        grid[y][x] = "#"

    visited = set()
    active = Queue(maxsize=0)

    active.put((0, 0, 0))

    while not active.empty():
        c = active.get()

        if (c[0], c[1]) == (70, 70):
            return c

        if (c[0], c[1]) in visited:
            continue

        visited.add((c[0], c[1]))

        for i in range(4):
            new_y = c[0] + dirs[i][0]
            new_x = c[1] + dirs[i][1]

            if (0 <= new_y < h) and (0 <= new_x < w):
                if grid[new_y][new_x] == "." and (new_y, new_x) not in visited:
                    active.put((new_y, new_x, c[2] + 1))

    return 0


def sol2(data):
    a = 1024
    b = 3450

    while True:
        if b - a == 1:
            return

        c = (a + b) // 2

        moving = sol1(data, c)
        print("attempt at", c, "has result", moving)

        if moving == 0:
            one_before = sol1(data, c - 1)
            if one_before:
                return data[c - 1]
            b = c
        else:
            a = c


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    # part1
    s1 = sol1(file, 1024)

    # part2
    s2 = sol2(file)
    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
