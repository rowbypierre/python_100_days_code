import food
from turtle import Screen
from snake import Snake
import scoreboard
import time

SCREEN_LENGTH = 600

screen = Screen()
screen.title("!!!SNAKE GAME!!!")
screen.bgcolor("black")
screen.setup(width=SCREEN_LENGTH, height=SCREEN_LENGTH)
positive_border = SCREEN_LENGTH / 2
negative_border = positive_border * -1
screen.tracer(0)
screen.listen()

snake = Snake(color="white", length=3, start_xcor=0, shape="square")
food = food.Food(high_limit=positive_border, low_limit=negative_border)
scoreboard = scoreboard.Scoreboard()

screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.down, key="Down")
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.right, key="Right")
screen.onkeypress(fun=screen.bye, key="space")


def food_ate():
    """
    Return "True" when head of snake is 15 or less pixels away from food.
    """
    if snake.snake_head.distance(food) < 15:
        return True


def not_at_outer_limit():
    """
    Return "True" when head of snake is at or exceeded lateral and horizontal limits else "False".
    """
    if snake.snake_head.xcor() >= positive_border or snake.snake_head.xcor() <= negative_border:
        return False
    elif snake.snake_head.ycor() >= positive_border or snake.snake_head.ycor() <= negative_border:
        return False
    else:
        return True


def head_meets_tail():
    """
    Return "True" if snake head contacts another snake segment.
    """
    for segment in snake.snake[1:]:
        if snake.snake_head.distance(segment) < 10:
            return True


game_on = True
while game_on:
    screen.update()
    time.sleep(.1)

    if not_at_outer_limit() is False or head_meets_tail():
        game_on = False
        scoreboard.game_over()
    else:
        snake.move()
        if food_ate():
            snake.add_snake_part()
            food.move_food(high_limit=positive_border, low_limit=negative_border)
            scoreboard.score_refresh()

screen.exitonclick()
