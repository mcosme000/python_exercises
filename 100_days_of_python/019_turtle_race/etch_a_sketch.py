from turtle import Turtle, Screen

# W = FORWARDS
# S = BACKWARDS
# A = COUNTER-CLOCKWISE
# D = CLOCKWISE

turtle = Turtle()
screen = Screen()
tortuga = Turtle()

turtle.shapesize(5)
turtle.pensize(5)


def forwards():
    turtle.forward(10)


def backwards():
    turtle.backward(10)


def counter():
    turtle.left(10)


def clockwise():
    turtle.left(-10)


def reset():
    turtle.reset()
    turtle.shapesize(5)
    turtle.pensize(5)


screen.onkey(forwards, "w")
screen.onkey(backwards, "s")
screen.onkey(counter, "a")
screen.onkey(clockwise, "d")
screen.onkey(turtle.penup, "p")
screen.onkey(turtle.pendown, "o")
screen.onkey(reset, "c")
screen.listen()

screen.exitonclick()
