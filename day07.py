import sys
from utils.helpers import *


def calc(target, numbers, partial, part2=False):
    if numbers == []:
        return partial == target

    if partial > target:
        return False

    a = calc(target, numbers[1:], partial + numbers[0], part2)
    b = calc(target, numbers[1:], partial * numbers[0], part2)

    if part2:
        c = calc(target, numbers[1:], int(str(partial) + str(numbers[0])), part2)
        return (a or b) or c
    else:
        return a or b


def sol(data):
    total = 0
    total2 = 0

    for r in data:
        res, others = r.split(":")
        v = int(res)
        args = list(map(int, others.strip().split()))

        check = calc(v, args[1:], args[0])
        check2 = calc(v, args[1:], args[0], True)

        if check == True:
            total += v
        if check2:
            total2 += v

    return total, total2


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    # part1

    s1, s2 = sol(file)

    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
