# Solution to Exercise 06:  Random and Self-Avoiding Random Walks in 3D
#
# Cameron F Abrams
# cfa22@drexel.edu
# 
# 2018

from math import acos, asin, pi, cos, sin, sqrt
from numpy.random import random, seed
import numpy as np
import sys
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

# generate a 3-D displacement of length R that points
# in a random direction
def random_step ( R ) :
    # get random number [-pi:pi] for angle phi
    phi=pi*(1-2*random(1))
    cphi=cos(phi)
    sphi=sin(phi)
    # get random number [-1:1] for cos(theta)
    ctheta=1-2*random(1)
    theta=acos(ctheta)
    stheta=sin(theta)
    # compute the cartesian coordinate displacements
    # to move a distance R along the (theta,phi) 
    # direction
    x=R*stheta*cphi
    y=R*stheta*sphi
    z=R*ctheta
    # return the vector displacement
    return np.array([x, y, z])

# check to see if the trial position is within a distance 
# 'size' from any position in the 'path' of length 'time'
def collides ( trial, path, time, size ) :
    collision=0
    i = 0
    while i <= time and not collision :
        dist=np.linalg.norm(path[i]-trial)
        if dist<size :
            collision=1
        i = i + 1
    return collision

def selfavoid_step ( R, path, i, size ) :
    tstep=random_step(R)
    tposn=np.add(path[i],tstep)
    maxtries=1000
    ntries=0
    while collides(tposn,path,i,size) and ntries < maxtries :
        tstep=random_step(R)
        tposn=np.add(path[i],tstep)
        ntries = ntries + 1
    if ntries == maxtries :
        print "Could not find next step"
        exit()
    return tstep

# default values
myseed = 1234 # random-number generator seed
stepsize = 1.0
nsteps = 100
nwalkers = 5
sasize = 0.7 # self-avoiding random-walk particle size

# argument-list handling
i=1
while i < len(sys.argv):
    if sys.argv[i] == '-seed':
        myseed = int(sys.argv[i+1])
        i = i + 1
    elif sys.argv[i] == '-stepsize':
        stepsize = float(sys.argv[i+1])
        i = i + 1
    elif sys.argv[i] == '-nsteps':
        nsteps = int(sys.argv[i+1])
        i = i + 1
    elif sys.argv[i] == '-nwalkers':
        nwalkers = int(sys.argv[i+1])
        i = i + 1
    elif sys.argv[i] == '-sasize':
        sasize = float(sys.argv[i+1])
        i = i + 1
    else:
        print "Argument {0:s} not recognized".format(sys.argv[i])
    i = i + 1

print "Seed = {0:d}".format(myseed)
print "Step size = {0:.3f}".format(stepsize)
print "Number of steps per walk = {0:d}".format(nsteps)
print "Number of walkers = {0:d}".format(nwalkers)
print "Self-avoiding walk particle size = {0:.2f}".format(sasize)

# seed the random-number generator
seed(myseed)

# define the origin
origin=np.array([0,0,0])
# allocate arrays for the random walker and self-avoiding walkers
rwalkers=np.zeros((nwalkers,nsteps+1,3))
sawalkers=np.zeros((nwalkers,nsteps+1,3))
# allocate arrays for the end-to-end distances
rdist=np.zeros((nwalkers,nsteps+1))
sadist=np.zeros((nwalkers,nsteps+1))
# allocate array for the time
time=np.arange(0,nsteps+1)

# perform each walk in sequence
for w in range(nwalkers) :
    print "Walker {0:d}...".format(w)
    # begin this walk at the origin
    rwalkers[w,0]=origin
    sawalkers[w,0]=origin
    # grow each walk
    for i in range(nsteps) :
        # add this step to the walk
        rwalkers[w,i+1]=np.add(rwalkers[w,i],random_step(stepsize))
        sawalkers[w,i+1]=np.add(sawalkers[w,i],selfavoid_step(stepsize,sawalkers[w],i,sasize))
        # measure end-to-end distancce for this step
        rdist[w,i+1]=np.linalg.norm(rwalkers[w,i+1]-origin)
        sadist[w,i+1]=np.linalg.norm(sawalkers[w,i+1]-origin)

# average all walk end-to-end distances together, stepwise
ardist=np.zeros(nsteps+1)
asadist=np.zeros(nsteps+1)
for i in range(nsteps+1) :
    ardist[i]=0.0
    asadist[i]=0.0
    for w in range(nwalkers) :
        ardist[i]+=rdist[w,i]
        asadist[i]+=sadist[w,i]
    ardist[i] /= nwalkers
    asadist[i] /= nwalkers

# plot results
x=np.logspace(np.log10(stepsize),np.log10(nsteps),100)
y=pow(x,0.5)
y2=pow(x,0.6)

plt.plot(time,ardist,'b-',label="Random")
plt.plot(x,y,'b--',label="x^0.5")
plt.plot(time,asadist,'r-',label="Self-avoiding")
plt.plot(x,y2,'r--',label="x^0.6")

plt.xlabel('number of steps')
plt.ylabel('average cartesian distance of walker to origin')
plt.legend()
#plt.yscale('log')
#plt.xscale('log')
plt.show()

