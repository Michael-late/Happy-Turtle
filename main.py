import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def up():
    pos = player.pos()
    player.goto(pos[0],pos[1]+20)

    
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#event listener
screen.onkey(up,"Up")
screen.listen()

#turtle
player = Player()

#cars
car = CarManager()

#display level
current_level = 0
level = Scoreboard(current_level)

game_is_on = True
while game_is_on:
    time.sleep(player.speeds)
    screen.update()
    car.generate_car()
    car.move()

    if player.ycor() > 280:
        player.reset()
        level.nextLevel()

    #collision
    for carx in car.cars:
        if player.distance(carx) < 20:
            level.over()
            game_is_on = False


screen.exitonclick()