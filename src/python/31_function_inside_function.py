def greater_num(num1,num2):
    if(num1>num2):
        return num1
    else:
        return num2

def greater_three(num1,num2,num3):
    bigger = greater_num(a,b)
    return greater_num(bigger,c)

a = int(input("Enter first number :-  ").strip())
b = int(input("Enter second number :-  ").strip())
c = int(input("Enter third number :-  ").strip())
print(f"{greater_three(a,b,c)} is largest number between {a} , {b} , {c}")
    