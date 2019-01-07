# we use enumerate function with for loop to keep track position of our item 
# in iterable

# How can we do this  without using enumerate function
names = ['a' , 'b','c','d']
# 0 -- a 
# 1 -- b 
# 2 -- c 
# 3 -- d
pos = 0
for name in names:
    print(f"{pos} -- {name}")
    pos +=1

# using enumerate function

for pos ,name in enumerate(names):
    print(f"{pos} -- {name}")

# define a function that takes to arguements
# 1.) list containing string
# 2.) string that want to find in your list
# and this function will return the index of string in your list 
# if the string is not present return -1

def pos_finder(l,target):
    for pos, name in enumerate(l):
        if name==target:
            return pos
    return -1

names = ['a' , 'b','c','d']

print(pos_finder(names,'b'))
print(pos_finder(names,'d'))
print(pos_finder(names,'f'))