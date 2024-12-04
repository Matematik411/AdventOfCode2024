import sys
from utils.helpers import *


def count_hor(data):
    result = 0
    data_hor = [[x for x in r] for r in data]

    for i in range(len(data_hor)):
        for j in range(len(data_hor[0]) - 3):
            if data_hor[i][j : j + 4] == [x for x in "XMAS"]:
                result += 1

    return result


def rotate_90(data):
    new_data = [[0 for _ in range(len(data))] for _ in range(len(data[0]))]
    for i in range(len(data)):
        for j in range(len(data[0])):
            new_data[j][len(data) - i - 1] = data[i][j]
    return new_data


def diag_search(data):
    result = 0
    for i in range(len(data) - 3):
        for j in range(len(data[0]) - 3):
            word = [
                data[i][j],
                data[i + 1][j + 1],
                data[i + 2][j + 2],
                data[i + 3][j + 3],
            ]

            if word == [x for x in "XMAS"]:
                result += 1

    return result


def find_x(data):
    result = 0
    for i in range(len(data) - 2):
        for j in range(len(data[0]) - 2):
            all = True
            if data[i][j] != "M":
                all = False
            if data[i + 2][j] != "M":
                all = False
            if data[i][j + 2] != "S":
                all = False
            if data[i + 2][j + 2] != "S":
                all = False
            if data[i + 1][j + 1] != "A":
                all = False

            if all:
                result += 1
    return result


def sol1(data):
    total = 0
    total2 = 0

    # normal
    data_0 = [[x for x in r] for r in data]
    total += count_hor(data_0)
    total += diag_search(data_0)
    total2 += find_x(data_0)

    # # rotate 90 deg - vertical reverse
    data_1 = rotate_90(data_0)
    total += count_hor(data_1)
    total += diag_search(data_1)
    total2 += find_x(data_1)

    # # rotate 90 deg - horizontal reverse
    data_2 = rotate_90(data_1)
    total += count_hor(data_2)
    total += diag_search(data_2)
    total2 += find_x(data_2)

    # # rotate 90 deg - vertical
    data_3 = rotate_90(data_2)
    total += count_hor(data_3)
    total += diag_search(data_3)
    total2 += find_x(data_3)

    return total, total2


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    # part1
    s1, s2 = sol1(file)

    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
