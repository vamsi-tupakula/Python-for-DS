"""
Numpy is a library for python which provides support for adding large, multidimensional arrays and matrices.
It provides high-level mathematical functions to operate on these arrays.
Arrays, unlike python lists, is a data structure that stores a collection of objects of same datatype.
The main data structure in numpy is Ndarray
"""

import numpy as np

# 1d array
a = np.array([1,2,3])
print('a :', a)
print('type(a) :', type(a))

# creating 2d array

b = np.array([[1,2,3],
                [4,5,6]])
print(b)