import sys
from utils.helpers import *
from collections import defaultdict

antennas = defaultdict(list)
antinodes1 = set()
antinodes2 = set()


def sol(data):
    for i, row in enumerate(data):
        for j, el in enumerate(row):
            if el != ".":
                antennas[el].append((i, j))
                antinodes2.add((i, j))

    h = len(data)
    w = len(data[0])

    for _, locs in antennas.items():
        for k in range(len(locs)):
            for l in range(k + 1, len(locs)):
                point1 = locs[k]
                point2 = locs[l]
                move_vector1 = (point1[0] - point2[0], point1[1] - point2[1])
                move_vector2 = (point2[0] - point1[0], point2[1] - point1[1])

                # part 1 ... only one vector move
                antinode1 = (point1[0] + move_vector1[0], point1[1] + move_vector1[1])
                antinode2 = (point2[0] + move_vector2[0], point2[1] + move_vector2[1])
                if (0 <= antinode1[0] < h) and (0 <= antinode1[1] < w):
                    antinodes1.add(antinode1)
                if (0 <= antinode2[0] < h) and (0 <= antinode2[1] < w):
                    antinodes1.add(antinode2)

                # part 2 ... as many as are inside the grid
                while (0 <= antinode1[0] < h) and (0 <= antinode1[1] < w):
                    antinodes2.add(antinode1)
                    antinode1 = (
                        antinode1[0] + move_vector1[0],
                        antinode1[1] + move_vector1[1],
                    )
                while (0 <= antinode2[0] < h) and (0 <= antinode2[1] < w):
                    antinodes2.add(antinode2)
                    antinode2 = (
                        antinode2[0] + move_vector2[0],
                        antinode2[1] + move_vector2[1],
                    )

    return len(antinodes1), len(antinodes2)


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    # both parts
    s1, s2 = sol(file)

    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
