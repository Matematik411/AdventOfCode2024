import sys
from utils.helpers import *


def sol1(data):
    file_id = 0
    odd = 1
    start_data = []
    empty_spaces = {}
    full_spaces = []

    for c in data:
        c = int(c)

        if odd:
            if c:
                full_spaces.append((len(start_data), c))
            start_data += [file_id for _ in range(c)]
            file_id += 1

        else:
            empty_spaces[len(start_data)] = c
            start_data += [-1 for _ in range(c)]

        odd = 1 - odd

    return part1([x for x in start_data]), part2(
        [x for x in start_data], empty_spaces, full_spaces
    )


def part1(start_data):
    last_pos = len(start_data) - 1
    checksum = 0

    # does moving and calculating in one loop
    for i, n in enumerate(start_data):
        if n == -1:
            if i >= last_pos:
                break

            start_data[i] = start_data[last_pos]
            start_data[last_pos] = -1

            checksum += start_data[i] * i
            while start_data[last_pos] == -1:
                last_pos -= 1

        else:
            checksum += n * i

    return checksum


def part2(data, empty, full):
    # takes a few seconds

    # move whole files in reverse order, only attempting once per file
    for f in full[::-1]:
        pos, size = f
        for i in range(pos):
            space = empty.get(i, 0)
            if space:
                if space >= size:

                    # swap in list
                    for j in range(size):
                        data[i + j] = data[pos + j]
                        data[pos + j] = -1

                    empty[i] = 0
                    if space > size:
                        empty[i + size] = space - size

                    break

    # calculate checksum
    checksum = 0
    for i, n in enumerate(data):
        if n != -1:
            checksum += n * i

    return checksum


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    # part1
    s1, s2 = sol1(file[0])

    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
