from turtle import Turtle

STARTING_POSITION = (0, -255)
MOVE_DISTANCE = 10


class Player(Turtle):

    # Defines the player's turtle and sends it to the starting position.
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("turtle")
        self.setheading(90)
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.showturtle()

    # A function to move the turtle
    def move(self):
        self.goto(self.xcor(), (self.ycor() + MOVE_DISTANCE))

    # Once the turtle completes one level, it is sent back to the starting position.
    def goes_back_to_the_starting_position(self):
        self.goto(STARTING_POSITION)
