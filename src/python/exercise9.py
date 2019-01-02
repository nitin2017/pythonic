# ask user to input a number containing more than one digit
# example = "12345"
# calculate 1+2+3+4+5 and print

user_number = input("Enter a number with more than 1 digit :- ")
total = 0
i =0 
while i<len(user_number):
    total += int(user_number[i])
    i += 1
print(f"Sum of digit of number {user_number} is {total}")