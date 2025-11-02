import turtle


def make_table(r_paddle, l_paddle):
    """
    Make black 800x600 game screen with 'Ping Pong' title.

    Parameters:
        - r_paddle (Turtle() obj): Right paddle.
        - l_paddle (Turtle() obj): Left paddle.

    Return:
        table (_Screen()): Screen with dimensions in summary and paddles.
    """
    table = turtle.Screen()
    table.bgcolor("black")
    table.title("Ping Pong")
    table.setup(width=800, height=600)
    table.listen()

    key_actions = [
        (r_paddle.paddle_up, "Up"),
        (r_paddle.paddle_down, "Down"),
        (l_paddle.paddle_up, "w"),
        (l_paddle.paddle_down, "s"),
    ]
    for combo in key_actions:
        table.onkeypress(*combo)

    return table


def ball_in_black(r_paddle, l_paddle, ball):
    """
    Confirm (bool) that ball (Turtle()) is in game screen.
    """

    false_conditions = [
        r_paddle.xcor() + 20 < ball.xcor(),
        l_paddle.xcor() - 20 > ball.xcor(),
    ]
    if any(false_conditions):
        return False
    else:
        return True
