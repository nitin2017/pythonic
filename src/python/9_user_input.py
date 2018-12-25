# understand how to take input from users
# input is always taken as string 
name = input("type your name")
print ("hello " + name)
age = input("what is your age")
print ("your age is "+ age)

# take two inputs from user in a single line

name , age = input("enter your name and age").split()
print(name)
print(age)