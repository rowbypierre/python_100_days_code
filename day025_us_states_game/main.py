import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Name the States")
map_image = "blank_states_img.gif"
screen.addshape(map_image)
turtle.shape(map_image)

datafile = "50_states.csv"
data = pandas.read_csv(datafile)

states_guessed = []
is_guessing = len(states_guessed) < 50
while is_guessing:
    state_guess = (
        screen.textinput(
            f"{len(states_guessed)}/50 States Correct", "Enter another state:"
        )
        .lower()
        .strip()
        .title()
    )

    if state_guess == "Exit":
        is_guessing = False

        states_missed = data[~data.state.isin(states_guessed)].state
        states_missed.to_csv("./study.csv", index=False)
    elif state_guess in data.state.values and state_guess not in states_guessed:
        states_guessed.append(state_guess)
        record = data.loc[data.state == state_guess].iloc[0]
        map_point = (int(record.x), int(record.y))

        label_turtle = turtle.Turtle(shape="circle")
        label_turtle.speed("slowest")
        label_turtle.shapesize(0.3, 0.3)
        label_turtle.penup()
        label_turtle.goto(*map_point)
        label_turtle.write(state_guess, font=("Arial", 8, "normal"))
        label_turtle.hideturtle()
