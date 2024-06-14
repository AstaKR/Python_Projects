import turtle
from turtle import Turtle, Screen
import pandas as pd
screen = Screen()

def game_postition(x, y):
    pass
image = "blank_states_img.gif"

screen.addshape(image)

state = Turtle()
state.shape(image)
data = pd.read_csv("50_states.csv")
data_state = data["state"].to_list()
guessed_state = []
while len(guessed_state) < 50:
    missing_state = []
    state_input = screen.textinput(f"State Answer {len(guessed_state)} / 50 ", " Enter the state ").title()
    if state_input == "Exit":
        for state in data_state:
            if state not in guessed_state:
                missing_state.append(state)
        missing_state = pd.DataFrame(missing_state)
        missing_state.to_csv("state_to_learn.csv")
        break

    if state_input in data_state:
        guessed_state.append(state_input)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_place = data[data["state"] == state_input]
        t.goto(int(state_place.x), int(state_place.y))
        t.write(state_input)

screen.exitonclick()
