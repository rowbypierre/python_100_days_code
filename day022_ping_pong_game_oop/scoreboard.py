from turtle import Turtle, Screen
import time

WINNING_PROMPT = "!CONGRATULATIONS {} PLAYER!"


# class GameScreen(Turtle.Screen):
#     def __init__(self, r_paddle, l_paddle):
#         super().__init__()
        
#         self.r_paddle = r_paddle
#         self.l_paddle = l_paddle

    
#     def assign_keys(self):
#         self.listen()

#         key_actions = [
#             (self.r_paddle.paddle_up, "Up"),
#             (self.r_paddle.paddle_down, "Down"),
#             (self.l_paddle.paddle_up, "w"),
#             (self.l_paddle.paddle_down, "s")
#         ]
#         for combo in key_actions:
#             self.onkeypress(*combo)

#         # super().exitonclick()
        


class Scoreboard(Turtle):
    def __init__(self, graph_x, graph_y, win_score):
        super().__init__()
        super().hideturtle()
        super().penup()
        super().teleport(graph_x, graph_y)
        super().color("white")
        self.align = "Center"
        self.font = ("Arial", 30, "normal")
        self.score_left = 0
        self.score_right = 0
        self.refresh()
        self.winning_score = win_score
        self.game_screen = None

    def make_game_screen(self, r_paddle, l_paddle):
        self.game_screen = Screen()
        self.game_screen.bgcolor("black")
        self.game_screen.title("Ping Pong")
        self.game_screen.setup(width=800, height=600)

        self.game_screen.listen()

        key_actions = [
            (r_paddle.paddle_up, "Up"),
            (r_paddle.paddle_down, "Down"),
            (l_paddle.paddle_up, "w"),
            (l_paddle.paddle_down, "s")
        ]
        for combo in key_actions:
            self.game_screen.onkeypress(*combo)

        self.game_screen.exitonclick()

    def refresh(self):
        """
        Summary: Clears scoreboard and reprints with updated scores.
        """
        super().clear()
        super().write(
            arg=f"{self.score_left}\t|\t{self.score_right}",
            font=self.font,
            align=self.align,
        )

    def add_score(self, paddle_location):
        """
        Summary: Increase player score by one.

        Parameter:
            paddle_location (str): 'right' / 'r' or 'left' / 'l' player.

        Return
            None: Updated gameplay scoreboard.
        """
        if paddle_location.strip().lower() in ["right", "r"]:
            self.score_right += 1
        else:
            self.score_left += 1

        self.refresh()

    def check_winner(self):
        """
        Summary: Confirm (bool) if a player has the winning and determings the winner.

        Return:
            - True if winner exist.
            - False if no winner exist.
            None: Print congradulatory message on screen.
        """
        all_scores = [self.score_left, self.score_right]
        all_scores.sort(reverse=True)

        winner_exists = self.winning_score in all_scores
        if winner_exists:
            super().penup()
            super().goto(0, 0)
            super().write(
                WINNING_PROMPT.format(
                    "RIGHT" if self.score_right > self.score_left else "LEFT"
                ),
                font=self.font,
                align=self.align,
            )

            return True
        else:
            return False
