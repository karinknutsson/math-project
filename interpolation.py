from divided_difference import *

def interpolation(a, x, newton_base):
    total = a[0]
    for i in range(1, len(a)):
        multiplier = 1
        for j in range(0, i + 1):
            multiplier *= x - newton_base[j]

        total += a[i] * multiplier

    return total

get_divided_difference(y)

print(interpolation(a, 10, x))
