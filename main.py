import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

NUMBER_OF_CAR_SPAWNING_DECI_SECONDS = 5

screen = Screen()
screen.setup(width=600, height=600)
screen._root.resizable(False, False)
screen.tracer(0)

player_obj = Player()
manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_obj.move, "Up")

game_is_on = True
count = 0
while game_is_on:
    count += 1
    time.sleep(0.1)
    screen.update()
    manager.move_cars()
    if count > NUMBER_OF_CAR_SPAWNING_DECI_SECONDS:
        manager.add_car()
        manager.remove_out_of_screen_cars()
        count = 0
    for car in manager.cars:
        if car.distance(player_obj) < 20:
            game_is_on = False
            time.sleep(1)
            screen.clear()
            scoreboard.display_game_over()
    if player_obj.ycor() > 260:
        player_obj.reset()
        scoreboard.increase_score()
        manager.increase_speed()

screen.exitonclick()
