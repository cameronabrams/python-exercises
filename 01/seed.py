#
# Seed code for Exercise 1:  Computing averages and standard deviations
#
# This program computes the column-wise averages from a datafile
# with an arbitrary number of parallel columns of data of arbitrary length
#
# The accompanying file 'data1' is an example of this format
# 
# Run this program at the command-line:
# 
# % python seed.py data1
#
# cameron f abrams
# cfa22@drexel.edu
# (c) 2018
# drexel university
#

import fileinput
import string
import numpy as np

count = 0
# read each line of input from the file named in the first argument
for line in fileinput.input():
    # split the line into an array of fields
    lst=line.split(" ");
    # if this is the first line, set up the accumulator 'sum'
    # note that the number of elements in sum is the number of
    # elements in 'lst', which should be the number of columns
    # in the file
    if count == 0 :
        nf = len(lst);
        sum = np.zeros(nf)
    # add elements in this line to the tallies; note the type conversion
    # to float
    i=0
    for x in lst[:] :
       sum[i]+=float(x)
       i+=1

    count+=1

for i in range(nf):
    sum[i]/=count

print 'Averages:',
for i in range(nf):
    print ' {0:.5f}'.format(sum[i]),
print
print 'Program ends.'
