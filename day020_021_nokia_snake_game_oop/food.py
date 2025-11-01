from turtle import Turtle
import random as R


class Food(Turtle):
    def __init__(self, max_radian, min_radian):
        super().__init__()
        """
        Initialize Food class with inherited properties from Turtle class.
        """
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.move_food(max_radian, min_radian)

    def move_food(self, max_radian, min_radian):
        """
        Move food object to random location within specified parameters.

        Parameters:
            max_radian: Upper bound of grid, y value.
            min_radian: Lower bound of grid, y value.

        Return:
            None: Relocation Food object.
        """
        location = [R.randint(min_radian, max_radian) for _ in range(2)]
        self.goto(*location)
