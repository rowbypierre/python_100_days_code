from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "normal")
COLOR = "white"
LOCATION = (0, 260)
DATAFILE = "./data.txt"


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
        self.file_score = self.high_score()
        self.score_refresh()

    def score_refresh(self):
        """
        Clear scoreboard and reprint with score increased by 1.
        """
        self.clear()
        self.score += 1
        prompt = f"Score: {self.score}  High Score: {self.high_score()}"
        self.write(arg=prompt, align=ALIGN, font=FONT)

    def game_over(self):
        """
        Write "GAME OVER" at middle of screen and save score.
        """
        self.goto(x=0, y=0)
        self.pendown()
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)
        self.save_score()

    def high_score(self):
        "Return the greater of two scores (int: local highscore vs current score)."
        with open(DATAFILE, "r") as data:
            saved_score = int(data.read().strip())

        return max([saved_score, self.score])

    def save_score(self):
        "Save gameplay score to local data.txt if greater than score within file."
        with open(DATAFILE, "r+") as data:
            data.write(str(self.high_score()))
