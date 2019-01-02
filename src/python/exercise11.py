#################### NUMBER GUESSING GAME
# Make a variable , like winning_number and assign any number to it.
# ask user to guess a number
# if user guessed correctly then print YOU WIN !!!
# if user guessed lower than actual number then print "too low"
# if user guessed higher than actual number then print "too high"

import random
winning_number = random.randint(1,101)
guess = 1
user_number = int(input("Guess the number between 1 and 100 : "))
game_over = False
while not game_over:
    if winning_number == user_number:
        print(f"YOU WIN !!! AND YOU GUESSED THIS IN {guess} ATTEMPTS")
        game_over=True
    else:
        if winning_number> user_number:
            print("TOO LOW")
            guess +=1
            user_number = int(input("guess again ... ").strip())
        else:
            print("TOO HIGH")
            guess +=1
            user_number = int(input("guess again ... ").strip())


