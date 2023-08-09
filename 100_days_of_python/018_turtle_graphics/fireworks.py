from turtle import Turtle, Screen
import random
angles = [0, 45, 150, 200]
colors = [
    ["#7B68EE", "#ADD8E6", "#6495ED", "#0000CD", "#4682B4", "#9370DB", "#48D1CC", "#5F9EA0"],
    ["#FFA500", "#FFD700", "#F5DEB3", "#F0E68C", "#FFFF00", "#FF4500"],
    ["#FA8072", "#F08080", "#CD5C5C", "#BC8F8F", "#FFC0CB", "#FFB6C1"]
]

turtle = Turtle()
screen = Screen()
turtle.shape("circle")
turtle.shapesize(0.3)
turtle.speed("fastest")
turtle.pensize(2)

current_position = turtle.heading()
step = 30


def random_walk():
    turtle.penup()
    turtle.left(random.randint(50, 270))
    turtle.forward(random.randint(100, 800))
    fireworks()


def fireworks():
    turtle.pendown()
    firework_size = random.randint(20, 50)
    random_number = random.randint(0, len(colors) - 1)
    random_set = colors[random_number]
    for x in range(int(361 / step)):
        turtle.pencolor(random.choice(random_set))
        turtle.circle(firework_size)
        turtle.setheading(turtle.heading() + step)
    random_walk()


fireworks()


screen.exitonclick()
