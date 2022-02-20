import numpy as np
import matplotlib.pyplot as plt
from interpolation import *
from divided_difference import *

newton_base = [4, 5, 7, 10, 11, 13]

plt.ylabel('y values')
plt.xlabel('x values')

get_divided_difference(y)

x_axis = np.linspace(-1000, 1000, 1000)
plt.plot(x_axis, interpolation(a, x_axis, newton_base))
plt.grid()
plt.show()
