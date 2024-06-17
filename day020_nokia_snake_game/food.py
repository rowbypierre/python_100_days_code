from turtle import Turtle
import random as r


class Food(Turtle):

    def __init__(self, high_limit, low_limit):
        super().__init__()
        """
        Initialize Food class with inherited properties from Turtle class.
        """
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.move_food(high_limit=high_limit, low_limit=low_limit)

    def move_food(self, high_limit, low_limit):
        """
        Move food object to random coordinate within specified parameters.

        Parameters:
            high_limit: Greatest positive radian.
            low_limit: The Least negative radian.
        """
        high_limit = int(high_limit)
        low_limit = int(low_limit)
        self.goto(x=r.randint(a=low_limit, b=high_limit), y=r.randint(a=low_limit, b=high_limit))


