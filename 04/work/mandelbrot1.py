# mandelbrot set image generator
# 
# cameron f abrams 2018
# cfa22@drexel.edu
#
from PIL import Image
import sys

EPSILON = sys.float_info.epsilon  # smallest possible difference
# desired image dimensions in pixels; "r" real, "i" imaginary
def convert_to_rgb_cyclic ( minval, maxval, val, colors ):
    fi = float(val-minval) / float(maxval-minval) * (len(colors)+1)
    i = int(fi)
    f = fi - i
    if f < EPSILON:
        return colors[i%len(colors)]
    else:
        (r1, g1, b1), (r2, g2, b2) = colors[i%len(colors)], colors[(i+1)%len(colors)]
        return int(r1 + f*(r2-r1)), int(g1 + f*(g2-g1)), int(b1 + f*(b2-b1))

npr = 1201
npi = int((npr-1)/3.0*2.0) + 1

# lower-left and upper-right coordinates of image field
zll=(-2,-1)
zur=(1,1)

# a nice palette from iwanthue.com
c1=(122,164,87)
c2=(158,110,189)
c3=(203,103,81)
colors = [c1,c2,c3] 
# white, black
w=(255,255,255)
b=(0,0,0)

# create a new image
im = Image.new('RGB',(npr,npi))
print im.mode, im.size, im.format

# pixel dimensions
dr = float(zur[0]-zll[0])/(npr-1)
di = float(zur[1]-zll[1])/(npi-1)
print dr, di

# iteration limit
iterlim = 1000

# loop over each pixel
for i in range(npr):
   for j in range(npi):
     # construct the complex number at this point
     z = complex(zll[0]+i*dr,zll[1]+j*di)
     # check for boundedness of f(z)=z^2+c
     c = z
     niter = 0
     while abs(z) < 2 and niter < iterlim :
       z = pow(z,2)+c
       niter = niter + 1
     if niter == iterlim:
       im.putpixel((i,npi-j-1),b)
     else:
       im.putpixel((i,npi-j-1),convert_to_rgb_cyclic(0,iterlim/50,niter,colors))

drawgrid = 0
if drawgrid :
  gdx = float(zur[0]-zll[0])/(ngx-1)
  gdy = float(zur[1]-zll[1])/(ngy-1)
  for gx in range(ngx):
    draw.line(c2i((zll[0]+gx*gdx,zll[1]),zll,zur,npr,npi) + c2i((zll[0]+gx*gdx,zur[1]),zll,zur,npr,npi), fill=w)
    tic = "{0:.12f}".format(zll[0]+gx*gdx)
    plc = c2i((zll[0]+gx*gdx,zll[1]),zll,zur,npr,npi-20)
    draw.text(plc,tic,font=fnt,fill=w)
  for gy in range(ngy):
    tic = "{0:.12f}".format(zll[1]+gy*gdy)
    draw.line(c2i((zll[0],zll[1]+gy*gdy),zll,zur,npr,npi) + c2i((zur[0],zll[1]+gy*gdy),zll,zur,npr,npi), fill=w)
    draw.text(c2i((zll[0],zll[1]+gy*gdy),zll,zur,npr,npi),tic,font=fnt,fill=w)

im.save('tmp.png')

