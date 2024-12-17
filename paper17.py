results = [2, 4, 1, 3, 7, 5, 4, 0, 1, 3, 0, 3, 5, 5, 3, 0]
building = results[::-1]
print("we need the solution to be:", building)

results = [("0", building)]

print("all starting numbers that give the correct solution")


while results:
    result, to_do = results.pop()

    if to_do == []:
        print(result)
        continue

    for n in range(8):
        n = str(bin(n))[2:]
        n = "0" * (3 - len(n)) + n
        N = int(result + n, 2)

        b = N % 8
        b = b ^ 3
        c = N // (2**b)

        b = b ^ c
        b = b ^ 3

        if (b % 8) == to_do[0]:

            results.append((result + n, to_do[1:]))
