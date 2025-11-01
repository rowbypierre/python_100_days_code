from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "normal")
COLOR = "white"
LOCATION = (0, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        """
        Initialize Scoreboard class with inherited properties from Turtle class.
        """
        self.hideturtle()
        self.penup()
        self.goto(*LOCATION)
        self.color(COLOR)
        self.score = -1
        self.score_refresh()

    def score_refresh(self):
        """
        Clear scoreboard and reprint with score increased by 1.
        """
        self.clear()
        self.score += 1
        prompt = f"Score: {self.score}"
        self.write(arg=prompt, align=ALIGN, font=FONT)

    def game_over(self):
        """
        Write "GAME OVER" at middle of screen.
        """
        self.goto(x=0, y=0)
        self.pendown()
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)
