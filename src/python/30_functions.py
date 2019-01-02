#functions in python
# lets start with a basic example

def addTwoNumbers(num1,num2):
    return num1+num2

a = int(input("Enter first number :-  ").strip())
b = int(input("Enter second number :-  ").strip())
total = addTwoNumbers(a,b)
print(total)