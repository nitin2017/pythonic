# append method
# insert method
# how to join two list
# extend method
# differnce between append and extend method

fruits1 = ['mango','apple']
fruits1.append('banana') # append adds element at last in the list
print(fruits1)

fruits1.insert(1,'grapes') # insert is used to add elemnt to specific position in list
                           # and elemnt at 1st pos and onwards will move one position ahead 
print(fruits1)

# concatenate two lists 

l1 = ['a','b','c']
l2 = ['c','d']

result = l1 + l2
print(result) # this will join all elements of two lists

# extend is used to add elements present in one list to another list

l1.extend(l2)
print(l1) 

# extend vs append 
l3 = [1,2]
l4 = [3,4]
l5 = [1,2]
l6 = [3,4]
l3.append(l4) # this will add "list" itself as a element i.e list inside list
l5.extend(l6) # this will add elements from l6 to list l5
print(l3)
print(l5) 