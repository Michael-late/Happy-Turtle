FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,current_lv, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.level = current_lv
        self.penup()
        self.color("black")
        self.goto(-280,260)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", font=(FONT))

    def nextLevel(self):
        self.level += 1
        self.update()    

