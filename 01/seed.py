#
# Seed code for Exercise 1:  Computing averages and standard deviations
#
# This program computes the average from a datafile
# with one number per line
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

count = 0
tally = 0.0
# read each line of input from the file named in the first argument
for line in fileinput.input():
  # convert the character string input in `line` to a floating-point, and 
  # tally it
  tally += float(line)
  # update the count of values tallied
  count += 1

# divide the tally by the count to get the average
tally /= count

print 'Average: {0:.5f}'.format(tally)
print 'Program ends.'
