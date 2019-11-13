'''
Reindexing changes the row labels and column labels of a DataFrame. 
To reindex means to conform the data to match a given set of labels along a particular axis.
'''
import pandas as pd 
import numpy as np 
N=20
df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})
# print(df)
#reindex the DataFrame
df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])
# print(df_reindexed)

#Reindex to Align with Other Objects
df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])
df1 = df1.reindex_like(df2)
print(df1)
print(df2)

#Filling while ReIndexing
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])
# Padding NAN's
print(df2.reindex_like(df1))

# Now Fill the NAN's with preceding Values
print ("Data Frame with Forward Fill:")
print(df2.reindex_like(df1,method='ffill'))

#Limits on Filling while Reindexing
print ("Data Frame with Forward Fill limiting to 1:")
print(df2.reindex_like(df1,method='ffill',limit=1))

#Renaming
'''
The rename() method allows you to relabel an axis based on some mapping (a dict or Series) or an arbitrary function.
'''

print ("After renaming the rows and columns:")
df1.rename(columns={'col1':'c1', 'col2':'c2','col3':'c3'}, index={0:'apple', 1:'banana',2:'durian'}, inplace=True)
print(df1)