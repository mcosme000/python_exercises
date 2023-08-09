from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("circle")
turtle.shapesize(0.5)
turtle.pensize(8)
turtle.speed(9)
angles = [0, 90, 180, 270]
colors = ["#7B68EE", "#ADD8E6", "#6495ED", "#0000CD", "#4682B4", "#9370DB", "#48D1CC", "#5F9EA0"]


def random_walk():
    turtle.left(random.choice(angles))
    turtle.pencolor(random.choice(colors))
    turtle.forward(20)


for _ in range(5, 900):
    random_walk()

screen = Screen()
screen.exitonclick()
