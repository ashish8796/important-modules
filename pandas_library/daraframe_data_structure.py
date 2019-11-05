#Python Pandas - DataFrame
'''
DataFrame is a two-dimensional array with heterogeneous data  i.e., data is aligned in a tabular fashion in rows and columns.
Features of DataFrame
    Potentially columns are of different types
    Size – Mutable
    Labeled axes (rows and columns)
    Can Perform Arithmetic operations on rows and columns
'''

'''
pandas.DataFrame
pandas.DataFrame( data, index, columns, dtype, copy)
'''



#Create an Empty DataFrame
import pandas as pd 
df = pd.DataFrame()
print(df)

#Create a DataFrame from Lists
#Example 1
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

#Example 2
data = [['Alex',10,'!'],['Bob',12,'@'],['Clarke',13,'#']]
df = pd.DataFrame(data, columns=['Name','Age','Quality'], dtype = float)
print(df)

#Create a DataFrame from Dict of ndarrays / Lists
#All the ndarrays must be of same length
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)

#Create a DataFrame from List of Dicts
# The dictionary keys are by default taken as column names.
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
#With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print(df)
print(df1)
print(df2)

#Create a DataFrame from Dict of Series
#Dictionary of Series can be passed to form a DataFrame. The resultant index is the union of all the series indexes passed.
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)