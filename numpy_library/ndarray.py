'''An instance of ndarray class can be constructed by different array creation routines described later in the tutorial. 
The basic ndarray is created using an array function in NumPy as follows −
`numpy.array `
It creates an ndarray from any object exposing array interface, or from any method that returns an array.
`numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)`
'''

import numpy as np 
a = np.array([1, 2, 3])
print(a)

# more than one dimensions
b = np.array([[1,2], [3,4]])
print(b)
# minimum dimensions 
c = np.array([1,2,3,4,5], ndmin=2)
print(c)
# dtype parameter 
a = np.array([1,2,3,4], dtype=complex)
print(a)