#Table-wise Function Application
#adder function
'''
The adder function adds two numeric values as parameters and returns the sum.

def adder(ele1,ele2):
   return ele1+ele2
We will now use the custom function to conduct operation on the DataFrame.

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.pipe(adder,2)
'''

import pandas as pd 
import numpy as np 

def adder(ele1,ele2):
   return ele1+ele2

df = pd.DataFrame(np.random.randn(5,3), columns=['col1', 'col2', 'col3'])
print(df.pipe(adder, 2))

#Row or Column Wise Function Application
print(df.apply(np.mean))

#By passing axis parameter, operations can be performed row wise.
print(df.apply(np.mean, axis=1))

# df.apply(lambda x: x.max() - x.min())
print(df.apply(np.mean))

#Element Wise Function Application
# My custom function
print(df['col1'].map(lambda x:x*100))
print(df.applymap(lambda x: x*100))
print(df.apply(np.mean))