# looping in tuples
# tuple with one element
# tuple without parenthesis
# tuple unpacking
# list inside tuple
# some functions that can be used with tuple

mixed = (1,2,3,4.0)

# for loop and tuple 
for i in mixed:
    print(i)

# tuple with one element

nums  = (1) # these are not tuples 
words = ('word1') # this is not tuple
print(type(nums)) #<class 'int'>
print(type(words))#<class 'str'>

nums1 = (1,) # tha comma at last help python understand this is tuple
words1 = ('word1',)
print(type(nums1)) #<class 'tuple'>
print(type(words1)) #<class 'tuple'>

# tuples without parenthesis 

guitars  =  'yamaha' , 'baton rouge' , 'taylor'
print(type(guitars)) # <class 'tuple'>

# tuple unpacking

words  = ['a','b','c']
w1 ,w2 ,w3 = (words)
print(f"{w1} and {w2} and {w3} ")

# list inside tuples 
# now in tuples we cannot add or remove elements 
# but elements can be added or removes in list present in tuple

favourites = ('yellow',['orange','black','white']) # list is present inside a tuple
favourites[1].pop()
favourites[1].append('pink')
print(favourites) # ('yellow', ['orange', 'black', 'pink']) white is removed from list inside tuple


## some functions

print(min(mixed))
print(max(mixed))

#### Something more about list , tuple and string

# using range to create tuple

nums = tuple(range(1,11))
print(nums)