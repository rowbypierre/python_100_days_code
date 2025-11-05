import time
from player import Player
from car_manager import CarManager
from screen import GameScreen

player = Player()
game_screen = GameScreen(player)
car_manager = CarManager(20)


game_is_on = True
while game_is_on:
    car_manager.drive_cars()
    car_manager.return_cars()
    if player.has_crossed():
        game_screen.add_level()
        player.home()
        car_manager.speed_up_cars()
    if car_manager.is_road_kill(player):
        break
    time.sleep(0.1)
    game_screen.screen_refresh()

game_screen.clicktoexit()
