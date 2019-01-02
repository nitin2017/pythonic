# create a function which takes two numbers as input and gives you greater one
# for e.g take input (13,45) and print 45 is bigger number

def greater_num(num1,num2):
    if(num1>num2):
        return num1
    else:
        return num2
    
a = int(input("Enter first number :-  ").strip())
b = int(input("Enter second number :-  ").strip())
print(f"{greater_num(a,b)} is larger number")