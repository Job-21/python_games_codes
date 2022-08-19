from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
tim.shape("turtle")
screen.setup(width=1000, height=600)


def move_forward():
    tim.pendown()
    tim.forward(50)


def clear_turtle():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def move_up():

    tim.up()


def turn_left():

    tim.left(10)


def turn_right():

    tim.right(10)


screen.listen()
screen.onkey(key="f", fun=move_forward)
screen.onkey(key="c", fun=clear_turtle)
screen.onkey(key="l", fun=turn_left)
screen.onkey(key="r", fun=turn_right)
screen.exitonclick()
