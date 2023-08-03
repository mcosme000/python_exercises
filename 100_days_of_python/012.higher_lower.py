import random



"""
- - - PSEUDO CODE - - -
1. get two random choices from data
2. ask user for an answer
3. Check answer
4. if True:
        - continue game
            - get a new random choice
            - ask user for answer
        - increase score
   if False:
        - stop game
"""

import higher_lower_data
score = 0
game = True
a = random.choice(higher_lower_data.data)

def compare(guess):
    global a, b
    if guess == "a":
        a = a
        return a['follower_count'] > b['follower_count']
    else:
        a = b
        return b['follower_count'] > a['follower_count']


def check_answer(guess):
    global score
    global game
    answer = compare(guess)
    if answer:
        score += 1
        print(f"Score: {score}")
    else:
        print("We are sorry, you lost")
        print(f"You scored {score} points!")
        game = False


while game:
    b = random.choice(higher_lower_data.data)
    # print(f"*** DEBUG: {a['name']}: {a['follower_count']} VS {b['name']}: {b['follower_count']}")
    print(f"Compare A: {a['name']}")
    print("VS")
    print(f"Agains B: {b['name']}")

    guess = input("Who has more followers? 'A' or 'B': ").lower()
    check_answer(guess)
