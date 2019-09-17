'''
The deque is a list optimized for inserting and removing items.
''' 
from collections import deque
lst = ["a","b","c"]
deq = deque(lst) #You have to pass a list as an argument
print(deq)

#Inserting Elements to deque
deq.append("d") #to insert a element in right of the list
deq.appendleft("e") #to insert a element in left of the list
print(deq)

#Removing Elements from the deque
deq.pop() #to remove a element in right of the list
deq.popleft() #to remove a element in left of the list
print(deq)

#Clearing a deque
deq.clear() #to remove all elements from a list
print(deq)

#Counting Elements in a deque
print(deq.count("a"))
 #to count a specific element in a list