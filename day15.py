import sys
from utils.helpers import *

dirs = {"<": (0, -1), ">": (0, 1), "v": (1, 0), "^": (-1, 0)}


def nice_print(t):
    for r in t:
        print("".join(r))


def result_value(t):
    total = 0
    for i, r in enumerate(t):
        for j, el in enumerate(r):
            if el in "O[":
                total += 100 * i + j

    return total


def sol1(starting_position, grid, moves):

    # moving the crates
    loc = starting_position
    for step in moves:
        dir = dirs[step]
        next_loc = [loc[0] + dir[0], loc[1] + dir[1]]

        # just move
        if grid[next_loc[0]][next_loc[1]] == ".":
            loc = next_loc
            continue

        # stack crates...
        while grid[next_loc[0]][next_loc[1]] == "O":
            next_loc[0] += dir[0]
            next_loc[1] += dir[1]

        # ...and push them if there is space
        if grid[next_loc[0]][next_loc[1]] == "#":
            continue
        else:
            grid[next_loc[0]][next_loc[1]] = "O"
            grid[loc[0] + dir[0]][loc[1] + dir[1]] = "."
            loc = [loc[0] + dir[0], loc[1] + dir[1]]

    print("Final warehouse structure for part 1.")
    nice_print(grid)
    print(f"The robot ended in position {loc}.")

    return result_value(grid)


def sol2(starting_position, grid, moves):

    # moving the crates
    loc = starting_position
    for step in moves:
        dir = dirs[step]
        next_loc = (loc[0] + dir[0], loc[1] + dir[1])

        # just move
        if grid[next_loc[0]][next_loc[1]] == ".":
            loc = next_loc
            continue

        # left/right push is as before
        if step in "<>":
            crates = 0
            while grid[next_loc[0]][next_loc[1]] in "[]":
                next_loc = (next_loc[0] + dir[0], next_loc[1] + dir[1])
                crates += 1

            if grid[next_loc[0]][next_loc[1]] == "#":
                continue
            else:
                for k in range(crates + 1):
                    grid[next_loc[0] - k * dir[0]][next_loc[1] - k * dir[1]] = grid[
                        next_loc[0] - (k + 1) * dir[0]
                    ][next_loc[1] - (k + 1) * dir[1]]

                loc = (loc[0] + dir[0], loc[1] + dir[1])

        # up/down is more involved as crates are wider
        else:
            # create structure by levels of what needs to be pushed
            next_row = [next_loc]
            next_row_full = set()
            all_crates = {}
            blocked = False

            level = 0
            while True:
                if blocked:
                    break
                for pos in next_row:

                    el = grid[pos[0]][pos[1]]

                    if el == "[":
                        next_row_full.add(pos)
                        next_row_full.add((pos[0], pos[1] + 1))
                    elif el == "]":
                        next_row_full.add(pos)
                        next_row_full.add((pos[0], pos[1] - 1))
                    elif el == ".":
                        continue
                    elif el == "#":
                        # if a wall blocked the push, we stop and do nothing
                        blocked = True
                    else:
                        raise "moving crates part 2 error"

                # if there are no new crates to be added to the push queue
                # and if nothing is blocking the push
                # we push everything
                if len(next_row_full) == 0 and (not blocked):
                    # since we're rewriting with empty spaces, we start at the very last level
                    for l in range(level - 1, -1, -1):
                        for c in all_crates[l]:
                            grid[c[0] + dir[0]][c[1]] = grid[c[0]][c[1]]
                            grid[c[0]][c[1]] = "."
                    loc = (loc[0] + dir[0], loc[1] + dir[1])
                    break

                # there are more things to push, so we rearange our structures
                all_crates[level] = next_row_full
                level += 1
                next_row = [(x[0] + dir[0], x[1]) for x in next_row_full]
                next_row_full = set()

    print("Final warehouse structure for part 2.")
    nice_print(grid)
    print(f"The robot ended in position {loc}.")

    return result_value(grid)


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    w = len(file)

    # read data
    mode = 0
    grid = []
    moves = ""
    for r in file:
        if r == "":
            mode = 1
            continue
        if mode:
            moves += r
        else:
            grid.append([x for x in r])

    # expand data for part 2
    new_grid = []
    for r in grid:
        new_row = []
        for el in r:
            if el == "#":
                new_row += ["#", "#"]
            elif el == "O":
                new_row += ["[", "]"]
            elif el == ".":
                new_row += [".", "."]
            elif el == "@":
                new_row += ["@", "."]
            else:
                raise "building part 2 data error"
        new_grid.append(new_row)

    # set starting positions
    for i, r in enumerate(grid):
        for j, el in enumerate(r):
            if el == "@":
                starting = (i, j)
                grid[i][j] = "."

    for i, r in enumerate(new_grid):
        for j, el in enumerate(r):
            if el == "@":
                new_starting = (i, j)
                new_grid[i][j] = "."

    # call both solutions
    # part1
    s1 = sol1(starting, grid, moves)
    # part2
    s2 = sol2(new_starting, new_grid, moves)

    # print results
    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
