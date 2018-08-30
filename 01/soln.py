# Solution to Exercise 01
# 
# cameron f abrams
# cfa22@drexel.edu
# (c) 2018
# drexel university
#
from math import sqrt 
import fileinput

count = 0
tally_x = 0.0
tally_xx = 0.0
min_x = 1.e99
max_x = -1.e99
for line in fileinput.input():
    x = float(line)
    if x < min_x :
        min_x = x
    if x > max_x :
        max_x = x
    tally_x += x
    tally_xx += x*x
    count+=1

mean = tally_x/count
stdev = sqrt((tally_xx - 1.0/count*tally_x*tally_x)/count)
print 'Average {0:.5f} Minimum {1:.5f} Maximum {2:.5f} Stdev {3:.5f}'.format(mean,min_x,max_x,stdev)
print 'Program ends.'
