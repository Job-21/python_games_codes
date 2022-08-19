from turtle import Turtle, Screen
import random
colors = ["red", "black", "yellow", "green", "blue", "indigo", "violet"]

tim = Turtle()
tim.penup()
tim.shape("turtle")
tim.color(colors[3])
tim.goto(x=-280, y=-100)


ted = Turtle(shape="turtle")
ted.color(colors[0])
ted.penup()
ted.goto(x=-280, y=0)

tad = Turtle(shape="turtle")
tad.penup()
tad.color(colors[1])
tad.goto(x=-280, y=100)

tod = Turtle(shape="turtle")
tod.penup()
tod.color(colors[2])
tod.goto(x=-280, y=200)
my_count = [1, 2, 4, 2, 50, 7]
while True:
    tim_no = random.choice(my_count)
    tim.forward(tim_no)

    ted_no = random.choice(my_count)
    ted.forward(ted_no)

    tod_no = random.choice(my_count)
    tod.forward(tod_no)

    tad_no = random.choice(my_count)
    tad.forward(tad_no)

screen = Screen()


screen.setup(width=600, height=500)
# tim.penup()


screen.listen()

screen.exitonclick()
