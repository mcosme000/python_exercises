from turtle import Turtle, Screen
from random import randint, choice

turtle = Turtle()
turtle.shape("circle")
turtle.shapesize(0.5)
turtle.pensize(8)

screen = Screen()


angles = [0, 90, 180, 270]
colors = ["#7B68EE", "#ADD8E6", "#6495ED", "#0000CD", "#4682B4", "#9370DB", "#48D1CC", "#5F9EA0"]
# We will be using TUPLE
screen.colormode(255)


def random_walk():
    random_color = (randint(1, 255), randint(1, 255), randint(1, 255))
    turtle.left(choice(angles))
    turtle.pencolor(random_color)
    turtle.forward(20)


for _ in range(1, 100):
    random_walk()


screen.exitonclick()
