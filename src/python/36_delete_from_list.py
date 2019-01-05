# methods to delete element from list

####pop() method , this will delete  element from the list

l1 = [1,2,3,4]
l1.pop() # by default pop deletes last element in list
print(l1) # this will print [1, 2, 3]
l1.pop(1) # this will delete 2nd element from list i.e 2 here
print (l1) # this will print [1, 3]

#### del operator 

l2 = [5,6,7,8]
del l2[1] # this will delete 2nd element in list i.e 6
print(l2)

#### remove function
l3 = [1,2,3,4]
l3.remove(1) # remove will delete 1 from list , remove deletes based on actual element value not on position
print(l3)