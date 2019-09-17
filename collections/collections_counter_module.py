#Collection modules :- Collections in Python are containers that are used to store collections of data, for example, list, dict, set, tuple etc.
'''
counter- The counter() function takes a iterable or mapping as argument and retunrs a dictionary. In this dictionary
a key is an element and value is the numbers of times that element exists in the iterable or mapping.
You have to import the Counter class before you can create a counter instance.
'''
from collections import Counter
list = [1,2,3,4,1,2,6,7,3,8,1]
cnt = Counter(list)
print(cnt) #give dict, number as key and count as value
print(cnt[6]) #give count of 6

'''
Counter has three additional functions:
Elements- element() function #It returns a list containing all the elements in the Counter object.
Most_common([n])- You can sort dictionary according to the number of counts in each element using most_common() function of the Counter object.
Subtract([interable-or-mapping])- deducts elements count using iterable or mapping as  argument.
'''
# elems = [i for i in cnt.elements()]
print([i for i in cnt.elements()])
print(cnt.most_common())
deduct = {1:1, 2:2}
cnt.subtract(deduct)
print(cnt)