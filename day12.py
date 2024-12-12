import sys
from collections import defaultdict
from utils.helpers import *

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def calc_perimeter(points):
    perimeter = 0

    # calculate perimeter by counting sides that don't have a neighbour
    for p in points:
        for i in range(4):
            new_p = (p[0] + dirs[i][0], p[1] + dirs[i][1])
            if new_p not in points:
                perimeter += 1

    return perimeter


def calc_perimeter2(points):
    horizontal = defaultdict(list)
    vertical = defaultdict(list)

    for p in points:

        for i in range(4):
            new_p = (p[0] + dirs[i][0], p[1] + dirs[i][1])
            if new_p not in points:

                # add +-1/4 so that left/right and up/down don't overlap
                if i % 2 == 0:
                    horizontal[p[0] + (dirs[i][0] / 4)].append(p[1])
                else:
                    vertical[p[1] + (dirs[i][1] / 4)].append(p[0])

    # then also need to calculate how many sections are seperated
    # this gives us the number of sides for each line
    hor_sides = 0
    for fixed, moving in horizontal.items():
        moving = sorted(moving)
        diffs = [moving[i + 1] - moving[i] for i in range(len(moving) - 1)]
        diffs = [x for x in diffs if x > 1]
        hor_sides += len(diffs) + 1

    ver_sides = 0
    for fixed, moving in vertical.items():
        moving = sorted(moving)
        diffs = [moving[i + 1] - moving[i] for i in range(len(moving) - 1)]
        diffs = [x for x in diffs if x > 1]
        ver_sides += len(diffs) + 1

    return hor_sides + ver_sides


def sol(data):
    total1 = 0
    total2 = 0

    visited = set()
    h = len(data)
    w = len(data[0])

    for start_i in range(h):
        for start_j in range(w):
            # do dfs to find each connected area and mark it as visited

            starting = (start_i, start_j)
            if starting in visited:
                continue

            letter = data[starting[0]][starting[1]]
            active = [starting]
            this_area = []
            while active:
                current = active.pop()

                if current in visited:
                    continue

                this_area.append(current)
                visited.add(current)

                for i in range(4):
                    new_pos = (current[0] + dirs[i][0], current[1] + dirs[i][1])

                    if (
                        (0 <= new_pos[0] < h)
                        and (0 <= new_pos[1] < w)
                        and data[new_pos[0]][new_pos[1]] == letter
                    ):
                        active.append(new_pos)

            # calculate area and two different perimeters and add their product to the result
            area = len(this_area)
            perimeter1 = calc_perimeter(set(this_area))
            perimeter2 = calc_perimeter2(set(this_area))

            total1 += area * perimeter1
            total2 += area * perimeter2

    return total1, total2


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    # both parts
    s1, s2 = sol(file)
    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
