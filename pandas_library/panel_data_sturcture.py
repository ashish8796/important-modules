'''
A panel is a 3D container of data. The term Panel data is derived from econometrics 
and is partially responsible for the name pandas − pan(el)-da(ta)-s.
'''

#pandas.Panel()
'''
pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)
'''
#Create Panel
#From 3D ndarray
# creating an empty panel
import pandas as pd
import numpy as np

data  = np.random.rand(2,4,5)
p = pd.Panel(data)
print(p)

#From dict of DataFrame Objects
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
   'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p)