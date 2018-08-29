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

Also shown in this figure is the concept of the "complex conjugate" ![](.README-images/complexconjugate.png).  One of the rules about arithmetic operations on complex numbers is that _squaring_ a complex number means multiplying it by its own complex conjugate:

![](.README-images/complex-square.png)

Note that this quantity has no imaginary component, and its square root (by Pythagoras) is just the length of the vector ![](.README-images/z.png).

Our goal in this assignment is not to become experts in complex variables, but instead to explore one of their more famous representations and learn a little more Python programming.   

The thing we will examine here is a particular curve that lives in the complex plane.  This curve is special because it marks the boundary enclosing a special set of complex numbers called the Mandelbrot set, after the mathematician Benoit Mandelbrot.  A complex number ![](.README-images/c.png), is in the Mandelbrot set if the sequence ![](.README-images/mand_seq.png) does not "blow up" (i.e., approach infinity), where

![](.README-images/mand_f.png).

In this exercise, we will write a two versions of a program that will generate a PNG image showing the Mandelbrot set.  As we will see, this curve that separates numbers in the set from those not in the set is _extremely_ complicated. In one version, we will color points in the set black and points not in the set white.  In the second version, we will use a more complicated scheme to choose what color to set points that are outside the set, based on how many iterations of the the function above are required to "know" the point is not in the set.

## Programming Concepts

This exercise demonstrates several concepts:
1.  Image creation and pixel-by-pixel manipulation;
2.  Nested looping;
3.  Complex numbers in NumPy; and
4.  Functions.


