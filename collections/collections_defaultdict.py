'''
The defaultdict works exactly like a python dictionary, except for it 
does not throw KeyError when you try to access a non-existent key.
Instead, it initializes the key with the element of the data type that you pass as an 
argument at the creation of defaultdict. The data type is called default_factory.
'''
from collections import defaultdict
nums = defaultdict(int) #Create a defaultdict, You have to specify a data type as an argument.
nums['one'] = 1
nums ['two']= 2
print(nums['two'])
print(nums['three']) #prints 0 cause defeaultdict created a new key as 'three' and assigned a value 0.

'''
let's say you want the count of each name in a list of names given
'''
count = defaultdict(int) #here int is called data_factory
names_list = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
for names in names_list:
    count[names] += 1
print(count)
#ountputs - defaultdict(<class 'int'>, {'Mike': 5, 'John': 3, 'Anna': 2, 'Britney': 1, 'Smith': 2})