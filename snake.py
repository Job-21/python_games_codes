from turtle import Turtle, Screen
POSITION  = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270

class Snake:

    def __init__(self):
        self.new_created_turtles = []
        self.create_snake()

    def create_snake(self):
        for coordinate in POSITION:
            self.add_segment(coordinate)

    def add_segment(self, coordinate):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(coordinate)
        self.new_created_turtles.append(new_turtle)

    def extend(self):
        self.add_segment(self.new_created_turtles[-1].position())

    def move(self):
        for num in range(len(self.new_created_turtles) - 1, 0, -1):
            new_x = self.new_created_turtles[num - 1].xcor()
            new_y = self.new_created_turtles[num - 1].ycor()
            self.new_created_turtles[num].goto(new_x, new_y)
        self.new_created_turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.new_created_turtles[0].heading() != DOWN:
            self.new_created_turtles[0].setheading(UP)

    def right(self):
        if self.new_created_turtles[0].heading() != LEFT:
            self.new_created_turtles[0].setheading(RIGHT)

    def left(self):
        if self.new_created_turtles[0].heading() != RIGHT:
            self.new_created_turtles[0].setheading(LEFT)

    def down(self):
        if self.new_created_turtles[0].heading() != UP:
            self.new_created_turtles[0].setheading(DOWN)

