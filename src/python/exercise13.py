# create a function which takes three numbers as input and gives you greater one
# for e.g take input (13,45,17) and print 45 is bigger number

def greater_three(num1,num2,num3):
    if(num1>num2 and num1>num3):
        return num1
    elif(num2>num1 and num2>num3):
        return num2
    else:
        return num3

a = int(input("Enter first number :-  ").strip())
b = int(input("Enter second number :-  ").strip())
c = int(input("Enter third number :-  ").strip())
print(f"{greater_three(a,b,c)} is larger number")