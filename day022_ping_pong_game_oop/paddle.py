from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.color("white")
        self.penup()
        self.teleport(x=x_cor, y=y_cor)
        self.setheading(90)
        self.turtlesize(stretch_len=5)
        self.speed("fastest")
        self.showturtle()

    def paddle_up(self):
        """
        Summary:    Move paddle north/ up.
        """
        if self.ycor() < 250:
            self.forward(25)

    def paddle_down(self):
        """
        Summary:    Move paddle south/ down.
        """
        if self.ycor() > -250:
            self.backward(25)
