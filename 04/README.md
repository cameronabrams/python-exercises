# Python Exercise 4:  Image creation and complex numbers via the Mandelbrot set

Cameron F. Abrams, `cfa22@drexel.edu`

2018

## Introduction

Complex numbers play important roles in  many branches of physics and engineering analysis.  Briefly, a complex number ![](.README-images/z.png) has two components, a "real" component ![](.README-images/x.png), and an "imaginary" component ![](.README-images/y.png), and is expressed as

![](.README-images/complex.png)

where the symbol ![](.README-images/i.png) stands for ![](.README-images/sqrtminusone.png).  
The "complex plane" is a 2-D coordinate system 
oriented with the real axis R horizontal and the imaginary axis I vertical;
in this plane, any complex number ![](.README-images/z.png) can be 
thought of as a vector from the origin to the point ![](.README-images/xy.png):

![](.README-images/complex-plane-fig.png)

Also shown in this figure is the "complex conjugate" ![](complexconjugate.png).  _Squaring_ a complex number means multiplying it by itself:

![](.README-images/complex-square.png)

and the magnitude (or absolute value) of a complex number is the square root of the product of the number and its complex conjugate:

![](.README-images/absolutevalue.png).

Our goal in this assignment is not to become experts in complex variables, but instead to explore one of their more famous representations and learn a little more Python programming. The thing we will examine here is a particular curve that lives in the complex plane.  This curve is special because it marks the boundary enclosing a special set of complex numbers called the Mandelbrot set, after the mathematician Benoit Mandelbrot.  A complex number ![](.README-images/c.png) is in the Mandelbrot set if the sequence ![](.README-images/mand_seq.png) does not "blow up" (i.e., approach infinity), where

![](.README-images/mand_f.png).

In this exercise, we will write a two versions of a program that will generate a PNG image showing the Mandelbrot set.  As we will see, this curve that separates numbers in the set from those not in the set is _extremely_ complicated. In one version, we will color points in the set black and points not in the set white.  In the second version, we will use a more complicated scheme to choose what color to set points that are outside the set, based on how many iterations of the the function above are required to "know" the point is not in the set.

## Programming Concepts

This exercise demonstrates several concepts:
1.  Nested looping;
2.  Functions;
3.  Complex number data types; and 
4.  Image creation and pixel-by-pixel manipulation.

## The Assignment

1.  Write a python program that loops over a field of pixels of with W and height H (such that W = (3/2)H) that corresponds to a region in the complex plane with the point (-2,-1) at the lower-left and the point (1,1) at the upper right.  At each pixel, determine the real and imaginary components of the complex number at that location, and print the number, its square, and its absolute value. (Note that python uses `j` to refer to ![](.README-images/i.png).)  Use the program `seed.py` provided here, which implements a loop over all WxH pixels.  The first few lines of this output looks like this
```
(-2+1j) (3-4j) 2.2360679775
(-2+0.996661101836j) (3.00666664809-3.98664440735j) 2.23457677244
(-2+0.993322203673j) (3.01331099969-3.97328881469j) 2.23308956388
(-2+0.989983305509j) (3.01993305481-3.95993322204j) 2.23160635982
(-2+0.986644407346j) (3.02653281345-3.94657762938j) 2.23012716825
(-2+0.983305509182j) (3.03311027561-3.93322203673j) 2.22865199715
(-2+0.979966611018j) (3.03966544129-3.91986644407j) 2.22718085451
(-2+0.976627712855j) (3.04619831048-3.90651085142j) 2.22571374833
(-2+0.973288814691j) (3.0527088832-3.89315525876j) 2.22425068659
(-2+0.969949916528j) (3.05919715943-3.87979966611j) 2.22279167728
```

2. Write a function that accepts a single complex number and returns the number of iterations of the function above before the magnitude of the results exceeds 2.  Call this function for each point you visit in Part 1 and report the result for each point.

3. Import the `Image` module from the `PIL` (python image library), and create an 'RGB'-mode image of WxH pixels.  At each pixel in the loop, use the `putpixel` function to color the pixel black if the point is in the set and white otherwise.  After the loop, save the image in 'my_bw.png'.

The image below was created with H = 600.

![](my_bw.png)

4. Write a function that accepts a single floating point value, the values of its minimum and maximum range, and a list of triples, each of which is a color of your choosing in RGB format. The colors are assumed to correspond to equally spaced positions in this range, and the range is cyclic.  The function should use the value to determine an interpolated RGB triple between the two nearest input RGB triples.  This is a "palette".  Now, use this function to choose the color for each pixel, and make a new image 'my_color.png'

The image below was created using the followed ordered color palette:
```
# white in RGB
w=(255,255,255)
# a nice palette from iwanthue.com
c1=(197,124,60)
c2=(171,98,192)
c3=(114,165,85)
c4=(202,86,112)
c5=(99,140,204)
colors = [c1,c2,c3,c4,c5,w]
```
and using 0 for the minimum number of iterations and 50 for the maximum in the cyclic domain; the value used to select the palette color is the number of iterations modulo 50.

![](my_color.png)
