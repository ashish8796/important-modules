'''Sr.No	Indexing & Description
1	
.loc()
Label based

2	
.iloc()
Integer based

3	
.ix()
Both Label and Integer based'''

#.loc()
'''.loc() has multiple access methods like −
A single scalar label
A list of labels
A slice object
A Boolean array
loc takes two single/list/range operator separated by ','. The first one indicates the row and the second one indicates columns.'''

import pandas as pd 
import numpy as np 

df = pd.DataFrame(np.random.randn(8,4),
index=['a','b','c','d','e','f','g','h'], columns= ['A','B','C','D'])

#select all rows for a specific column
print(df.loc[:,"A"])

# Select all rows for multiple columns, say list[]
print(df.loc[:,['A','C']])

# Select few rows for multiple columns, say list[]
print(df.loc[['a','b','e','g'],['A','D']])

# Select range of rows for all columns
print(df.loc['a':'f'])

# for getting values with a boolean array
print(df.loc['a']>0)

#.iloc()
'''The various access methods are as follows −
An Integer
A list of integers
A range of values'''

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
# Select range of rows for all columns
print(df.iloc[:4])

# Integer slicing
print(df.iloc[:4])
print(df.iloc[1:5,2:4])

# Slicing through list of values
print(df.iloc[[1,3,5],[1,3]])
print(df.iloc[1:3, :])
print(df.iloc[:,1:3])

#.ix()
'''Besides pure label based and integer based, Pandas provides a hybrid method for 
selections and subsetting the object using the .ix() operator.'''

# Integer slicing
print(df.ix[:4])

# Index slicing
print(df.ix[:,'A'])

'''We will use the basic indexing operator '[ ]' −
Example 1'''
print(df["A"])
#We can pass a list of values to [ ] to select those columns.
print(df[['A','B']])
#Attribute Access
print(df.A)