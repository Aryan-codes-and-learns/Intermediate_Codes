from turtle import Turtle

FONT = ("Courier", 18, "normal")

class LevelBoard(Turtle):

    # Defining the scoreboard
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-240, 240)
        self.level = 0  # Keeping track of the score.
        self.color("black")
        self.write(f"Level: {self.level}", move=False, align="center", font=FONT)

    # Increasing score
    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", move=False, align="center", font=FONT)

    # A little ending screen when the car hits the turtle
    def say_game_over(self):
        self.goto(0,-50)
        self.write(f"GAME OVER! You reached a level of {self.level}", move=False, align="center", font=("Courier", 20, "normal"))