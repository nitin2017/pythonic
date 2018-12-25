# Understand variables in python 
number1 =  2
print(type(number1))
print(number1)
number2 = 0.45
print(type(number2))
print(number2)
name = "Nitin"
print(type(name))
print(name)

# Some rules to define a variable

#1 we cannot start a variable with a number 
#  1number = 2 this will give compilation error

# Cannot start with a special character , unerscore will work
_name = "nitin"
print(_name)

# Use snake case writing to define variables 
user_name = "Nitin"

name ,age = "Nitin",28
print("Hello "+name+ " your age is " + str(age))
