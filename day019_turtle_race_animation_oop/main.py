import turtle as T
import random as R

screen = T.Screen()
screen.setup(800, 800)
turtle_colors = ["red", "pink", "green", "yellow", "blue", "purple"]
R.shuffle(turtle_colors)

get_pick = True
try:
    while get_pick:
        user_choice = (
            screen.textinput(
                title="PICK A WINNER", prompt=f"Which turtle wins: {turtle_colors}?"
            )
            .strip()
            .lower()
        )

        if user_choice in turtle_colors:
            get_pick = not get_pick
        else:
            raise ValueError(f"'{user_choice}' not in {turtle_colors}")
except Exception as error:
    print(f"Error: {error}")

start_positions = [
    (int(screen.window_width() / -2 + 100), y)
    for y in range(
        int(screen.window_height() / -2 + 60),
        int(screen.window_height() / 2),
        int(screen.window_height() / len(turtle_colors)),
    )
]

racing_turtles = []
for pos in start_positions[: len(turtle_colors)]:
    new_turtle = T.Turtle(shape="turtle")
    new_turtle.color(turtle_colors[start_positions.index(pos)])
    new_turtle.shapesize(2)
    new_turtle.penup()
    new_turtle.goto(*pos)
    racing_turtles.append(new_turtle)

start_line_begin = (-260, -400)
drawing_turtle = T.Turtle(shape="turtle")
drawing_turtle.showturtle()
drawing_turtle.setheading(90)
drawing_turtle.teleport(*start_line_begin)
drawing_turtle.pendown()
drawing_turtle.forward(screen.window_height())
drawing_turtle.setheading(270)

racing = True
while racing:
    for turtle in racing_turtles:
        turtle.forward(R.randint(0, 30))

        if turtle.xcor() >= (screen.window_width() / 2):
            win_color = turtle.fillcolor()
            if win_color.lower() == user_choice.lower():
                screen.title(titlestring=f"GOOD PICK: !!!{win_color.upper()} WON!!!")
            else:
                screen.title(titlestring=f"WRONG PICK: !!!{win_color.upper()} WON!!!")

            racing = False

screen.exitonclick()
