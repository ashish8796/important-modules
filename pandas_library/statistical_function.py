import pandas as pd 
import numpy as np 

#Percent_change
s = pd.Series([1,2,3,4,5,4])
print(s.pct_change())

df = pd.DataFrame(np.random.randn(5, 2))
print(df)
print(df.pct_change(axis=1))

#Covariance
'''
Covariance is applied on series data. The Series object has a method cov to 
compute covariance between series objects. NA will be excluded automatically.
'''
#Cov Series
s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(10))

print(s1.cov(s2))

#Covariance method when applied on a DataFrame, computes cov between all the columns.
frame = pd.DataFrame(np.random.randn(10,5), columns=['a','b','c','d','e'])
print(frame['a'].cov(frame['b']))
print(frame.cov())

#Correlation
'''
Correlation shows the linear relationship between any two array of values (series). 
There are multiple methods to compute the correlation like pearson(default), spearman and kendall.
'''
print(frame['a'].corr(frame['b']))
print(frame.corr())

#Data Ranking
s = pd.Series(np.random.randn(5), index=list('abcde'))
print(s)
print(s.rank())