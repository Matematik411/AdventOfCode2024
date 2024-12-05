import sys
from utils.helpers import *
from collections import defaultdict


def check_order(rules, nrs):
    for i in range(len(nrs) - 1):
        on_right = nrs[i + 1 :]

        allowed = rules[nrs[i]]
        for k in on_right:
            if k not in allowed:
                return False

    return True


def correctly_order(rules, nrs):
    # this assumes there is exactly one way to sort the nrs
    new_numbers = []
    while nrs:
        for n in nrs:
            others = [x for x in nrs if x != n]
            needed = [x for x in rules[n] if (x in others)]
            if [x for x in needed if x not in new_numbers] == []:
                new_numbers.append(n)
                nrs.remove(n)
                break

    return new_numbers[len(new_numbers) // 2]


def sol1(data):
    pairs = defaultdict(list)
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

        good = check_order(pairs, numbers)

        # part1 counts already sorted
        if good:
            total += numbers[len(numbers) // 2]

        # part2 sorts the unsorted and counts after the sorting
        else:
            total2 += correctly_order(pairs, set(numbers))

    return total, total2


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    # part1
    s1, s2 = sol1(file)

    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
