#Pandas deals with the following three data structures
    #Series
    #DataFrame
    #Panel

#Series
#Series is a one-dimensional array like structure with homogeneous data. For example, the following series is a collection of integers 10, 23, 56, 
# Key Points
# Homogeneous data
# Size Immutable
# Values of Data Mutable


'''
pandas.Series
creation of pandas Series
pandas.Series('data, index, dtype, copy')
'''


import pandas as pd
import numpy as np 

#Create an empty series 
s = pd.Series()
print(s)

#Create a Series from ndarray
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data, index=[1, 2, 3, 4])
print(s)

#Create a Series from dict
data = {'a':0., 'b':1., 'c':2.}
s = pd.Series(data, index=['a','b','c','d'])
print(s)

#Create a Series from Scalar
#If data is a scalar value, an index must be provided.
s = pd.Series(5, index=[0,1,2,3,4])
print(s)

#Accessing Data from Series with Position 
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s[0])
print(s[:3])
print(s[-3:])

#Retrieve Data Using Label (Index)
print(s['a'])
print(s[['a', 'b', 'c']])
print(s['g']) #output key error

