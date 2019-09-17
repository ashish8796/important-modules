'''
The namedtuple() returns a tuple with names for each position in the tuple.
'''
from collections import namedtuple
Student = namedtuple('Student', 'fname, lname, age')
s1 = Student('John', 'Clarke', '13')
print(s1)

#Creating a namedtuple Using List
s2 = Student._make(['Adam','joe','18']) #you can use _make() to create a namedtuple instance with a list.
print(s2)

#Create a New Instance Using Existing Instance
'''The _asdict() function can be used to create an OrderedDict instance from an existing instance.'''
s2 = s1._asdict()
print(s2)
for i, val in s2.items():
    print(i, val)

#Changing Field Values with _replace() Function
'''To change the value of a field of an instance, the _replace() function is used.'''
s2 = s1._replace(age='14') #Remember that, _replace() function creates a new instance. It does not change the value of existing instance.
print(s1)
print(s2)