from turtle import Turtle, Screen
import random
colors = ["#7B68EE", "#ADD8E6", "#6495ED", "#0000CD", "#4682B4", "#9370DB", "#48D1CC", "#5F9EA0"]

turtle = Turtle()
turtle.shape("circle")
turtle.shapesize(0.3)
turtle.speed("fastest")
turtle.pensize(2)

current_position = turtle.heading()
step = 5


for x in range(0, int(360 / step)):
    turtle.pencolor(random.choice(colors))
    turtle.circle(100)
    turtle.setheading(turtle.heading() + step)


screen = Screen()
screen.exitonclick()