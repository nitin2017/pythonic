# sum of n natural numbers
# ask a user for natural number (n)
# print toatl from 1 to n

user_number = int(input("Enter a natural number:- ").strip())
total = 0
i = 1
while i<=user_number:
    total += i
    i += 1
print(f"Sum of natural numbers from 1 to {user_number} is {total}") 