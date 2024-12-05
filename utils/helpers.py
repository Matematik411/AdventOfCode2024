# auxiliary functions


def very_useful_function(arg):
    return arg


def rotate_90(data):
    new_data = [[0 for _ in range(len(data))] for _ in range(len(data[0]))]
    for i in range(len(data)):
        for j in range(len(data[0])):
            new_data[j][len(data) - i - 1] = data[i][j]
    return new_data
