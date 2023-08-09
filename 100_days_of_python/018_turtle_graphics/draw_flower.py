from turtle import Turtle, Screen

titi = Turtle()
print(titi)
titi.shape("circle")
titi.speed(9)


def draw_square():
    for _ in range(1, 5):
        titi.left(90)
        titi.forward(100)


def draw_triangle():
    for _ in range(1, 4):
        titi.left(120)
        titi.forward(100)


def turn_right():
    titi.left(270)


def draw_flower():
    for _ in range(1, 5):
        draw_square()
        draw_triangle()
        turn_right()


draw_flower()

titi.left(90)
titi.forward(200)
draw_flower()

screen = Screen()
screen.exitonclick()
