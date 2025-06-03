import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput("Make your bet", "which turtle will win the race? enter a color?")
colors = ["red", "orange", "yellow", "green","blue", "purple"]
turtles = []
next_pos = -120

for color in colors:
    t = Turtle("turtle")
    t.color(color)
    t.penup()
    next_pos += 40
    t.goto(-230,next_pos)
    turtles.append(t)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        turtle_pos = turtle.position()
        if turtle_pos[0] > 215:
            is_race_on = False
            print(f"The {turtle.color()[0]} turtle won!")
            if user_bet == turtle.color()[0]:
                print("You Won!!")
            else:
                print("You lost!")

screen.exitonclick()