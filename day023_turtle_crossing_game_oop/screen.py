from turtle import Turtle, Screen

FONT = ("Courier", 24, "normal")
LEVEL_LOCATION = (-280, 250)
STOP_LOCATION = (-150, 0)


class GameScreen(Turtle):
    def __init__(self, player):
        super().__init__()
        self.screen = self.make_screen(player)
        super().hideturtle()
        super().penup()
        super().goto(*LEVEL_LOCATION)
        self.level = -1
        self.add_level()

    def add_level(self):
        "Incease game level graphic."
        self.level += 1
        super().clear()
        super().write(f"Level: {self.level}", font=FONT)

    def make_screen(self, player):
        screen = Screen()
        screen.title("TURTLE CROSSING")
        screen.setup(width=600, height=600)
        screen.tracer(0)
        screen.listen()

        player_keys = {"Up": player.move_up}
        for key, method in player_keys.items():
            screen.onkeypress(fun=method, key=key)

        return screen
    
    def clicktoexit(self):
        "Close game window on mouse click."
        self.screen.exitonclick()

    def screen_refresh(self):
        "Refresh game window."
        self.screen.update()

    def game_over(self):
        "Write game over at center of screen."
        super().goto(STOP_LOCATION)
        super().write('!!!GAME OVER!!!', font=FONT)
        


