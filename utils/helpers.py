# auxiliary functions


def very_useful_function(arg):
    return arg


def rotate_90(data):
    new_data = [[0 for _ in range(len(data))] for _ in range(len(data[0]))]
    for i in range(len(data)):
        for j in range(len(data[0])):
            new_data[j][len(data) - i - 1] = data[i][j]
    return new_data


def nice_print(t):
    for r in t:
        print("".join([str(x) for x in r]))


def generate_circle(center, radius, h, w):
    points = []
    for dy in range(-radius, radius + 1):
        for dx in range(-(radius - abs(dy)), (radius - abs(dy)) + 1):
            p = (center[0] + dy, center[1] + dx)
            if (0 <= p[0] < h) and (0 <= p[1] < w):
                points.append(p)
    return points
