# import colorgram
# rgb = []
# colors = colorgram.extract("download.jpg", 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     my_colors = (r, g, b)
#     rgb.append(my_colors)
#
# print(rgb)
import turtle
import random
turtle.colormode(255)


colors = [(248, 246, 236), (237, 250, 244), (251, 239, 248), (236, 243, 250), (233, 222, 92), (211, 158, 105), (116, 177, 210), (226, 57, 131), (181, 78, 33), (210, 135, 174)]
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.backward(250)
tim.right(90)
tim.forward(230)
tim.left(90)
screen = turtle.Screen()
def draw():
    for i in range(10):
        tim.dot(30, random.choice(colors))
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)

for i in range(10):
    draw()




screen.exitonclick()
