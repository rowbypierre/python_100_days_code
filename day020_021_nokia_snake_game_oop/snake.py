from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, color, length, shape, start_x):
        self.color = color
        self.length = length
        self.shape = shape
        self.start_x = start_x
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
            snake_part.setx(x=self.start_x)
            self.start_x -= 20
            self.snake.append(snake_part)

    def grow_snake(self):
        """
        Create 1 snake segment by cloning the last segment.
        """
        new_segment = self.snake[-1].clone()
        self.snake.append(new_segment)

    def move(self):
        """
        Move snake segments seamlessly with each segment moving to the coordinate of the segment ahead.
        """
        for snake_part in range(len(self.snake) - 1, 0, -1):
            segment_infront = self.snake[snake_part - 1]
            self.snake[snake_part].goto(*segment_infront.pos())

        self.snake[0].forward(MOVE_DISTANCE)

    def head_up(self):
        """
        Turn snake head north if not facing south.
        """
        if self.snake_head.heading() != DOWN:
            self.snake_head.seth(UP)

    def head_down(self):
        """
        Turn snake head south if not facing north.
        """
        if self.snake_head.heading() != UP:
            self.snake_head.seth(DOWN)

    def head_left(self):
        """
        Turn snake head west if not facing east.
        """
        if self.snake_head.heading() != RIGHT:
            self.snake_head.seth(LEFT)

    def head_right(self):
        """
        Turn snake head east if not facing west.
        """
        if self.snake_head.heading() != LEFT:
            self.snake_head.seth(RIGHT)

    def is_food_ate(self, food_location):
        """
        Validate (bool) when snake head <= 15 pixels away from food.
        """
        return self.snake_head.distance(food_location) < 15
    
    def is_outbound(self, max_radian, min_radian):
        """
        Validate (bool) if snake head is at or exceeded lateral and horizontal limits.
        """
        if self.snake_head.xcor() >= max_radian \
            or self.snake_head.xcor() <= min_radian \
            or self.snake_head.ycor() >= max_radian \
            or self.snake_head.ycor() <= min_radian:
            return True
        else:
            return False
        
    def is_tangled(self):
        """
        Confirms (bool) if snake head contacts another snake segment.
        """
        contact = False
        for segment in self.snake[1:]:
            if self.snake_head.distance(segment) < 10:
                contact = True
        
        return contact
