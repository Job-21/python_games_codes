from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from score_board import ScoreBoard
screen = Screen()
screen.setup(width=900, height=600)
screen.listen()
screen.bgcolor("black")
screen.title("JOB'S PYTHON")
screen.tracer(0)

snake = Snake()
turtle_food = Food()
total_score = ScoreBoard()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.new_created_turtles[0].distance(turtle_food) < 15:
        turtle_food.refresh()
        snake.extend()
        total_score.increase_score()


    if snake.new_created_turtles[0].xcor() < -440 or snake.new_created_turtles[0].xcor() > 440 or snake.new_created_turtles[0].ycor() > 298 or snake.new_created_turtles[0].ycor() < -298:
        total_score.game_over()
        game_is_on = False

    for segment in snake.new_created_turtles:
        if segment == snake.new_created_turtles[0]:
            pass
        elif snake.new_created_turtles[0].distance(segment) < 10:
            game_is_on = False
            total_score.game_over()





screen.exitonclick()