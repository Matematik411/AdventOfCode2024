import sys
from utils.helpers import *
from collections import defaultdict


def sol(data):
    part1 = 0

    numbers = defaultdict(int)
    for n in data:
        numbers[n] += 1

    for i in range(75):
        # part1 ends after 25 rounds
        if i == 25:
            part1 = sum([x for x in numbers.values()])

        new_numbers = defaultdict(int)
        for n, ap in numbers.items():
            if n == 0:
                new_numbers[1] += ap

            elif len(str(n)) % 2 == 0:
                d = len(str(n))
                half = int(d / 2)
                left = int(str(n)[:half])
                right = int(str(n)[half:])
                new_numbers[left] += ap
                new_numbers[right] += ap

            else:
                new_numbers[n * 2024] += ap

        numbers = new_numbers

    return part1, sum([x for x in numbers.values()])


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    data = list(map(int, file[0].split()))

    # both parts part2
    s1, s2 = sol(data)

    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
