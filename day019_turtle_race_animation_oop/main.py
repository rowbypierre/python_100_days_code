import turtle as tt
import random as rm

screen = tt.Screen()
width = 800
height = 800
screen.setup(width=width, height=height)
colors = ["red", "pink", "green", "yellow", "blue", "purple"]
rm.shuffle(colors)
user_choice = screen.textinput(title=f"PICK A WINNER", prompt=f"Which turtle win {tuple(colors)}?")
# print(user_choice)

turtles = []
gap = height / len(colors)
start_pos_x = - 1 * (height / 2) + gap / 2
start_pos_y = - 1 * (height / 2) + gap / 1.8

for turtle in range(1, 7):
    count = turtle
    if count > 1:
        start_pos_y += gap

    color = colors[count - 1]

    turtle = tt.Turtle(shape="turtle")
    turtle.color(color)
    turtle.shapesize(2)
    turtle.penup()
    turtle.goto(x=start_pos_x, y=start_pos_y)

    turtles.append({
        "object_id": turtle,
        "color": color
    })

drawing_turtle = tt.Turtle(shape="turtle")
drawing_turtle.showturtle()
drawing_turtle.setheading(90)
start_line_begin = (start_pos_x + (gap / 2), start_pos_x - (gap / 4))
drawing_turtle.teleport(x=start_line_begin[0], y=start_line_begin[1])
drawing_turtle.pendown()
drawing_turtle.forward(start_line_begin[1] * -2 - (gap / 100))

racing = True
while racing:
    for turtle in turtles:
        turtle["object_id"].forward(rm.randint(0, 30))
        # print(turtle)
        if turtle["object_id"].xcor() >= (width / 2 - gap / 4):
            winner = turtle["color"].upper()
            if winner.lower() == user_choice.lower():
                screen.title(titlestring=f"GOOD PICK: !!!{winner} WON!!!")
            else:
                screen.title(titlestring=f"WRONG PICK: !!!{winner} WON!!!")
            racing = False
            break

tt.exitonclick()
