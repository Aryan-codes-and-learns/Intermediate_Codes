from operator import index
from turtle import Screen, Turtle
screen = Screen()
import time
STARTING_POSITIONS = [(-20,0), (-40,0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

snake_head = Turtle(shape="square")
snake_head.color("white")
snake_head.penup()

class Snake:

    def __init__(self):
        self.full_snake = [snake_head]
        self.create_snake()
        self.head = self.full_snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_tiny_snake = Turtle(shape="square")
            new_tiny_snake.color("white")
            new_tiny_snake.penup()
            new_tiny_snake.goto(position)
            self.full_snake.append(new_tiny_snake)

    def new_snake(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        self.full_snake.append(new_segment)


    def move_snake(self):

        for follow in range(len(self.full_snake)-1, 0, -1):
            new_x = self.full_snake[follow-1].xcor()
            new_y = self.full_snake[follow-1].ycor()
            self.full_snake[follow].goto(new_x,new_y)
        self.full_snake[0].forward(MOVE_DISTANCE)


    def right(self):
        if self.head.heading() != LEFT:
            self.full_snake[0].setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.full_snake[0].setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.full_snake[0].setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.full_snake[0].setheading(DOWN)
