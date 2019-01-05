# ordered collection of items
# created using square brackets []
# can store naything like int , float , string 

numbers = [1,2,3,4]
print(numbers)
print(numbers[1])  # this will print second element as list pos starts from 0

words = ["word1" , "word2", "word3"]
print(words)
print(words[:1]) # slicing is similar to string slicing

mixed = [1,2,3,4,"five",4.7,None] # None is kind of emplty place holder in python
print(mixed)
print(mixed[-1:])

# change a element in list
mixed[1] = "two"
print(mixed)

