number_one = input("enter first number")
number_two = input("enter second number")
total =  number_one + number_two
print("total is " + total) ### This will print output as 44 , however we need 8 as answer

number_one = int(input("enter first number"))
number_two = int(input("enter second number"))
total =  number_one + number_two
print("total is " + str(total)) ### we have used str() since int cannot be concatenated to string

number1 = float("44")
number2 = int("33")
print (number1+number2)