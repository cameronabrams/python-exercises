# Python Exercise 2:  Working with large datafiles (part 2)

Cameron F. Abrams, `cfa22@drexel.edu`

2018

## Introduction

In this exercise, you will learn how to handle large data files with more than one element on each line.  The file `data3` provided here has three columns of "random" data, and we will compute the average of each column independently.

## Programming Concepts

In addition to fileinput, this exercise also illustrates the use of _arrays_.  The NumPy library provides (among a _lot_ of other things) a lot of functions for manipulating arrays.  To access them, a convenient way is to `import` it:
```
import numpy as np
```

You will read each line of the file, convert it to an array of numbers, and then use them to update a corresponding array of tallies.  (It will be assumed that every line has the same number of elements.)  This will look like this:  

```
tally = np.zeros(3)
for line in fileinput.input():
  tally += line.split(" ")
```
Here, `tally` is a 3-element array the that NumPy `zeros` function creates and initializes with zeros.  The `line.split(" ")` call returns ..


## The Assignment

