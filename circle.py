import random
import turtle
from turtle import Turtle, Screen
# colors = ["red", "blue", "black", "yellow", "violet", "red", "pink", "green"]
turtle.colormode(255)


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple


tim = Turtle()

tim.speed("fastest")
def draw(size):
    for i in range(int(360 / size)):
        tim.color(change_color())
        tim.circle(100)

        tim.setheading(tim.heading() + size)

draw(20)




screen = Screen()
screen.exitonclick()
