import turtle
import turtle as tt
import colorgram as cg
import random as rm

colours = cg.extract("./images/damien_hirst_print.jpg", 21)
# print(colours)

background = colours[0]
# print(background)
rgb_colors = []

for color in colours:
    if color != background:
        r_hue = color.rgb[0]
        g_hue = color.rgb[1]
        b_hue = color.rgb[2]
        color_rgb = (r_hue, g_hue, b_hue)
        rgb_colors.append(color_rgb)
# print(rgb_colors)

# Todo: 1. Create custom window.
turtle.screensize(250, 250)
print(tt.screensize())

# Todo: 2. Create turtle.
turtle = tt.Turtle()
turtle.color("black")
turtle.shape("turtle")
turtle.speed("fastest")


def turtle_info():
    """
    Returns turtles coordinated position and angle (0 = east).
    """
    print(f"Position:\t{turtle.pos()}"
          f"\nAngle:\t\t{turtle.heading()}")


# Todo: 3. Teleport turtle to start position.
start_x = -200
start_y = -200
turtle.teleport(start_x, start_y)

# Todo: 4. Create 100 dots.
tt.colormode(255)
dots_count = range(1,101)
for dot in dots_count:
    color = rm.choice(rgb_colors)
    turtle.dot(20, color)
    turtle.penup()
    turtle.fd(50)
    turtle.pendown()

    if dot % 10 == 0 and dot != dots_count[-1]:
        elevation = list(turtle.pos())[1]
        elevation += 50
        turtle.teleport(start_x, elevation)
    elif dot == dots_count[-1]:
        turtle.hideturtle()

# Todo: 5. Have screen remain open.
# turtle_info()
tt.exitonclick()
