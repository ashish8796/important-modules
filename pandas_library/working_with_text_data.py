'''
Sr.No	Function & Description
1	
lower()

Converts strings in the Series/Index to lower case.

2	
upper()

Converts strings in the Series/Index to upper case.

3	
len()

Computes String length().

4	
strip()

Helps strip whitespace(including newline) from each string in the Series/index from both the sides.

5	
split(' ')

Splits each string with the given pattern.

6	
cat(sep=' ')

Concatenates the series/index elements with given separator.

7	
get_dummies()

Returns the DataFrame with One-Hot Encoded values.

8	
contains(pattern)

Returns a Boolean value True for each element if the substring contains in the element, else False.

9	
replace(a,b)

Replaces the value a with the value b.

10	
repeat(value)

Repeats each element with specified number of times.

11	
count(pattern)

Returns count of appearance of pattern in each element.

12	
startswith(pattern)

Returns true if the element in the Series/Index starts with the pattern.

13	
endswith(pattern)

Returns true if the element in the Series/Index ends with the pattern.

14	
find(pattern)

Returns the first position of the first occurrence of the pattern.

15	
findall(pattern)

Returns a list of all occurrence of the pattern.

16	
swapcase

Swaps the case lower/upper.

17	
islower()

Checks whether all characters in each string in the Series/Index in lower case or not. Returns Boolean

18	
isupper()

Checks whether all characters in each string in the Series/Index in upper case or not. Returns Boolean.

19	
isnumeric()

Checks whether all characters in each string in the Series/Index are numeric. Returns Boolean.
'''

import pandas as pd
import numpy as np
#lower()
s = pd.Series(['Tom ', 'William Rick', ' John', 'Alber@t', np.nan, '1234','SteveSmith'])
print(s.str.lower())

#upper()
print(s.str.upper())

#len()
print(s.str.len())

#strip()
print(s.str.strip())

#split(pattern)
print(s.str.split(" "))

#cat(sep=pattern)
print(s.str.cat(sep='_'))

#get_dummies()
print(s.str.get_dummies())

#Contains(0)
print(s.str.contains(' '))

#replace(a.b)
print ("After replacing @ with $:")
print(s.str.replace('@','$'))

#repeat(value)
print(s.str.repeat(2))

#count(pattern)
print ("The number of 'm's in each string:")
print(s.str.count('m'))

#startswith(pattern)
print ("Strings that start with 'T':")
print(s.str.startswith('T'))

#endswith(pattern)
print ("Strings that end with 't':")
print(s.str.endswith('t'))

#find(pattern)
print(s.str.find('e'))

#findall(pattern)
print(s.str.findall('e'))

#swapcase()
print(s.str.swapcase())

#islower()
print(s.str.islower())
#isupper()
print(s.str.isupper())
#isnumeric
print(s.str.isnumeric())