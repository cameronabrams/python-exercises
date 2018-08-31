# Solution to Exercise 01
# 
# cameron f abrams
# cfa22@drexel.edu
# (c) 2018
# drexel university
#
from math import sqrt 
import fileinput
import numpy as np

count = 0
tally_x = np.zeros(3)
tally_xx = np.zeros(3)
min_x = np.full(3,1.e99) 
max_x = np.full(3,-1.e99)
for line in fileinput.input():
    x = [float(i) for i in line.split(" ")]
    tally_x += x
    tally_xx += np.multiply(x,x)
# below doesn't work: np.greater is an array of truth values!
    if np.greater(x,max_x):
        max_x = x
    if np.less(x,min_x):
        min_x = x
    count+=1

mean = tally_x/count
stdev = np.sqrt((tally_xx - np.multiply(tally_x,tally_x)/count)/count)
print mean
print stdev
print max_x
print min_x

print 'Program ends.'
