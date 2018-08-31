# Solution to Exercise 03: Using NumPy Histogram()
# 
# cameron f abrams
# cfa22@drexel.edu
# (c) 2018
# drexel university
#
from math import sqrt 
import fileinput
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

xmin = -10.0
xmax = 10.0
dx = 0.1

nb = int((xmax-xmin)/dx)
plt.hist([float(i) for i in fileinput.input()],bins=nb,range=(xmin,xmax))
plt.title('NumPy Hist()')
plt.ylabel('H(x)')
plt.xlabel('x')
plt.xlim([xmin,xmax])
plt.savefig("numpy-hist.png")
plt.show()
print 'Program ends.'

