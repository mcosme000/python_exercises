from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


turtle.shape("circle")
turtle.shapesize(1)
turtle.pensize(5)


def move_right():
    turtle.setheading(0)
    turtle.forward(20)


def move_up():
    turtle.setheading(90)
    turtle.forward(20)


def move_left():
    turtle.setheading(180)
    turtle.forward(20)


def move_down():
    turtle.setheading(270)
    turtle.forward(20)


screen.onkey(move_right, "j")
screen.onkey(move_left, "h")
screen.onkey(move_up, "u")
screen.onkey(move_down, "n")
screen.listen()

screen.exitonclick()
