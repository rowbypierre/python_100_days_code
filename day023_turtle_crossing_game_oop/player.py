from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        super().penup()
        super().fillcolor("black")
        super().setheading(90)
        self.home()

    def move_up(self):
        "Move turtle forward 10 pixels."
        if super().ycor() < FINISH_LINE_Y:
            super().forward(MOVE_DISTANCE)

    def home(self):
        "Return to start location."
        super().hideturtle()
        super().goto(STARTING_POSITION)
        super().showturtle()

    def has_crossed(self):
        "Confirm (bool) Turtle has reached endpoint."
        return super().ycor() == FINISH_LINE_Y
