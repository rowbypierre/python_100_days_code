import turtle as T

screen = T.Screen()
screen.setup(height=500, width=500)
screen.title(titlestring="!!!USE KEYBOARD AND DRAW ON SKETCH PAD!!!")

turtle = T.Turtle(shape="classic")
turtle.speed("fastest")


def angle_adjust(adjustment):
    turtle.setheading(turtle.heading() + adjustment)


def move_front():
    turtle.forward(10)


def move_back():
    turtle.backward(10)


def turn_right():
    angle_adjust(-5)


def move_right():
    turn_right()
    move_front()


def turn_left():
    angle_adjust(5)


def move_left():
    turn_left()
    move_front()


def reset_canvas():
    turtle.reset()


def close_canvas():
    screen.bye()


screen.onkeypress(fun=move_front, key="w")
screen.onkeypress(fun=move_back, key="s")
screen.onkeypress(fun=turn_left, key="a")
screen.onkeypress(fun=move_left, key="q")
screen.onkeypress(fun=turn_right, key="d")
screen.onkeypress(fun=move_right, key="e")
screen.onkeypress(fun=reset_canvas, key="z")
screen.onkeypress(fun=close_canvas, key="space")

screen.listen()
screen.mainloop()