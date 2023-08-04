import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

numbers = list(range(1, 101))
rand_number = random.choice(numbers)
print(f"##Debugging: {rand_number}")

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n")
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def check_answer(choice):
    difference = abs(rand_number - choice)
    if rand_number == choice: return "YOU WON!!"
    elif rand_number > choice and difference > 10: return "Too low"
    elif rand_number > choice and difference <= 10: return "Low, but close"
    elif rand_number < choice and difference > 10: return "Too high"
    elif rand_number < choice and difference <= 10: return "High, but close"

tries = set_difficulty()
choice = int(input("* * * Guess a number * * *\n"))
message = check_answer(choice)
print(message)

while not choice == rand_number:
    tries -= 1
    if tries == 0:
        print("You ran out of tries, you lost")
        break
    else:
        choice = int(input("* * * Guess a number * * * \n"))
        message = check_answer(choice)
        print(message)
        print(f"You have {tries} tries left\n")
