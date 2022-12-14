from pylab import array, linspace, subplots
from ddeint import ddeint
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def model(Y, t, d):
    x, y = Y(t)
    xd, yd = Y(t - d)
    return array([0.5 * x * (1 - yd), -0.5 * y * (1 - xd)])


g = lambda t: array([1, 2])
tt = linspace(2, 30, 20000)
plt.figure()
fig, ax = subplots(1, figsize=(4, 4))


for d in [0, 0.2, 0.3]:
    print("Computing for d=%.02f" % d)
    yy = ddeint(model, g, tt, fargs=(d,))
    # WE PLOT X AGAINST Y
    ax.plot(yy[:, 0], yy[:, 1], lw=2, label="delay = %.01f" % d)
plt.legend()

ax.figure.savefig("lotka.jpeg")
plt.show()