name = "Nitin"
age = 28
print("Hello "+ name + " Your age is "+ str(age)) # ugly syntax

#python 3
print("Hello {} your age is {} ".format(name,age))
print("Hello {} your age is {} ".format(name,age+2))

#python 3.6
print(f"Hello {name} your age is {age}") #clean
print(f"Hello {name} your age is {age+5}")