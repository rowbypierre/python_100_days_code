from food import Food
from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
import time

SCREEN_DIM = 600

max_bound = int(SCREEN_DIM / 2)
min_bound = int(max_bound * -1)

screen = Screen()
screen.title("!!!SNAKE GAME!!!")
screen.bgcolor("black")
screen.setup(width=SCREEN_DIM, height=SCREEN_DIM)
screen.tracer(0)
screen.listen()

snake = Snake(color="white", length=3, start_x=0, shape="square")
food = Food(max_radian=max_bound, min_radian=min_bound)
scoreboard = Scoreboard()

snake_key_function = {
    "Up": snake.head_up,
    "Down": snake.head_down,
    "Left": snake.head_left,
    "Right": snake.head_right,
    "space": screen.bye,
}

for k, f in snake_key_function.items():
    screen.onkeypress(f, k)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    if snake.is_outbound(max_bound, min_bound) or snake.is_tangled():
        game_on = False
        scoreboard.game_over()
    else:
        snake.move()

        if snake.is_food_ate(food.pos()):
            snake.grow_snake()
            food.move_food(max_bound, min_bound)
            scoreboard.score_refresh()

screen.exitonclick()
