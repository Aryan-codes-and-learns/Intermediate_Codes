from turtle import Turtle
import time


class Scoreboard(Turtle):

    # Defining the scoreboard
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.score_left = 0  # Keeping track of the score.
        self.score_right = 0
        self.color("white")
        self.write(f"{self.score_left} : {self.score_right}", move=False, align="center", font=("Arial", 25, "normal"))

    # Increasing score for the left player
    def increase_score_left(self):
        self.score_left += 1
        self.write(f"{self.score_left} : {self.score_right}", move=False, align="center", font=("Arial", 25, "normal"))

    # Increasing score for the right player.
    def increase_score_right(self):
        self.score_right += 1
        self.write(f"{self.score_left} : {self.score_right}", move=False, align="center", font=("Arial", 25, "normal"))

    # A little ending screen when a player wins.
    def game_over(self, winner):
        self.goto(0,-50)
        if winner == "left":
            self.write(f"LEFT      WINS!", align="center", move=False, font=("Arial", 60, "normal" ))
        elif winner == "right":
            self.write(f"RIGHT     WINS!", align="center", move=False, font=("Arial", 60, "normal"))