# iterator vs iterable 

numbers = [1,2,3,4] #iterables
squares = map(lambda a:a**2,numbers) # iterators

for i in squares:
    print(i)

for i in numbers:
    print(i)

# step 1 : call iter function 
# iter(numbers) ---> iterator 
# next(iter(numbers))

number_iter =iter(numbers)
print(number_iter) #<list_iterator object at 0x000002887BDA44E0>   
print(next(number_iter)) ## this will give 1 
print(next(number_iter)) ## this will give 2
print(next(number_iter)) ## this will give 3 
print(next(number_iter)) ## this will give 4
#print(next(number_iter)) ## this will give StopIteration 
