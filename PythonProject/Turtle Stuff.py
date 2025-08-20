from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? \nThe participants are "
                                                          "Blue, Red, Green, Pink, Purple. \nEnter a color: ").lower()

colors = ["blue", "red", "green", "pink", "purple"]
y_value = [200, 100, 0, -100, -200]
all_turtles = []

for index_number in range(0, 5):
    tim = Turtle(shape= "turtle")
    tim.color(colors[index_number])
    tim.penup()
    tim.goto(x=-600, y= y_value[index_number])
    all_turtles.append(tim)

referee = Turtle()
referee.hideturtle()
referee.penup()
referee.goto(x= 600, y= 250)
referee.pendown()
referee.right(90)
referee.pensize(10)

def make_screen_pause_for_a_sec():
    referee.penup()
    referee.speed(15)
    referee.circle(50)

for i in range(0,5):
    referee.pencolor("red")
    referee.forward(50)
    referee.pencolor("black")
    referee.forward(50)

if user_bet:
    is_race_on = True

winning_color = ""
make_screen_pause_for_a_sec()

while is_race_on:
    for i in all_turtles:
        if i.xcor() >= 600:
            is_race_on = False
            winning_color = i.pencolor()

    for a in all_turtles:
        a.forward(random.randint(10,25))


if user_bet == winning_color:
    print(f"You WON!! The {winning_color.upper()} turtle is the winner! Congrats")
else:
    print(f"You lost. The {winning_color.upper()} turtle is the winner. Better luck next time!")

make_screen_pause_for_a_sec()
screen.bye()