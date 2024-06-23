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
        Summary:    Move ball diagonally across grid.
        """
        new_xcor = self.xcor() + self.run
        new_ycor = self.ycor() + self.rise
        self.goto(new_xcor, new_ycor)

    def bounce_y(self):
        """
        Summary:    Reverse ball vertical direction.
        """
        self.rise *= -1

    def bounce_x(self):
        """
        Summary:    Reverse ball horizontal direction.
        """
        self.run *= -1

    def center(self):
        """
        Summary:    teleport ball to center screen.
        """
        self.teleport(x=0, y=0)

    def speed_up(self):
        """
        Summary:    Speed ball up by 25 percent.
        """
        self.run *= 1.25

    def reset_speed(self):
        """
        Summary:    Reset ball speed.
        """
        self.run = 10


