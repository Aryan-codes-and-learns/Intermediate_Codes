from turtle import Turtle, Screen
import time

class Additional(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 5

    # The Middle Line
    def create_net(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 210)
        self.setheading(270)
        self.pensize(5)
        self.pencolor("white")
        for i in range(0, 16):
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)

    # The walls
    def create_border(self):
        self.hideturtle()
        self.penup()
        self.goto(-600, 235)
        self.pendown()
        self.pensize(10)

        for i in range(0,2):
            self.pencolor("blue")
            self.forward(1200)
            self.right(90)
            self.pencolor("red")
            self.forward(510)
            self.right(90)

    # I created another animation for the start sequence where it counts down from 5. and says GO!
    # The game would start after this sequence.
    # However, my turtle tab crashes whenever I use it and I don't get to see it anyway.
    # So, I didn't include the animation in the main code. I still kept the function in though :)
    def start(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,-30)
        for i in range(0,4):
            self.clear()
            time.sleep(1)
            self.write(f"{self.count}", move=False, align="center",
                       font=("Arial", 70, "normal"))
            self.count -= 1

        self.write("GO!", move=False, align="center",
                   font=("Arial", 70, "normal"))
        time.sleep(2)


