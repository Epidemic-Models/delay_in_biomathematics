from pylab import array, linspace, subplots
from ddeint import ddeint
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

def model(x, t, d, a):
  return a*x(t)*(1-x(t-d))

g = lambda t : 0.1
tt = np.linspace(0,50,1000)

yy = ddeint(model,g,tt,fargs=(1, 1))
# WE PLOT X AGAINST Y
plt.figure()
plt.plot(tt, yy, lw=2,label="delay = %.01f")
plt.legend()# display the legend
plt.show()