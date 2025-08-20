from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 5  # The cars become faster in each level


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.moving_distance = 5  # The moving distance of each car in level 1.
        self.all_cars = []
        self.hideturtle()

    def create_cars(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.turtlesize(stretch_wid=1, stretch_len=2)  # Makes the square look like a car
        new_car.color(random.choice(COLORS))    # Gives the car a certain color
        random_y = random.randint(-220, 220)  # Places it on a random location on the y-axis at the screen's right edge.
        new_car.goto(300, random_y)  # Sends each car to that location.
        self.all_cars.append(new_car)

    def move_left(self):
        for car in self.all_cars:
            car.backward(self.moving_distance)  # Moves them towards the left

    def increase_level(self):
        self.moving_distance += MOVE_INCREMENT  # Increases the speed of the car by 5 every time the level is increased.