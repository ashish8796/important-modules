'''
OrderedDict is a dictionary where keys maintain the order in which they are inserted, 
which means if you change the value of a key later, it will not change the position of the key.
'''
from collections import Counter, OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)
for key, value in od.items():
    print(key, value)
#we create a Counter from a list and insert element to an OrderedDict based on their count
lst = ["a","c","c","a","b","a","a","b","c"]
cnt = Counter(lst)
od = OrderedDict(cnt.most_common())
print(od)