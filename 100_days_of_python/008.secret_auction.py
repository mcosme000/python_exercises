import os
import time
# SECRET AUCTION

# TO CLEAN THE CONSOLE!!!
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

bids_dic = {}
is_bidding = True

def wait():
    print("We are getting the results...")
    print(".")
    time.sleep(1)
    print(". .")
    time.sleep(1)
    print(". . .")

def find_highest_bidder(dic):
    max_number = max([dic[value] for value in dic])
    max_bidder = [key for key, value in dic.items() if value == max_number][0]
    print(f"The winner is {max_bidder} with a bid of ${dic[max_bidder]}. ")

while is_bidding:
    clear_terminal()
    name = input("What is your name?\n")
    bid = int(input(f"Great, {name}, how much do you want to bid?\n"))

    bids_dic[name] = bid

    choice = input("Is there more people who wants to bid? [ yes | no ] \n").lower()
    if choice == "no":
        is_bidding = False
        print("Thank you.")
        wait()
        find_highest_bidder(bids_dic)
