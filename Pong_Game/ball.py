from turtle import Turtle

class Ball(Turtle):

    # Defining the characteristics of the ball
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 1  # how much it moves forward/backward
        self.y_move = 1  # how much it moves upward, downward.

    # A function to keep the ball moving.
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # A function to bounce the ball off once it collides with the wall.
    def bounce(self):
        self.y_move *= -1

    # A function to bounce the ball off once it collides with the platform.
    def reflect(self):
        self.x_move *= -1

