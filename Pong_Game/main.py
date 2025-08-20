from turtle import Screen, Turtle
from paddles import Paddle
from aesthetics import Additional
from ScoreBoard import Scoreboard
from ball import Ball
import time
import random

screen = Screen()   # Setting the Screen
screen.setup(1200,550)
screen.bgcolor("black")

screen.tracer(0)  # for animation

left_paddle = Paddle(position=(-550, 0))    # The two platforms that we play with.
right_paddle = Paddle(position=(550, 0))

net = Additional()  # The middle line
net.create_net()
screen.update()

border = Additional()  # walls.
border.create_border()
screen.update()
ball = Ball()

scoreboard = Scoreboard()  # A scoreboard to keep track of the points

screen.listen()   # Controls
screen.onkey(key="w", fun=left_paddle.go_up)
screen.onkey(key="s", fun=left_paddle.go_down)
screen.onkey(key="Up", fun=right_paddle.go_up)
screen.onkey(key="Down", fun=right_paddle.go_down)

# The possible angles (which the ball could be heading)
angles = [
    -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20,
    20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160,
    200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210
]

heading_direction = random.choice(angles)   # So that it is different in every round
ball.setheading(heading_direction)

left_user_score = 0   # Score
right_user_score = 0

game_is_on = True
while game_is_on:

    ball.move()  # A function to move the ball in the x-axis and the y-axis
    screen.update()
    time.sleep(0.001)   # Delay (lower means faster. Hence, looks smoother)

    if ball.ycor() > 240 or ball.ycor() < -250:   # Collision with the top/bottom wall.
        ball.bounce()

    if ball.xcor() > 590 or ball.xcor() < -590:  # Checking to see if any player misses and loses points
        if ball.xcor() > 590:
            left_user_score += 1
            heading_direction = random.choice(angles[22:])
            scoreboard.clear()
            scoreboard.increase_score_left()   # Increasing score
        elif ball.xcor() < -590:
            right_user_score += 1
            heading_direction = random.choice(angles[:22])
            scoreboard.clear()
            scoreboard.increase_score_right()

        time.sleep(2)  # A little delay so that things don't go too fast.
        ball.goto(0,0)

    # Collision with the right paddle
    if ball.xcor() > 530 and (right_paddle.ycor() - 55) < ball.ycor() < (right_paddle.ycor() + 55):
        ball.reflect()

    # Collision with the left paddle
    if ball.xcor() < -530 and (left_paddle.ycor() - 55) < ball.ycor() < (left_paddle.ycor() + 55):
        ball.reflect()


    # The game will end if either player reaches 3 points. The first one to do so wins.
    if scoreboard.score_right == 3 or scoreboard.score_left == 3:
        if scoreboard.score_left == 3:
            scoreboard.game_over("left")
        elif scoreboard.score_right == 3:
            scoreboard.game_over("right")

        game_is_on = False

screen.exitonclick()