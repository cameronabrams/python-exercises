# Solution to Exercise 06, Question 2:  Draw multiple 3D 
# random walks and plot average end-to-end distance
# as a function of contour length
#
# Cameron F Abrams
# cfa22@drexel.edu
# 
# 2018

from math import acos, asin, pi, cos, sin, sqrt
from numpy.random import random, seed
import numpy as np
import sys
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
mpl.use("TkAgg")
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

# default values
myseed = 1234 # random-number generator seed
stepsize = 1.0
nsteps = 100
nwalkers = 5

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
    else:
        print "Argument {0:s} not recognized".format(sys.argv[i])
    i = i + 1

print "Seed = {0:d}".format(myseed)
print "Step size = {0:.3f}".format(stepsize)
print "Number of steps per walk = {0:d}".format(nsteps)
print "Number of walkers = {0:d}".format(nwalkers)

# seed the random-number generator
seed(myseed)

# define the origin
origin=np.array([0,0,0])
# allocate arrays for the random walker and self-avoiding walkers
rwalker=np.zeros((nwalkers,nsteps+1,3))
for w in range(nwalkers) :
    rwalker[w,0]=origin
    for i in range(nsteps) :
        # add this step to the walk
        rwalker[w,i+1]=np.add(rwalker[w,i],random_step(stepsize))

dist=np.zeros(nsteps+1)
for w in range(nwalkers) :
    for i in range(nsteps+1) :
        dist[i]=dist[i]+np.linalg.norm(rwalker[w,i]-origin)

time=np.zeros(nsteps+1)
for i in range(nsteps+1) :
    dist[i]/=nwalkers
    time[i]=i

# colors as a random palette from iwanthue.com
#color=["#c9578c","#50ac72","#8675ca","#9b9d3f","#c96840"]
#color=["#bf5d39","#934acd","#668e43","#b84a84","#6574bd"]
color=["#b460bd",
        "#5db852",
        "#6a7ecd",
        "#d09634",
        "#4eb7a1",
        "#d15237",
        "#597c3a",
        "#c9587a",
        "#a7b149",
        "#b37749"]
nc=np.shape(color)
# plot results
e2e=np.zeros((nwalkers,2,3))
fig = plt.figure(figsize=plt.figaspect(0.5))
fig.suptitle('{0:d} random walks of length {1:d} steps'.format(nwalkers,nsteps))
lim=2*int(sqrt(nsteps+1))
ax = fig.add_subplot(1,2,1,projection='3d')
ax.set_xlim((-lim,lim))
ax.set_ylim((-lim,lim))
ax.set_zlim((-lim,lim))
for w in range(nwalkers) :
    c=color[np.mod(w,int(nc[0]))]
    ax.plot(rwalker[w,:,0],rwalker[w,:,1],rwalker[w,:,2],c=c,lw=0.3)

ex=0.485
ax.scatter(0,0,0,c='r',marker='o')
ax = fig.add_subplot(1,2,2)
ax.set_xlabel('number of steps $n$')
ax.set_ylabel('end-to-end distance $d$')
ax.plot(time,dist,label='walks')
ax.plot(time,np.power(time,ex),label='$d(n)=n^{0.485}$')
ax.legend()
plt.show()

