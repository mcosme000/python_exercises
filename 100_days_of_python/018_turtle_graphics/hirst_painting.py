import colorgram
from turtle import Turtle, Screen
import random

screen = Screen()
colors = colorgram.extract('color_4.jpeg', 4)
print(colors)


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])


hex_values = [rgb_to_hex(color.rgb) for color in colors]
print(hex_values)


turtle = Turtle()
turtle.shape("circle")
turtle.shapesize(1)
turtle.pensize(5)
turtle.speed("fastest")
turtle.pu()
turtle.setheading(220)
turtle.forward(300)
turtle.setheading(0)


def generate_line():
    turtle.speed(8)
    for _ in range(1, 11):
        turtle.forward(20)
        turtle.dot(20, random.choice(hex_values))
        turtle.forward(20)
    turtle.pu()
    go_back()


def go_back():
    turtle.speed("fastest")
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(180)


for _ in range(1, 11):
    generate_line()

screen.exitonclick()
