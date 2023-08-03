"""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
"""

import random

numbers = list(range(1, 101))
rand_number = random.choice(numbers)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n")
choice = int(input("* * * Guess a number * * *\n"))
is_playing = True

if difficulty == 'easy':
    tries = 10
else:
    tries = 5

def create_message(choice):
    difference = abs(rand_number - choice)
    if rand_number > choice and difference > 10: return "Too low"
    elif rand_number > choice and difference <= 10: return "Low, but close"
    elif rand_number < choice and difference > 10: return "Too high"
    elif rand_number < choice and difference <= 10: return "High, but close"

print(f"##Debugging: {rand_number}")

while is_playing:
    if choice == rand_number:
        print("You won!")
        is_playing = False
    else:
        tries -= 1
        if tries == 0:
            print("You ran out of tries, you lost")
            is_playing = False
        else:
            message = create_message(choice)
            print(message)
            print(f"You have {tries} tries left\n")
            choice = int(input("* * * Guess a number * * * \n"))
