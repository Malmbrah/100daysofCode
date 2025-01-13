from turtle import Turtle
import random

#Vi vil at denne klassen skal inherit fra Turtle-klassen slik at den har alt fra Turtle + litt mer
class Food(Turtle):

    def __init__(self):

        #Dette er Turtles __init__
        super().__init__()
        self.shape("circle")
        self.penup()
        #Vi ønsker å lage sirkelen mindre enn standard 20x20. Da kan vi bruke shapesize og si at ting er halvparten av vanlig
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        #Vi trenger ikke se at sirkelen blir laget, og SÅ går til posisjonen vi vil. Det løser vi med "fastest"
        self.speed("fastest")
        self.refresh()

    
    def refresh(self):
        """Dette skal plassere maten. Skjermen går fra -300 til 300, men vi vil ikke at man skal være helt i kanten"""
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)