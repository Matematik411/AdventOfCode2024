import sys
from utils.helpers import *
from functools import lru_cache
from collections import defaultdict

numeric_keypad = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}
directional_keypad = {"^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}


@lru_cache
def steps(combination, mode):
    if mode == "numeric":
        keypad = numeric_keypad
        empty = (3, 0)
    else:
        keypad = directional_keypad
        empty = (0, 0)

    steps = ""
    pos = keypad["A"]
    for button in combination:
        new_pos = keypad[button]
        dy = new_pos[0] - pos[0]
        dx = new_pos[1] - pos[1]

        if dy == 0:
            if dx > 0:
                steps += ">" * abs(dx)
            else:
                steps += "<" * abs(dx)

        elif dx == 0:
            if dy > 0:
                steps += "v" * abs(dy)
            else:
                steps += "^" * abs(dy)

        # both nonzero
        else:
            pos = list(pos)
            while pos != list(new_pos):
                # do <v >^ IS WRONG ... works for part 1 xD
                # -------------------
                # | but <v ^> IS OK | <-- trial and error after working code
                # -------------------

                # if we would end in empty space, we skip it first

                # <
                if dx < 0:
                    if (pos[0], pos[1] + dx) != empty:
                        steps += "<" * abs(dx)
                        pos[1] += dx
                        dx = 0
                # v
                if dy > 0:
                    if (pos[0] + dy, pos[1]) != empty:
                        steps += "v" * abs(dy)
                        pos[0] += dy
                        dy = 0

                # ^
                if dy < 0:
                    if (pos[0] + dy, pos[1]) != empty:
                        steps += "^" * abs(dy)
                        pos[0] += dy
                        dy = 0
                # >
                if dx > 0:
                    steps += ">" * abs(dx)
                    pos[1] += abs(dx)
                    dx = 0

        steps += "A"
        pos = new_pos

    return steps


def sol(pins, number_of_directionals):
    total = 0

    for pin in pins:
        steps_made = steps(pin, "numeric")
        parts = {p + "A": 1 for p in steps_made.split("A")[:-1]}

        for _ in range(number_of_directionals):
            new_parts = defaultdict(int)

            for part, val in parts.items():
                new_part = steps(part, "directional")
                for p in new_part.split("A")[:-1]:
                    new_parts[p + "A"] += val

            parts = new_parts

        str_val = 0
        for part, val in parts.items():
            str_val += len(part) * val

        price = int(pin[:-1]) * str_val
        total += price

    return total


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    # part1
    s1 = sol(file, 2)

    # part2
    s2 = sol(file, 25)
    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
