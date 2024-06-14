from turtle import Screen
import time
from player import Player
from computer_manager import CarManger
from scoreboard import ScoreBoard

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)
player= Player()
carmanger = CarManger()
scoreboard =ScoreBoard()

screen.listen()
screen.onkey(player.move_forward, "Up")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
  
    carmanger.create_cars()
    carmanger.move_cars()
    
    #detect the collision with cars
    for cars in carmanger.all_cars:
        if cars.distance(player) < 20:
            is_game_on= False
            scoreboard.game_over_print()

    #Detect the succesing the cross line 
    if player.is_game_finishing():
        player.is_game_start()
        scoreboard.level_increment()
        carmanger.game_level_up()
        

                   

screen.exitonclick()