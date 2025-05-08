from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.shape("square")
        self.shapesize(1,4)
        self.penup()
        self.currentColour = -1

    def move(self):
        if self.currentColour == len(COLORS) -1:
            self.currentColour = -1
        self.currentColour += 1
        self.y = random.randint(-380,380)
        print(self.y)
        self.setpos(280,self.y)
        self.color(COLORS[self.currentColour])   
        
