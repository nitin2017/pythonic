# for loop with range function
for i in range(10):
    print(f"Hello World {i}")

# sum from 1 to 10
total = 0
for i in range(11):
    total += i
print(f"Sum of numbers from 1 to 10 is {total}")

# ask user to input a number containing more than one digit
# example = "12345"
# calculate 1+2+3+4+5 and print

user_number  = input("Enter a number :- ").strip()
total = 0
for i in range(0,len(user_number)):
    total += int(user_number[i])
print(total)

# ask a user for Name
# Example - Nitin Choudhary
# print Count of each words
# output 
# N : 2
# I : 2
# T : 1
# c : 1
# AND SO ON 

name  = input("Enter your name :- ")
temp_var = ""
for i in range(0,len(name)):
    if name[i] not in temp_var:
        print(f"{name[i]}  :  {name.count(name[i])}")
        temp_var += name[i]
    