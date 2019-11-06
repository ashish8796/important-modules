import pandas as pd 
import numpy as np 

#Create a series with 100 random numbers
s = pd.Series(np.random.randn(4))
print(s)

#axes
#Returns the list of the labels of the series
print("The axes are:")
print(s.axes)

#empty
print(s.empty)

#ndim
#Returns the number of dimensions of the object.
print("The dimensions of the object:")
print(s.ndim)

#size
print("The size of object is:")
print(s.size)

#values
print("The actual data series is:")
print(s.values)

# Head & Tail
print("The first two rows of the data:")
print(s.head(2))
print("The last tow rows of the data:")
print(s.tail(2))