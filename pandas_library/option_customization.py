#Pandas provide API to customize some aspects of its behavior, display is being mostly used.
'''
The API is composed of five relevant functions. They are −
get_option()
set_option()
reset_option()
describe_option()
option_context()
'''
#get_option(param)
'''
get_option takes a single parameter and returns the value as given in the output below −
``display.max_rows``
Displays the default number of value. Interpreter reads this value and displays 
the rows with this value as upper limit to display.
'''
import pandas as pd 
print(pd.get_option("display.precision"))
#display.max_columns
print(pd.get_option("display.max_columns"))

#set_option(param,value)
#set_option takes two arguments and sets the value to the parameter 
#display.max_rows
pd.set_option("display.max_rows", 90)
print(pd.get_option("display.max_rows"))

#display.max_columns
pd.set_option("display.max_columns", 30)
print(pd.get_option("display.max_columns"))

#reset_option(param)
'''reset_option takes an argument and sets the value back to the default value'''
#display.max_rows
pd.reset_option("display.max_rows")
pd.reset_option("display.max_columns")
print(pd.get_option("display.max_rows"))
print(pd.get_option("display.max_columns"))

#describe_option(param)
print(pd.describe_option("display.max_rows"))

#option_context()
'''option_context context manager is used to set the option in ``with`` statement temporarily. 
Option values are restored automatically when you exit the with block −'''
with pd.option_context("display.max_rows", 10):
    print(pd.get_option("display.max_rows"))
    print(pd.get_option("display.max_rows"))
'''
Frequently used Parameters
Sr.No	Parameter & Description
1	
display.max_rows
Displays maximum number of rows to display

2	
display.max_columns
Displays maximum number of columns to display

3	
display.expand_frame_repr
Displays DataFrames to Stretch Pages

4	
display.max_colwidth
Displays maximum column width

5	
display.precision
Displays precision for decimal numbers
'''