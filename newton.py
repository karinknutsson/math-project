x = [4, 5, 7, 10, 11, 13]
y0 = []
z = 1


def divide(y0, y1, x0, x1):
    #print("y0: " + str(y0))
    #print("y1: " + str(y1))
    #print("x0: " + str(x0))
    #print("x1: " + str(x1))

    return (y1 - y0) / (x1 - x0)


def newton(y):
    global z

    y0.append(y[0])

    print(y)

    if (len(y) == 1):
        return y

    new_y = []

    for i in range(0, len(y) - 1):
        #new_y.append((y[i + 1] - y[i]) / (x[i + 1] - x[i]))
        new_y.append(divide(y[i], y[i + 1], x[i], x[i + z]))

    z += 1

    newton(new_y)


y = [48, 100, 294, 900, 1210, 2028]

print(newton(y))
print(y0)
