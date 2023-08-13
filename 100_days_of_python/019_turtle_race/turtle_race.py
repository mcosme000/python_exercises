from turtle import *
import random

screen = Screen()
screen.setup(500, 400)
colors = ["blue", "orange", "green", "pink", "gray"]

turtles = []
racing = True


def set_turtles():
    for n in range(0, 5):
        turtle = Turtle(shape="turtle")
        turtle.speed("fast")
        turtle.penup()
        turtle.color(colors[n])
        turtle.setpos(-200, -120 + (n * 60))
        turtles.append(turtle)
    user_bet = screen.textinput("Place your bet", "Which turtle do you think will win?")
    start_race(user_bet)


def start_race(user_bet):
    global racing
    while racing:
        for turtle in turtles:
            step = random.randint(0, 20)
            turtle.forward(step)
            if turtle.xcor() > 230:
                winner = turtle.pencolor()
                if winner == user_bet:
                    write("You WON :)")
                else:
                    write("You LOST :(")
                racing = False


set_turtles()
screen.exitonclick()
