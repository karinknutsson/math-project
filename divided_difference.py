newton_base = [4, 5, 7, 10, 11, 13]
a = []
z = 1


def divide(y0, y1, x0, x1):
    return (y1 - y0) / (x1 - x0)


def get_divided_difference(y):
    global z

    a.append(y[0])

    if (len(y) == 1):
        return

    new_y = []
    for i in range(0, len(y) - 1):
        new_y.append(divide(y[i], y[i + 1], newton_base[i], newton_base[i + z]))

    z += 1

    get_divided_difference(new_y)


y = [48, 100, 294, 900, 1210, 2028]
