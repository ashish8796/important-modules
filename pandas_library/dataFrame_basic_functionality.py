import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our data series is:")
print(df)

#T (Transpose)
#The rows and columns will interchange.
print ("The transpose of the data series is:")
print(df.T)

#axes
#Returns the list of row axis labels and column axis labels.
print ("Row axis labels and column axis labels are:")
print(df.axes)

#dtypes
print ("The data types of each column are:")
print(df.dtypes)

#empty
print ("Is the object empty?")
print(df.empty)

#ndim
print ("The dimension of the object is:")
print(df.ndim)

#shape
#Tuple (a,b), where a represents the number of rows and b represents the number of columns.
print ("The shape of the object is:")
print(df.shape)

#size
print("The size of the object is:")
print(df.size)

#values
print("The actual data in our data frame is:")
print(df.values)

#Head & Tail
print("The first two rows of the our data frame are:")
print(df.head(2))
print("The last tow rows of the our data frame are:")
print(df.tail(2))