import sys
from utils.helpers import *
import re


def which_quadrant(w, h, x, y):
    if x < (w // 2) and y < (h // 2):
        return 0
    elif x > (w // 2) and y < (h // 2):
        return 1
    elif x < (w // 2) and y > (h // 2):
        return 2
    elif x > (w // 2) and y > (h // 2):
        return 3
    else:
        return -1


def nice_print(t):
    for r in t:
        print("".join(r))


def find_long_connected_row(t, N):
    for r in t:
        if r.count("#") > N:
            pos = [i for i, el in enumerate(r) if el == "#"]
            diffs = [pos[i] - pos[i - 1] for i in range(len(pos) - 1)]

            if diffs.count(1) > N:
                return True

    return False


def sol1(data):
    w, h = 11, 7  # test input
    w, h = 101, 103
    robots = []
    speeds = []
    for row in data:
        pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
        x, y, dx, dy = map(int, re.findall(pattern, row)[0])
        robots.append([x, y])
        speeds.append((dx, dy))

    quadrants = [0 for _ in range(4)]

    steps = 100
    for i in range(len(robots)):
        final_x = (robots[i][0] + steps * speeds[i][0]) % w
        final_y = (robots[i][1] + steps * speeds[i][1]) % h

        q = which_quadrant(w, h, final_x, final_y)
        if q >= 0:
            quadrants[q] += 1

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def sol2(data):
    w, h = 11, 7  # test input
    w, h = 101, 103
    robots = []
    speeds = []
    for row in data:
        pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
        x, y, dx, dy = map(int, re.findall(pattern, row)[0])
        robots.append([x, y])
        speeds.append((dx, dy))

    steps_per_move = 1
    total_steps = 0
    while total_steps < 10000:
        picture = [["." for _ in range(w)] for _ in range(h)]
        for i in range(len(robots)):
            final_x = (robots[i][0] + steps_per_move * speeds[i][0]) % w
            final_y = (robots[i][1] + steps_per_move * speeds[i][1]) % h

            robots[i] = [final_x, final_y]
            picture[final_y][final_x] = "#"

        total_steps += steps_per_move
        if find_long_connected_row(picture, 15):
            nice_print(picture)
            print(total_steps)
            break

        if total_steps % 1000 == 0:
            nice_print(picture)
            print(total_steps)

    return total_steps


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    # # part1
    s1 = sol1(file)

    # part2
    s2 = sol2(file)
    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
