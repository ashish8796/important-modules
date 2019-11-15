'''
There are two kinds of sorting available in Pandas. They are −
1-By label
2-By Actual Value
'''
import pandas as pd
import numpy as np

unsorted_df=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns=['col2','col1'])
print(unsorted_df)

#By Label & Order of sorting
sorted_df = unsorted_df.sort_index(ascending=False)
print(sorted_df)

#Sort the Columns
'''
By passing the axis argument with a value 0 or 1, the sorting can be done on the column labels.
'''
sorted_df1 = unsorted_df.sort_index(axis=1)
print(sorted_df1)

#By Value
unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
sorted_df = unsorted_df.sort_values(by='col1')
print(sorted_df)
#'by' argument takes a list of column values.
sorted_df = unsorted_df.sort_values(by=['col1','col2'])
print(sorted_df)

#Sorting Algorithm
sorted_df = unsorted_df.sort_values(by='col1' ,kind='mergesort')
print(sorted_df)