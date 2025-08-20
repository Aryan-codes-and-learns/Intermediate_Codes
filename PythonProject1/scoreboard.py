from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 240)
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.write(f"Score  {self.score}", move=False, align="center", font=("Arial", 18, "normal"),)


    def increase_score(self):
        self.score += 1
        self.write(f"Score  {self.score}", move=False, align="center", font=("Arial", 20, "normal"), )


    def say_game_over(self):
        self.color("Blue")
        self.goto(0,0)
        self.write("Game Over!",move=False, align="center", font=("Arial", 40, "normal"))