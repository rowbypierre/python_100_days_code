from turtle import Turtle

score_start = -1
ALIGN = "center"
FONT = ('Courier', 20, 'normal')
COLOR = "white"
LOCATION = {
    "x": 0,
    "y": 260
}


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        """
        Initialize Scoreboard class with inherited properties from Turtle class.
        """
        self.hideturtle()
        self.penup()
        self.goto(x=LOCATION["x"], y=LOCATION["y"])
        self.color(COLOR)
        self.score_refresh()

    def score_refresh(self):
        """
        Clear scoreboard and reprint with score increased by 1.
        """
        self.clear()
        global score_start
        score_start += 1
        prompt = f"Score: {score_start}"
        self.write(arg=prompt, align=ALIGN, font=FONT)

    def game_over(self):
        """
        Print "GAME OVER" at middle of screen.
        """
        self.goto(x=0, y=0)
        self.pendown()
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)

