monster = '''

  oo`'._..---.___..-
 (_,-.        ,..'`
      `'.    ;
         : :`
        _;_; '''

# ascii art ✨
# https://ascii.co.uk/art


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")



left_or_right = input("Do you want to go left or right? L or R: \n").lower()
if left_or_right == "l":
    print("You reached a huge lake. It is dark right now.")
    swim_or_wait = input("Do you want to swim or wait until morning? SWIM | WAIT\n").lower()
    if swim_or_wait == "wait":
        print("You managed to cross the lake and you reached a large wall with three doors")
        door = input("Which door do you choose? RED | BLUE | YELLOW \n").lower()
        if door == "yellow":
            print("You reached the treasure!! You won!!")
        elif door == "red":
            print("You open the door and you were burned by fire. Game Over.")
        elif door == "blue":
            print(monster)
            print("The next room was filled with huge beasts. They ate you. Game Over.")
        else:
            print("You didn't chose any door and you waited and you starved to death. Game Over.")
    else:
        print("You were attacked by a trout. Game Over.")
else:
    print("You fall into a hole. Game Over.")
