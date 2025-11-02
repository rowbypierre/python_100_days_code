from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.run = 10
        self.rise = 10

    def move(self):
        """
        Move ball diagonally across grid.
        """
        self.goto(super().xcor() + self.run, super().ycor() + self.rise)

    def bounce_high(self):
        """
        Reverse ball vertical direction.
        """
        self.rise *= -1

    def bounce_long(self):
        """
        Reverse ball horizontal direction.
        """
        self.run *= -1

    def center(self):
        """
        Teleport ball to center screen.
        """
        self.teleport(x=0, y=0)

    def speed_up(self):
        """
        Speed ball up by 25 percent.
        """
        self.run *= 1.25

    def reset_speed(self):
        """
        Reset ball speed.
        """
        self.run = 10
