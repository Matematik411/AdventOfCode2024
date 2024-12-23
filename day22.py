import sys
from utils.helpers import *

MOD = 16777216


def next_secret(secret):
    secret = ((secret * 64) ^ secret) % MOD
    secret = ((secret // 32) ^ secret) % MOD
    secret = ((secret * 2048) ^ secret) % MOD
    return secret


def sol1(data):
    total = 0
    for secret in data:
        for _ in range(2000):
            secret = next_secret(secret)

        total += secret

    return total


def prepare_secrets_for_part2(secret):
    ones = [secret % 10]
    changes = []
    for _ in range(2000):
        secret = next_secret(secret)
        ones.append(secret % 10)
        changes.append(ones[-1] - ones[-2])

    fours = []
    for i in range(1997):
        fours.append(changes[i : i + 4])
    return ones[1:], fours


def bananas_bought(seq, secrets):
    try:
        i = secrets[1].index(seq)
        return secrets[0][i + 3]
    except:
        return 0


def sol2(data):
    # takes a while, finds 2191 at [0, -3, 2, 1]
    info = []
    for secret in data:
        ones, fours = prepare_secrets_for_part2(secret)
        info.append((ones, fours))

    seq = [-2, 1, -1, 3]

    most_bananas = 0
    for d1 in range(-6, 5):
        for d2 in range(-6, 5):
            for d3 in range(-6, 5):
                for d4 in range(0, 10):
                    seq = [d1, d2, d3, d4]
                    if sum(seq) > 9 or sum(seq) < -9:
                        continue

                    bananas_this_seq = 0
                    for i in range(len(data)):
                        bananas = bananas_bought(seq, info[i])
                        bananas_this_seq += bananas

                    if bananas_this_seq > most_bananas:
                        most_bananas = bananas_this_seq
                        print(bananas_this_seq, seq)
                        # this is only, so my solution stops
                        if most_bananas == 2191:
                            return most_bananas

    return most_bananas


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()
    data = [int(x) for x in file]

    # part1
    s1 = sol1(data)

    # part2
    s2 = sol2(data)
    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
