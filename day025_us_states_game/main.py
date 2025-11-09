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
print(data)

all_guess = []
game_on = len(all_guess) < 50
while game_on:
    guess = screen.textinput(f"{len(all_guess)}/50 States Correct", "Enter another state:").lower().strip().title()

    if guess in data.state.values and guess not in all_guess:
        all_guess.append(guess)
        record = data.loc[data.state == guess].iloc[0]
        point = (int(record.x), int(record.y))

        label_turtle = turtle.Turtle(shape="circle")
        label_turtle.speed("slowest")
        label_turtle.shapesize(0.3, 0.3)
        label_turtle.penup()
        label_turtle.goto(*point)
        label_turtle.write(guess, font=("Arial", 8, "normal"))
        label_turtle.hideturtle()


screen.mainloop()
