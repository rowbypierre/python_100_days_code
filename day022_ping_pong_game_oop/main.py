from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
import scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")

r_paddle = Paddle(x_cor=375, y_cor=0)
l_paddle = Paddle(x_cor=-382, y_cor=0)
ball = Ball()
scoreboard = scoreboard.Scoreboard(xcor=0, ycor=240, win_score=1)


screen.listen()
screen.onkeypress(fun=r_paddle.paddle_up, key="Up")
screen.onkeypress(fun=r_paddle.paddle_down, key="Down")
screen.onkeypress(fun=l_paddle.paddle_up, key="w")
screen.onkeypress(fun=l_paddle.paddle_down, key="s")


def screen_delay():
    """
    Summary:    Delay system response by 1/20 of a second.
    """
    time.sleep(.05)


def ball_inbounds():
    """
    Summary:    Return true if ball x coordinates exceeds that of right or left paddle.
    """
    if r_paddle.xcor() + 20 < ball.xcor():
        return False
    elif l_paddle.xcor() - 20 > ball.xcor():
        return False
    else:
        return True


game_on = True
while game_on:

    ball.center()
    ball.reset_speed()
    ball.bounce_x()
    while ball_inbounds():
        screen_delay()
        ball.move()

        if ball.ycor() >= 290 or ball.ycor() <= -280:
            ball.bounce_y()
        elif ((r_paddle.distance(ball) <= 30 and ball.run > 0)
                or (r_paddle.distance(ball) <= 50 and ball.xcor() >= r_paddle.xcor() - 30 and ball.run > 0)
                or (l_paddle.distance(ball) <= 30 and ball.run < 0)
                or (l_paddle.distance(ball) <= 50 and ball.xcor() <= l_paddle.xcor() + 30 and ball.run < 0)):
            ball.bounce_x()
            ball.speed_up()

        if ball_inbounds() is False:
            if ball.xcor() > 0:
                scoreboard.score_increase("left")
            else:
                scoreboard.score_increase("right")

    if scoreboard.check_winner():
        game_on = False

screen.exitonclick()




