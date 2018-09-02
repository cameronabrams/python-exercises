# Solution to Exercise 06:  Random and Self-Avoiding Random Walks in 3D
#
# Cameron F Abrams
# cfa22@drexel.edu
# 
# 2018

from math import acos, asin, pi, cos, sin, sqrt
from numpy.random import random, seed
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

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
    return np.array([x, y, z])

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
#    print "at ({0:.3f},{1:.3f},{2:.3f})".format(path[i][0],path[i][1],path[i][2])
    tstep=random_step(R)
    tposn=np.add(path[i],tstep)
    maxtries=100
    ntries=0
    while collides(tposn,path,i,size) and ntries < maxtries :
        tstep=random_step(R)
        tposn=np.add(path[i],tstep)
        ntries = ntries + 1
    if ntries == maxtries :
        print "Could not find next step"
        exit()
    return tstep

seed(1234)
nsteps=10000
nwalkers=20
sasize=0.5
origin=np.array([0,0,0])

rwalkers=np.zeros((nwalkers,nsteps+1,3))
sawalkers=np.zeros((nwalkers,nsteps+1,3))
rdist=np.zeros((nwalkers,nsteps+1))
sadist=np.zeros((nwalkers,nsteps+1))
time=np.arange(0,nsteps+1)

for w in range(nwalkers) :
    print "Walker {0:d}...".format(w)
    rwalkers[w,0]=origin
    sawalkers[w,0]=origin
    for i in range(nsteps) :
        rwalkers[w,i+1]=np.add(rwalkers[w,i],random_step(1.0))
#        print "   Step {0:d}...".format(i+1)
        sawalkers[w,i+1]=np.add(sawalkers[w,i],selfavoid_step(1.0,sawalkers[w],i,sasize))
        thisrdist=np.linalg.norm(rwalkers[w,i+1]-origin)
        rdist[w,i+1]=thisrdist
        thissadist=np.linalg.norm(sawalkers[w,i+1]-origin)
        sadist[w,i+1]=thissadist

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

#print time
#print adist
plt.plot(time,ardist,label="Random")
plt.plot(time,asadist,label="Self-avoiding")
plt.xlabel('number of steps')
plt.ylabel('average cartesian distance of walker to origin')
plt.legend()
plt.show()

