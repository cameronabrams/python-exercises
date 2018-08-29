# mandelbrot set image generator
# 
# cameron f abrams 2018
# cfa22@drexel.edu
#
from PIL import Image, ImageDraw, ImageFont
from math import log
import sys

EPSILON = sys.float_info.epsilon  # smallest possible difference
def convert_to_rgb_cyclic ( minval, maxval, val, colors ):
    fi = float(val-minval) / float(maxval-minval) * (len(colors)+1)
    i = int(fi)
    f = fi - i
    if f < EPSILON:
        return colors[i%len(colors)]
    else:
        (r1, g1, b1), (r2, g2, b2) = colors[i%len(colors)], colors[(i+1)%len(colors)]
        return int(r1 + f*(r2-r1)), int(g1 + f*(g2-g1)), int(b1 + f*(b2-b1))


def c2i ( pt, cll, cur, Lx, Ly ):
   rx = float(pt[0]-cll[0]) / float(cur[0]-cll[0])
   ix = int(rx*Lx)
   ry = float(cur[1]-pt[1]) / float(cur[1]-cll[1])
   iy = int(ry*Ly)
   return ix, iy

npr = 1201
npi = 801
#npr = 301
#npi = 201

zll=(-2,-1)
zur=(1,1)

#zll=(-0.875,0)
#zur=(-0.5,0.25)

#zll=(-0.875,0.21875)
#zur=(-0.828125,0.25)

c1=(122,164,87)
c2=(158,110,189)
c3=(203,103,81)
c1=(197,124,60)
c2=(171,98,192)
c3=(114,165,85)
c4=(202,86,112)
c5=(99,140,204)
w=(255,255,255)
b=(0,0,0)
colors = [c1,c2,c3,c4,c5,w] 

im = Image.new('RGB',(npr,npi))
print im.mode, im.size, im.format
draw = ImageDraw.Draw(im)
drawgrid = 0
ngx = 9
ngy = 9
fnt = ImageFont.truetype('/usr/share/fonts/truetype/OpenSans-Regular.ttf',12)

dr = float(zur[0]-zll[0])/(npr-1)
di = float(zur[1]-zll[1])/(npi-1)
print dr, di

iterlim = 1000

for i in range(npr):
   for j in range(npi):
     z = complex(zll[0]+i*dr,zll[1]+j*di)
     c = z
     niter = 0
     while abs(z) < 2 and niter < iterlim :
       z = pow(z,2) + c
       niter = niter + 1
     if niter == iterlim:
       im.putpixel((i,npi-j-1),b)
     else:
       #log_zn=log ( z.real*z.real+z.imag*z.imag ) / 2
       #nu = log ( log_zn / log(2) ) / log(2)
       #niter = niter + 1 - nu
       #im.putpixel((i,npi-j-1),convert_to_rgb_cyclic(0,1.0,niter%1,colors))
       im.putpixel((i,npi-j-1),convert_to_rgb_cyclic(0,iterlim/50,niter,colors))

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

