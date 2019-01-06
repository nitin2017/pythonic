# list comprehension
# with the help of list comprehension we can create the lis tin one line

# create a list of squares from 1 to 10

## normal way
squares = []
for i in range(1,11):
    squares.append(i**2)

print(squares)

## using list comprehension 

square2 = [i**2 for i in range(1,11)]
print(square2)

negative  = [-i for i in range(1,11)]
print(negative)

## another example

names = ['nitin','mohit','rohit','shael']
## create another list which contains first character of every name ['n','m','r','s']
first = [name[0] for name in names]
print(first)


##### LIST COMPREHENSION with if statement

numbers = list(range(1,11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# create another list using list comprehension which conatins even number from above list

even_nums = [i for i in numbers if i%2==0]
print(even_nums)

odd_nums = [i for i in range(1,11) if i %2 != 0]
print(odd_nums)

##### LIST COMPREHENSION with if-else statement

nums = [1,2,3,4,5,6,7,8,9,10]
# if even multile by 2 , if odd multiply by -1
# output = [-1,4,-3,8,-5,12,-7,16,-9,20]
num_list = [i*2 if i%2==0 else -i for i in nums]
print(num_list)

#### List comprehension in nested list

example = [[1,2,3],[1,2,3],[1,2,3]]
nested_Comp = [[i for i in range(1,4)] for j in range(3)]
print(nested_Comp)