# Solution to Exercise 04 Part 2
# 
# cameron f abrams 2018
# cfa22@drexel.edu
#
def isInIter ( z, iterlim ) :
    c = z
    niter = 0
    while abs(z) < 2 and niter < iterlim :
        z = pow(z,2) + c
        niter = niter + 1
    return niter

H = 600
W = int(H/2.0*3.0)

# lower-left and upper-right coordinates of
# image region in the complex plane
zll=complex(-2,-1)
zur=complex(1,1)

# pixel dimensions
dr = float(zur.real - zll.real)/(W-1)
di = float(zur.imag - zll.imag)/(H-1)

# loop over each pixel
for i in range(W):
   for j in range(H):
     # construct the complex number at this point
     z = complex(zll.real+i*dr,zur.imag-j*di)
     # check for boundedness of f(z)=z^2+c
     print z,isInIter(z,1000)
