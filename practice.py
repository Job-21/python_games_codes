# import heroes
#
# print(heroes.gen())
from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()

colors = ["red", "blue", "black", "yellow", "violet", "red", "pink", "green"]
def draw(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(80)
        tim.left(angle)


for shape in range(3, 11):
    tim.color(random.choice(colors))
    draw(shape)


screen.exitonclick()