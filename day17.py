import sys
from utils.helpers import *
import math


def sol():
    starting_string = "2,4,1,3,7,5,4,0,1,3,0,3,5,5,3,0"
    starting_number = [51342988, 108107574778365]

    for i in range(2):
        registers = [starting_number[i], 0, 0]
        ops = list(map(int, starting_string.split(",")))

        solution = intcomputer(registers, ops)

        if i == 0:
            print(f"Part one: {solution}")

        else:
            print(f"Part two solution really is: {solution}")
            print(f"Part two: {starting_number[i]}")


def intcomputer(registers, ops):
    outputs = []

    i = 0
    while 0 <= i < len(ops):
        op = ops[i]
        val = ops[i + 1]

        if op == 0:
            num = registers[0]
            if val >= 4:
                val = registers[val - 4]
            den = 2**val
            sol = int(num / den)
            registers[0] = sol
            i += 2

        elif op == 1:
            sol = registers[1] ^ val
            registers[1] = sol
            i += 2

        elif op == 2:
            if val >= 4:
                val = registers[val - 4]
            sol = val % 8
            registers[1] = sol
            i += 2

        elif op == 3:
            if registers[0]:
                i = val
            else:
                i += 2

        elif op == 4:
            sol = registers[1] ^ registers[2]
            registers[1] = sol
            i += 2

        elif op == 5:
            if val >= 4:
                val = registers[val - 4]
            sol = val % 8
            outputs.append(sol)
            i += 2

        elif op == 6:
            num = registers[0]
            if val >= 4:
                val = registers[val - 4]
            den = 2**val
            sol = int(num / den)
            registers[1] = sol
            i += 2

        elif op == 7:
            num = registers[0]
            if val >= 4:
                val = registers[val - 4]
            den = 2**val
            sol = int(num / den)
            registers[2] = sol
            i += 2

        else:
            raise "wrong command"

    result = ",".join([str(x) for x in outputs])

    return result


def sol2(data):
    pass

    return 2


if __name__ == "__main__":

    # both parts
    sol()
