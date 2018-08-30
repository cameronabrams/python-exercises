# simple code to generate a 4-column, 10000-line file of "random" data
#
# cameron f abrams  cfa22@drexel.edu
#
import numpy as np
cnt=349526
samps1 = np.random.normal(2.3,0.67,cnt)
samps2 = np.random.normal(-1.2,0.44,cnt)
samps3 = np.random.normal(3.7,0.85,cnt)

for i in range(cnt) :
   print "{0:0.8f}".format(samps1[i])
   print "{0:0.8f}".format(samps2[i])
   print "{0:0.8f}".format(samps3[i])

