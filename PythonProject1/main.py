import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(550, 550)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
snake.create_snake()

food = Food()

scoreboard = Scoreboard()

screen.listen()

screen.onkey(key="w", fun=snake.up)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="d", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.075)
    snake.move_snake()

    upper_estimated_x_of_food = food.xcor() + 10
    lower_estimated_x_of_food = food.xcor() - 10
    upper_estimated_y_of_food = food.ycor() + 10
    lower_estimated_y_of_food = food.ycor() - 10

    if upper_estimated_x_of_food > snake.head.xcor() > lower_estimated_x_of_food and upper_estimated_y_of_food > snake.head.ycor() > lower_estimated_y_of_food:
        food.hideturtle()
        snake.new_snake()
        food = Food()
        scoreboard.clear()
        scoreboard.increase_score()


    for number in range(1, len(snake.full_snake)):
        upper_x = snake.full_snake[number].xcor() + 5
        lower_x = snake.full_snake[number].xcor() - 5
        upper_y = snake.full_snake[number].ycor() + 5
        lower_y = snake.full_snake[number].ycor() - 5
        if upper_x > snake.head.xcor() > lower_x and upper_y > snake.head.ycor() > lower_y:
            game_is_on = False


    if snake.head.xcor() > 270 or snake.head.xcor() < -270:
        game_is_on = False
    if snake.head.ycor() > 270 or snake.head.ycor() < -270:
        game_is_on = False

scoreboard.say_game_over()
screen.exitonclick()
