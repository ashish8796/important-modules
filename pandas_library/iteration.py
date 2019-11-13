#Iterating a DataFrame
#Iterating a DataFrame gives column names.

import pandas as pd
import numpy as np

'''
basic iteration (for i in object) produces −
Series − values
DataFrame − column labels
Panel − item labels
'''

N=20
df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
   })
for col in df:
    print(col)

'''
To iterate over the rows of the DataFrame, we can use the following functions −
iteritems() − to iterate over the (key,value) pairs
iterrows() − iterate over the rows as (index,series) pairs
itertuples() − iterate over the rows as namedtuples
'''

#iteritems()
df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
for key,value in df.iteritems():
    print(key,value)

#iterrows()
'''
iterrows() returns the iterator yielding each index value along with a series containing the data in each row.
'''
for row_index, row in df.iterrows():
    print(row_index, row)

#itertuples()
for row in df.itertuples():
    print(row)

