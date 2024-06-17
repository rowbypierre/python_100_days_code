from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, color, length, shape, start_xcor):
        self.color = color
        self.length = length
        self.shape = shape
        self.start_xcor = start_xcor
        self.snake = []
        self.make_snake()
        self.snake_head = self.snake[0]

    def make_snake(self):
        """
        Make three 20x20 snake segments along the X axis headed east.
        """
        for snake_part in range(3):
            snake_part = Turtle()
            snake_part.penup()
            snake_part.color(self.color)
            snake_part.shape(self.shape)
            snake_part.setx(x=self.start_xcor)
            self.start_xcor -= 20
            self.snake.append(snake_part)

    def add_snake_part(self):
        """
        Create 1 snake segment by cloning the last segment.
        """
        new_snake_part = self.snake[-1].clone()
        self.snake.append(new_snake_part)

    def move(self):
        """
        Move snake segments seamlessly with each segment moving to the coordinate of the segment ahead.
        """
        for snake_part in range(len(self.snake) - 1, 0, -1):
            new_lat = self.snake[snake_part - 1].xcor()
            new_long = self.snake[snake_part - 1].ycor()
            self.snake[snake_part].goto(x=new_lat, y=new_long)
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        """
        Turn snake head north if not facing south.
        """
        if self.snake_head.heading() != UP + 180:
            self.snake_head.seth(UP)

    def down(self):
        """
        Turn snake head south if not facing north.
        """
        if self.snake_head.heading() != DOWN - 180:
            self.snake_head.seth(DOWN)

    def left(self):
        """
        Turn snake head west if not facing east.
        """
        if self.snake_head.heading() != LEFT - 180:
            self.snake_head.seth(LEFT)

    def right(self):
        """
        Turn snake head east if not facing west.
        """
        if self.snake_head.heading() != RIGHT + 180:
            self.snake_head.seth(RIGHT)
