from turtle import Turtle

WINNING_PROMPT = "CONGRATULATIONS {} PLAYER"


class Scoreboard(Turtle):

    def __init__(self, xcor, ycor, win_score):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.teleport(x=xcor, y=ycor)
        self.color("white")
        self.align = "Center"
        self.font = ("Arial", 30, "normal")
        self.score_left = 0
        self.score_right = 0
        self.update()
        self.winning_score = win_score

    def update(self):
        """
        Summary:    Clears scoreboard and reprints with updated scores.
        """
        self.clear()
        self.write(arg=f"{self.score_left}\t|\t{self.score_right}", font=self.font, align=self.align)

    def score_increase(self, side):
        """
        Summary:    Increases score of parameter 'side' by 1.

        Parameter:  'side': String -- 'right' / 'r' or 'left' / 'l'.
        """
        if side == "right" or side == "r":
            self.score_right += 1
        elif side == "left" or side == "f":
            self.score_left += 1
        self.update()

    def check_winner(self):
        """
        Summary:    Determines winner using 'winscore' parameter passed when initializing Scoreboard() class.
                    Winning side is printed at center of screen.

        Return:     'True' if winner exist.
                    'False' if no winner exist.
        """
        if self.score_right == self.winning_score or self.score_left == self.winning_score:
            self.home()
            if self.score_right > self.score_left:
                self.write(arg=WINNING_PROMPT.format("RIGHT"), font=self.font, align=self.align)
            else:
                self.write(arg=WINNING_PROMPT.format("LEFT"), font=self.font, align=self.align)
            return True
        else:
            return False

