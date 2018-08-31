# Solution to Exercise 02
# 
# cameron f abrams
# cfa22@drexel.edu
# (c) 2018
# drexel university
#
from math import sqrt 
import fileinput
import numpy as np

ncol = 3
count = 0
tally_x = np.zeros(ncol)
tally_xx = np.zeros(ncol)
min_x = np.full(ncol,1.e99) 
max_x = np.full(ncol,-1.e99)
for line in fileinput.input():
    xc = line.split(" ")
    for i in range(ncol):
      x = float(xc[i])
      tally_x[i]+=x;
      tally_xx[i]+=x*x;
      if x<min_x[i]:
	min_x[i]=x
      if x>max_x[i]:
	max_x[i]=x
    count+=1

mean = tally_x/count
stdev = np.sqrt((tally_xx - np.multiply(tally_x,tally_x)/count)/count)
print "{0:d} data read in.".format(count)
for i in range(ncol):
   print "----------------"
   print "Column {0:d}:".format(i)
   print "    Mean {0:.5f}".format(mean[i])
   print "   StDev {0:.5f}".format(stdev[i])
   print "     Min {0:.5f}".format(min_x[i])
   print "     Max {0:.5f}".format(max_x[i])
print 'Program ends.'
