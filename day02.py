import sys
from utils.helpers import *


def sol(data):
    safe1 = 0
    safe2 = 0

    for r in data:
        row = list(map(int, r.split()))

        good = False
        if row == sorted(row) or row == sorted(row, reverse=True):
            good = True
            for i in range(len(row) - 1):
                if abs(row[i] - row[i + 1]) > 3:
                    good = False
                if row[i] == row[i + 1]:
                    good = False
            if good:
                safe1 += 1
                safe2 += 1

        # for part 2, we remove 1 and check if the new row is good for any case
        for rem in range(len(row)):
            if good:
                break
            this_row = row[:rem] + row[rem + 1 :]
            good = False
            if this_row == sorted(this_row) or this_row == sorted(
                this_row, reverse=True
            ):
                good = True
                # print(this_row)
                for i in range(len(this_row) - 1):
                    if abs(this_row[i] - this_row[i + 1]) > 3:
                        good = False
                    if this_row[i] == this_row[i + 1]:
                        good = False
                if good:
                    safe2 += 1

    return safe1, safe2


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    # part2
    s1, s2 = sol(file)

    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
