# Solution to Exercise 03
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

count = 0
xmin = -10.0
xmax = 10.0
dx = 0.1

nb=int((xmax-xmin)/dx)
hist = np.zeros(nb)
bins = np.zeros(nb)
for line in fileinput.input():
    x = float(line)
    i = int((x-xmin)/dx)
    if i>=0 and i<nb:
       hist[i] += 1
    count+=1
for i in range(nb):
    bins[i]=xmin+i*dx

plt.bar(bins,hist,dx)
plt.title('My Histogram')
plt.ylabel('H(x)')
plt.xlabel('x')
plt.xlim([-10,10])
plt.savefig("my-hist.png")
plt.show()
print 'Program ends.'

