# Seed code for Exercise 04 Part 1 
# 
# cameron f abrams 2018
# cfa22@drexel.edu
#
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
       print i,j,i*dr+zll.real,zur.imag-j*di
       # code here to construct a complex number and square it
