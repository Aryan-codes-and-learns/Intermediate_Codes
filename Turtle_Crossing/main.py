import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import LevelBoard

screen = Screen()
screen.setup(width=600, height=550)  # Setting the screen
screen.tracer(0)

# Creating Objects
turtle = Player()
car_manager = CarManager()
level = LevelBoard()

# Setting the controls
screen.listen()
screen.onkey(key="Up", fun= turtle.move)

loops = 6  # A variable that decides if a new car is created or not

game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Animation
    screen.update()

    # If the turtle makes it to the other side. It will be sent back to the starting point, with a higher difficulty.
    if turtle.ycor() > 260:
        turtle.goes_back_to_the_starting_position()
        car_manager.increase_level()
        level.increase_level()

    # A car will only be created once every 6 loops (the variable increases by 1 each time).
    # This is done so that it isn't too fast for the player.
    if loops % 6 == 0:
        car_manager.create_cars()

    # Detecting Collisions with the car.
    for each in car_manager.all_cars:
        if (int(each.xcor()) - 20) < int(turtle.xcor()) < (int(each.xcor()) + 20) and (int(each.ycor()) - 13) < int(turtle.ycor()) < (int(each.ycor()) + 13):
            game_is_on = False
            level.say_game_over()

    car_manager.move_left()  # moves the car leftwards
    loops += 1
    
screen.exitonclick()