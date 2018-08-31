# simple code to generate a 3-column, 349526-line file of "random" data
#
# cameron f abrams  cfa22@drexel.edu
#
import numpy as np
cnt=349526
samps1 = np.random.normal(-2.7,0.37,cnt)
samps2 = np.random.normal(1.8,0.94,cnt)
samps3 = np.random.normal(3.4,0.75,cnt)

for i in range(cnt) :
    print "{0:0.8f} {1:0.8f} {2:0.8f}".format(samps1[i],samps2[i],samps3[i])

