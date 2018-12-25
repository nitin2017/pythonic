# Ask user to input 3 numbers and you have to print average of three numbers using string formatting

num1,num2,num3 = input("Enter three number comma seperated ").split(",")
average = (int(num1) + int(num2) + int(num3))/3
print(f"Average of {num1} , {num2} , {num3} is {average}")