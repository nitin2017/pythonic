#################### NUMBER GUESSING GAME
# Make a variable , like winning_number and assign any number to it.
# ask user to guess a number
# if user guessed correctly then print YOU WIN !!!
# if user guessed lower than actual number then print "too low"
# if user guessed higher than actual number then print "too high"

import random
winning_number = random.randint(1,101)
user_number = int(input("Guess the number : "))
if winning_number==user_number:
    print("YOU WIN !!!!")
else:
    if winning_number>user_number:
        print("TOO LOW")
    else:
        print("TOO HIGH")

print(f"Winning number is {winning_number}")