import sys
from utils.helpers import *
from queue import Queue
from collections import defaultdict

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# first solution
def sol1(grid, starting, ending):
    h = len(grid)
    w = len(grid[0])

    # first do reverse bfs
    visited = set()
    active = Queue()
    active.put((ending, [ending]))
    while not active.empty():
        c, p = active.get()

        if c in visited:
            continue

        if c == starting:
            best_path = p

        visited.add(c)
        grid[c[0]][c[1]] = len(p) - 1

        for i in range(4):
            new_pos = (c[0] + dirs[i][0], c[1] + dirs[i][1])
            if grid[new_pos[0]][new_pos[1]] in [".", "S"]:
                active.put((new_pos, p + [new_pos]))

    # now check for each dir, if wall is thin enough, then cross it
    # and save the jump in jumps set (I could also only take note of the
    # large enough [>= 100] jumps)
    jumps = defaultdict(set)
    for p in best_path[::-1]:
        for i in range(4):

            # skip length
            max_skip = 2
            wall_len = 0
            for skip in range(1, max_skip):
                between = (p[0] + skip * dirs[i][0], p[1] + skip * dirs[i][1])
                if (0 <= between[0] < h) and (0 <= between[1] < w):
                    if grid[between[0]][between[1]] == "#":
                        wall_len = skip
                    else:
                        break

            # if there is no wall, we go to next dir
            if wall_len == 0:
                continue
            new_pos = (
                p[0] + (wall_len + 1) * dirs[i][0],
                p[1] + (wall_len + 1) * dirs[i][1],
            )

            if (0 <= new_pos[0] < h) and (0 <= new_pos[1] < w):
                a = grid[p[0]][p[1]]
                b = grid[new_pos[0]][new_pos[1]]
                if b != "#":
                    diff = a - b
                    if diff > 0:
                        jumps[diff - wall_len - 1].add(p)

    total = 0
    for k, v in jumps.items():
        if k >= 100:
            total += len(v)
    return total


# better second solution
def generate_circle(center, radius, h, w):
    points = []
    for dy in range(-radius, radius + 1):
        for dx in range(-(radius - abs(dy)), (radius - abs(dy)) + 1):
            p = (center[0] + dy, center[1] + dx)
            if (0 <= p[0] < h) and (0 <= p[1] < w):
                points.append(p)
    return points


def sol2(grid, starting, ending, max_cheat):
    h = len(grid)
    w = len(grid[0])

    # first do reverse bfs
    visited = set()
    active = Queue()
    active.put((ending, [ending]))
    while not active.empty():
        c, p = active.get()

        if c in visited:
            continue

        if c == starting:
            best_path = p

        visited.add(c)
        grid[c[0]][c[1]] = len(p) - 1

        for i in range(4):
            new_pos = (c[0] + dirs[i][0], c[1] + dirs[i][1])
            if grid[new_pos[0]][new_pos[1]] in [".", "S"]:
                active.put((new_pos, p + [new_pos]))

    # now check all the points in the cirlce, if they make a jump
    jumps = defaultdict(set)
    for p in best_path[::-1]:
        # for up to max_skip seconds, use cheat => no walls
        all_points = generate_circle(p, max_cheat, h, w)

        for q in all_points:
            val = grid[q[0]][q[1]]
            if val != "#":
                one_dist = abs(q[0] - p[0]) + abs(q[1] - p[1])
                if grid[p[0]][p[1]] - val - one_dist > 0:

                    # a unique cheat is characterised with
                    # - starting point
                    # - end point
                    jumps[grid[p[0]][p[1]] - val - one_dist].add((p, q))

    total = 0
    for k, v in jumps.items():
        if k >= 100:
            total += len(v)
    return total


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    h = len(file)
    w = len(file[0])
    grid = [[e for e in r] for r in file]
    for i, r in enumerate(grid):
        if "S" in r:
            starting_pos = (i, r.index("S"))
        if "E" in r:
            ending_pos = (i, r.index("E"))

    # sol1 only works for part1, as it can't make turns in the cheat_mode
    s1_first = sol1([[e for e in r] for r in grid], starting_pos, ending_pos)

    # sol2 is correct, works for both parts
    s1 = sol2([[e for e in r] for r in grid], starting_pos, ending_pos, 2)
    # part2
    s2 = sol2([[e for e in r] for r in grid], starting_pos, ending_pos, 20)
    print(f"Part one (first solution): {s1_first}")
    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
