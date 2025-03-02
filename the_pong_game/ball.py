from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("normal")
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)

    #def when_hit(self):
      #  current_heading = self.heading()
       # self.heading = - current_heading

    