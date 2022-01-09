import random
from turtle import Turtle, Screen

colors = ["green", "yellow", "red", "blue", "purple", "orange"]
screen = Screen()

screen.setup(width=500, height=400)

turtles = []


def init_turtle():
    step = 100
    for i in range(len(colors)):
        turtles.append(Turtle(shape="turtle"))
        turtles[i].color(colors[i])
        turtles[i].color(colors[i])
        turtles[i].penup()
        turtles[i].goto(x=-230, y=step)
        step = step - 25


def run_turtle_race():
    is_race_on = False

    user_bets = screen.textinput(title="Make your bet",
                                 prompt="Which turtle will win the race ? Enter a color: ").lower()
    if user_bets:
        is_race_on = True
    winner = ""
    while is_race_on:
        ran_distance = random.randint(0, 10)
        final_turtle = random.choice(turtles)
        final_turtle.forward(ran_distance)
        position = (final_turtle.position())

        if position[0] > 250:
            winner = final_turtle.color()[0]
            is_race_on = False

    if not user_bets == winner:
        screen.title(f"You Lose, Winner was {winner}")


init_turtle()
run_turtle_race()
screen.exitonclick()
