import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from pylab import array, linspace, subplots
from ddeint import ddeint


def model(x, t, d, a, b, n):
    return ((b * x(t-d))/((x(t-d))**n+1))-a*x(t)

g = lambda t : 0.1
tt = np.linspace(0, 800, 1000)

yy = ddeint(model, g, tt, fargs=(22, 0.1, 0.2, 10))
# WE PLOT X AGAINST Y
plt.figure()
plt.plot(tt, yy, "r", lw=2, label="delay = %.01f")

plt.legend()# display the legend
plt.show()
