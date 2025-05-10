from turtle import Turtle
from random import randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.COLORS = COLORS
        self.cars = []

    def generate_car(self):
        if randint(1, 6) == 6:
            new_car = Turtle()
            new_car.penup()
            new_car.color(self.COLORS[randint(0, len(COLORS)-1)])
            new_car.shape("square")
            new_car.shapesize(1, 2)
            y = randint(-250, 250)
            new_car.setpos(300, y)
            self.cars.append(new_car)


    def move(self):
        for x in self.cars:
            x.backward(STARTING_MOVE_DISTANCE)
    
        
