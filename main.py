import random
from tkinter import messagebox
from turtle import Turtle, Screen


def randomise_start_positions(turtles):
    random.shuffle(turtles)
    y_coordinate = 200
    for racer in turtles:
        racer.goto(-225, y_coordinate)
        y_coordinate = y_coordinate - 60


def race(turtles):
    while True:
        random.shuffle(turtles)
        for racer in turtles:
            racer.forward(random.randint(0, 10))
            if racer.xcor() >= 225:
                return racer


def create_turtle(colour):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colour)
    return new_turtle


if __name__ == '__main__':

    s = Screen()
    s.setup(width=500, height=500)
    user_bet = s.textinput(title="Place your bet!", prompt="Choose your turtle - Red, Yellow, Blue, Green, Black, "
                                                           "or Brown. Which turtle will win? ").lower()
    colours = ["red", "yellow", "blue", "green", "black", "purple", "brown"]
    racing_turtles = [create_turtle(colour) for colour in colours]
    randomise_start_positions(racing_turtles)
    winner = race(racing_turtles).color()[0]
    winner_name = str(winner).capitalize()
    if winner == user_bet:
        messagebox.showinfo("Winner", f"{winner_name} turtle won!")
    else:
        messagebox.showinfo("Loser", f"{winner_name} turtle won!")
    s.exitonclick()
