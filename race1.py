import turtle
from turtle import Turtle, Screen
import random
screen = Screen()
screen.title("JOBBY'S TURTLES RACE GAME")
screen.bgcolor("black")


def play():
    screen.listen()
    # turtle.hideturtle()
    screen.setup(width=700, height=500)
    colors = ["red", "white", "yellow", "green", "blue", "indigo", "pink"]
    position = [-150, -100, -50, 0, 50, 100, 150]
    bet = screen.textinput(title="Place your be", prompt="Which turtle will win the race? Enter color?")
    find = False
    if bet in colors:
        find = True
    else:
        find = False
        style = ("Arial", 13, "bold")
        turtle.color("white")
        turtle.write("Please choose a turtle.", font=style, align="center")

        # screen.onkey(key="p", fun=play())



    new_turtle_list = []
    is_race_on = False
    if bet and find:
        for index in range(0, 6):
            player = Turtle(shape="turtle")
            player.color(colors[index])
            player.penup()
            player.goto(x=-330, y=position[index])
            new_turtle_list.append(player)
        is_race_on = True

    while is_race_on:

        for new_player in new_turtle_list:
            if new_player.xcor() > 310:
                is_race_on = False
                winner = new_player.pencolor()
                if bet == winner:
                    print(f"Well done, {winner} turtle has won. you win.")
                    turtle.color("white")
                    style = ("Arial", 10, "bold")
                    turtle.write(f"Well done, {winner} turtle has won. you win.", font=style, align="center")
                    turtle.hideturtle()

                else:
                    print(f"You lose, {winner} turtle has won.")
                    turtle.color("white")
                    style = ("Arial", 10, "bold")
                    turtle.write(f"You lose, {winner} turtle has won.", font=style, align="center")
                    turtle.hideturtle()
            distance = random.randint(1, 10)
            new_player.forward(distance)

play()


screen.exitonclick()
