import pandas as pd
import numpy as np
# .rolling() function
'''
This function can be applied on a series of data. 
Specify the window=n argument and apply the appropriate statistical function on top of it.
'''

df = pd.DataFrame(np.random.randn(10,4), index= pd.date_range('1/1/2000', periods=10), columns=list('ABCD'))
print(df)
print(df.rolling(window=3).mean())

#.expanding() Function
'''
This function can be applied on a series of data. 
Specify the min_periods=n argument and apply the appropriate statistical function on top of it.
'''
print(df.expanding(min_periods=3).mean())

#.ewm() Function
'''
ewm is applied on a series of data. Specify any of the com, span, halflife argument and 
apply the appropriate statistical function on top of it. It assigns the weights exponentially.
'''
print(df.ewm(com=0.5).mean())
