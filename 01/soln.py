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
for line in fileinput.input():
    x = float(line)
    tally_x += x
    tally_xx += x*x
    count+=1

mean = tally_x/count
stdev = sqrt((tally_xx - 1.0/count*tally_x*tally_x)/count)
print 'Average {0:.5f} Stdev {1:.5f}'.format(mean,stdev)
print 'Program ends.'
