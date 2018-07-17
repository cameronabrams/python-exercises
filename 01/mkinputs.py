# simple code to generate a 4-column, 10000-line file of "random" data
#
# cameron f abrams  cfa22@drexel.edu
#
import numpy as np

samps1 = np.random.normal(0.0,1.0,10000)
samps2 = np.random.poisson(2.5,10000)
samps3 = np.random.normal(0.0,5.0,10000)
samps4 = np.random.weibull(0.3,10000)

for i in range(10000) :
   print "{0:0.8f} {1:0.8f} {2:0.8f} {3:0.8f}".format(samps1[i],samps2[i],samps3[i],samps4[i])


