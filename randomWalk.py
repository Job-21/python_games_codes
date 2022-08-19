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
screen = Screen()
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
while True:
    colors = change_color()
    num = random.choice(list)
    if num % 2 == 0:
        tim.speed(200)
        tim.dot(10)

        tim.width(10)
        tim.color(colors)
        tim.forward(50)
        tim.left(90)
    else:
        tim.speed(200)
        tim.dot(10)
        tim.width(10)
        tim.color(colors)
        tim.forward(50)
        tim.right(90)
screen.exitonclick()
