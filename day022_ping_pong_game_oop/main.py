from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from game_screen import make_table, ball_in_black


r_paddle = Paddle(x_cor=375, y_cor=0)
l_paddle = Paddle(x_cor=-382, y_cor=0)
ball = Ball()
scoreboard = Scoreboard(graph_x=0, graph_y=240, win_score=1)
screen = make_table(r_paddle, l_paddle)


game_on = True
while game_on:
    ball.center()
    ball.reset_speed()
    ball.bounce_long()
    while ball_in_black(r_paddle, l_paddle, ball):
        time.sleep(0.05)
        ball.move()

        if ball.ycor() >= 290 or ball.ycor() <= -280:
            ball.bounce_high()
        elif (
            (r_paddle.distance(ball) <= 30 and ball.run > 0)
            or (
                r_paddle.distance(ball) <= 50
                and ball.xcor() >= r_paddle.xcor() - 30
                and ball.run > 0
            )
            or (l_paddle.distance(ball) <= 30 and ball.run < 0)
            or (
                l_paddle.distance(ball) <= 50
                and ball.xcor() <= l_paddle.xcor() + 30
                and ball.run < 0
            )
        ):
            ball.bounce_long()
            ball.speed_up()

        if not ball_in_black(r_paddle, l_paddle, ball):
            if ball.xcor() > 0:
                scoreboard.add_score("left")
            else:
                scoreboard.add_score("right")

    game_on = not scoreboard.check_winner()

screen.exitonclick()
