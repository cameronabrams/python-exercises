# simple code to generate a 4-column, 10000-line file of "random" data
#
# cameron f abrams  cfa22@drexel.edu
#
import numpy as np
cnt=1048577
samps1 = np.random.normal(2.3,0.67,cnt)

for i in range(cnt) :
   print "{0:0.8f}".format(samps1[i])

