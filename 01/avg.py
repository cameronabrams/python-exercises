# avg.py -- computes the column-wise average and standard deviation of a datafile
# with an arbitrary number of parallel columns of data
# 
# an exercise in learning python
#
# cameron f abrams
# cfa22@drexel.edu
# (c) 2017
# drexel university
#
from math import sqrt # so we can use math functions without "math.*"
import fileinput # can only use fileinput functions with "fileinput.*"
#import sys
import string
import numpy as np

count = 0
for line in fileinput.input():
    # split the line into an array of fields
    lst = line.split(" ");
    # if this is the first line, set up the accumulators
    if count == 0 :
        nf = len(lst);
        sum = np.zeros(nf)
        sum2 = np.zeros(nf)
    i = 0
    for x in lst[:] :
       sum[i] += float(x)
       sum2[i] += float(x)*float(x)
       i+=1

    count += 1

for i in range(nf):
    sum[i] /= count
    sum2[i] = sqrt((sum2[i] - sum[i]*sum[i]/count)/count)

print 'Averages:',
for i in range(nf):
    print ' {0:.5f}'.format(sum[i]),
print
print 'Std. Devs.:',
for i in range(nf):
    print ' {0:.5f}'.format(sum2[i]),
print

