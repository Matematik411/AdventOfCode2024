import sys
from utils.helpers import *
from collections import defaultdict
import functools

pairs = defaultdict(list)


def elf_compare(x, y):
    if x in pairs and y in pairs[x]:
        return -1
    return 0


def sol1(data):
    end = 0
    for i, r in enumerate(data):
        if r == "":
            end = i
            break
        l, r = map(int, r.split("|"))
        pairs[l].append(r)

    total = 0
    total2 = 0
    for r in data[end + 1 :]:
        numbers = list(map(int, r.split(",")))
        elf_sorted = sorted(numbers, key=functools.cmp_to_key(elf_compare))

        # part1 counts already sorted
        if numbers == elf_sorted:
            total += numbers[len(numbers) // 2]

        # part2 sorts the unsorted and counts after the sorting
        else:
            total2 += elf_sorted[len(numbers) // 2]

    return total, total2


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    # part1
    s1, s2 = sol1(file)

    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
