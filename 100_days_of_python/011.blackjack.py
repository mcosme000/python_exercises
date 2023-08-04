import random
from functools import reduce

# BLACKJACK
"""
> 21: BUST
2 - 10
J Q K = 10
A = 11

dealer smaller than 17, the must pick a new card
"""

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def start_game():
    keep_playing = True

    player_total = 0
    dealer_total = 0

    while keep_playing:
        player_choice = deal_card()
        print(f"You picked up [{player_choice}]")
        player_total += player_choice
        print(f"The player score is {player_total}")

        print("\n")

        dealer_choice = deal_card()
        print(f"The dealer picked up [{dealer_choice}]")
        dealer_total += dealer_choice
        print(f"The dealer score is {dealer_total}")

        print("\n")

        choice = input("Do you want to keep playing? yes | no \n>_").lower()
        if choice == "no": keep_playing = False

    if player_total == 21:
        print("Player won, 21")
        keep_playing = False
    elif player_total > 21 or dealer_total > player_total:
        print("player got more than 21, player lost")
        keep_playing = False
    elif player_total > dealer_total or dealer_total > 21:
        print("player won!")
    else:
        print("Player lost")

start_game()
