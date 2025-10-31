import turtle as T
import colorgram as CG
import random as RM

colours = CG.extract("./images/damien_hirst_print.jpg", 21)
background = colours[0]
rgb_colors = [
    (color.rgb[0], color.rgb[1], color.rgb[2])
    for color in colours
    if color != background
]

# Todo: 1. Create custom window.
screen = T.Screen()
screen.setup(width=700, height=700)
screen.screensize(250, 250)
screen.colormode(255)

# Todo: 2. Create turtle.
turtle = T.Turtle(shape="turtle")
turtle.color("black")
turtle.speed("fastest")


# Todo: 3. Teleport turtle to start position.
start_xy = (-200, -200)
turtle.teleport(*start_xy)

# Todo: 4. Create 100 dots.
elevation = 50
all_dots = range(1, 101)
for dot in all_dots:
    color = RM.choice(rgb_colors)
    turtle.dot(20, color)
    turtle.penup()
    turtle.fd(50)
    turtle.pendown()

    if dot == all_dots[-1]:
        turtle.hideturtle()
    elif dot % 10 == 0:
        turtle.teleport(start_xy[0], turtle.pos()[1] + elevation)

# Todo: 5. Have screen remain open.
screen.exitonclick()
