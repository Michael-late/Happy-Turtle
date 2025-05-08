from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.shape("turtle")
        self.color("grey")
        self.setheading(90)
        self.setpos(STARTING_POSITION)

    def reset(self):
        self.setpos(STARTING_POSITION)
        

