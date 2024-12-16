import sys
from utils.helpers import *
from queue import PriorityQueue

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def sol(grid, loc):
    # start facing EAST
    start_dir = 1

    # set up things for dijkstra
    # but without "visited = set()" because of part 2
    pq = PriorityQueue(maxsize=0)
    pq.put((0, loc, start_dir, [loc]))

    # for part 2, we end after we have score larger than the best finished path
    best_score = 0
    steps_in_best_paths = set()

    # because we need ALL the best paths, we keep score of best score at each position
    in_paths = {}

    while not pq.empty():
        c = pq.get()

        val, pos, dir, steps = c

        # end condition
        if best_score and val > best_score:
            break

        # pretty hacky here
        # distance can be 1000 if the 2nd path comes from different direction
        # this worked so I didn't look further
        if (pos in in_paths) and (val - in_paths[pos]) not in [0, 1000]:
            continue

        # set best score for the position if not set yet
        if pos not in in_paths:
            in_paths[pos] = val

        # check if we're in the wall or at the end
        el = grid[pos[0]][pos[1]]
        if el == "#":
            continue
        elif el == "E":
            # save best score and all the positions we went through
            best_score = val
            for p in steps:
                steps_in_best_paths.add(p)

        # move in the grid
        for i in range(4):
            if (i - dir) % 4 == 2:
                continue
            next_pos = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])

            new_val = val + ((i - dir) % 2) * 1000 + 1

            if grid[next_pos[0]][next_pos[1]] in ".E":
                pq.put((new_val, next_pos, i, steps + [next_pos]))

    return best_score, len(steps_in_best_paths)


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    for i, r in enumerate(file):
        if "S" in r:
            starting_loc = (i, r.index("S"))

    # both parts
    s1, s2 = sol(file, starting_loc)

    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
