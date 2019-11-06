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

#Column Selection
print(df['one'])

#Column Addition
# Adding a new column to an existing DataFrame object with column label by passing new series
print("Adding a new column by passing as Series:")
df['three'] = pd.Series([10, 20, 30], index=['a','b','c'])
print(df)

print("Adding a new column to an existing DataFrame using the existing columns in dataFrame:")
df['four'] = df['one'] + df['three']
print(df)

#Column Deletion
# using del function
print("Deleting the first column using DEL function:")
del df['one']
print(df)

# using pop function
print ("Deleting another column using POP function:")
df.pop('two')
print(df)

#Row Selection, Addition, and Deletion
#Selection by Label
print(df.loc['b'])

#Selection by integer location
print(df.iloc[2])

#Slice Rows
print(df[2:4])

#Addition of Rows
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
df = df.append(df2)
print(df)

#Deletion of Rows
'''
Use index label to delete or drop rows from a DataFrame. If label is duplicated, 
then multiple rows will be dropped.
'''
# Drop rows with label 0
df = df.drop(0)
print(df)