# Solution to Exercise 04 Part 2
# 
# cameron f abrams 2018
# cfa22@drexel.edu
#
from PIL import Image

def my_palette ( val, minv, maxv, colors ) :
    fi = float(val-minv) / float(maxv-minv)*(len(colors)+1)
    i = int(fi)
    f = fi - i
    if f < 1.e-6:
        return colors[i%len(colors)]
    else:
        (r1, g1, b1), (r2, g2, b2) = colors[i%len(colors)], colors[(i+1)%len(colors)]
        return int(r1+f*(r2-r1)),int(g1+f*(g2-g1)),int(b1+f*(b2-b1))

def isInIter ( z, iterlim ) :
    c = z
    niter = 0
    while abs(z) < 2 and niter < iterlim :
        z = pow(z,2) + c
        niter = niter + 1
    return niter

H = 600
W = int(H/2.0*3.0)

# create new image
im = Image.new('RGB',(W,H))
# black in RGB
b=(0,0,0)
# white in RGB
w=(255,255,255)
# a nice palette from iwanthue.com
c1=(197,124,60)
c2=(171,98,192)
c3=(114,165,85)
c4=(202,86,112)
c5=(99,140,204)
colors = [c1,c2,c3,c4,c5,w]

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
     iterc=isInIter(z,1000)
     if iterc < 1000 :
         im.putpixel((i,H-j-1),my_palette(iterc,0,20,colors))
     else:
         im.putpixel((i,H-j-1),b)

im.save('my_color.png')
