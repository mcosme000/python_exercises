from turtle import Turtle, Screen
import random

turtle = Turtle()

colors = ["#7B68EE", "#ADD8E6", "#6495ED", "#0000CD", "#4682B4", "#9370DB", "#48D1CC", "#5F9EA0"]

degrees = 360
corners = 3
turtle.left(180)

while corners < 11:
    turtle.color(random.choice(colors))
    for _ in range(1, corners + 1):
        turtle.left(degrees / corners)
        turtle.forward(50)
    corners += 1


screen = Screen()
screen.exitonclick()
