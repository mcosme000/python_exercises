from turtle import Turtle, Screen


my_turtle = Turtle()
my_turtle.shape("circle")
my_turtle.pensize(2)


def draw_dashed_line(value):
    for _ in range(1, value + 1):
        my_turtle.pu()
        my_turtle.forward(10)
        my_turtle.pd()
        my_turtle.forward(10)


draw_dashed_line(50)


screen = Screen()
screen.exitonclick()
