from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.score = 0
        style = ("Courier", 15, "bold")
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.clear()
        self.write(f"Score : {self.score}", font=style, align="center")
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        style = ("Courier", 25, "bold")
        self.write("GAME OVER", font=style, align="center")

    def increase_score(self):
        self.score += 1
        style = ("Courier", 15, "bold")
        self.clear()
        self.write(f"Score : {self.score}", font=style, align="center")
