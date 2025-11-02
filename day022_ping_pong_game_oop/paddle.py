from turtle import Turtle

VERTICAL_LIMITS = [250, -250]


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        super().shape("square")
        super().hideturtle()
        super().color("white")
        super().penup()
        super().teleport(x=x_cor, y=y_cor)
        super().setheading(90)
        super().turtlesize(stretch_len=5)
        super().speed("fastest")
        super().showturtle()

    def paddle_up(self):
        """
        Summary: Move paddle north/ up.
        """
        if super().ycor() < VERTICAL_LIMITS[0]:
            super().forward(25)

    def paddle_down(self):
        """
        Summary: Move paddle south/ down.
        """
        if super().ycor() > VERTICAL_LIMITS[1]:
            super().backward(25)
