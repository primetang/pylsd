pylsd
=============

###1. Introduction

pyflann is the python bindings for [FLANN - Fast Library for Approximate Nearest Neighbors](http://www.cs.ubc.ca/research/flann/).

#####Please feel free to contact me [tanggefu@gmail.com] if you have any questions.

###2. Install

This package uses distutils, which is the default way of installing python modules. To install in your home directory, securely run the following:
```
git clone https://github.com/primetang/pyflann.git
cd pyflann
[sudo] python setup.py install
```

Or directly through `pip` to install it:
```
[sudo] pip install pyflann
```

###3. Usage

Use it just like the following code:
```python
from pyflann import *
import numpy as np

dataset = np.array(
    [[1., 1, 1, 2, 3],
     [10, 10, 10, 3, 2],
     [100, 100, 2, 30, 1]
     ])
testset = np.array(
    [[1., 1, 1, 1, 1],
     [90, 90, 10, 10, 1]
     ])
flann = FLANN()
result, dists = flann.nn(
    dataset, testset, 2, algorithm="kmeans", branching=32, iterations=7, checks=16)
print result
print dists

dataset = np.random.rand(10000, 128)
testset = np.random.rand(1000, 128)
flann = FLANN()
result, dists = flann.nn(
    dataset, testset, 5, algorithm="kmeans", branching=32, iterations=7, checks=16)
print result
print dists
```
