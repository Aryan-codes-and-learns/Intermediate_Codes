from turtle import Turtle, Screen
import time

screen = Screen()
class Paddle(Turtle):

    def __init__(self, position):  # Defining the shape, size, color and starting positions of the two platforms.
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)


    def go_up(self):  # Function to make a platform move upwards
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)
        screen.update()
        time.sleep(0.01)

    def go_down(self):  # Function to make a platform move downwards
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
        screen.update()
        time.sleep(0.01)
