'''
ChainMap is used to combine several dictionaries or mappings. It returns a list of dictionaries.
'''
from collections import ChainMap


dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)


print(chain_map.maps)
print(chain_map['a']) #You can access chain map values by key name.

#ChainMap updates its values when its associated dictionaries are updated. 
dict2['c'] = 5
print(chain_map.maps)

#Getting Keys and Values from ChainMap
print (list(chain_map.keys())) #You can access the keys of a ChainMap with keys() function
print (list(chain_map.values())) # you can access the values of elements with values() function.

#Adding a New Dictionary to ChainMap
'''If you want to add a new dictionary to an existing ChainMap, use new_child() function.'''
dict3 = {'e' : 5, 'f' : 6}
new_chain_map = chain_map.new_child(dict3)
print(new_chain_map) #new dictionary is added to the beginning of ChainMap list.