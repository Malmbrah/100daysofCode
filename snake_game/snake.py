from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.creating_snake()
        #Det første segmentet i blokken
        self.head = self.segments[0]

    def moveSnake(self):
        """Denne oppdaterer posisjonen til de ulike segmentene"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            #Vi må starte på de bakerste og jobbe oss fremover. Det er derfor vi starter på seg_num - 1
            #For å få slangen til å bevege seg som en samlet unit burde man gjøre slik at den 3. turtle går fra siste posisjon
            #til posisjon nr 2, og den fra posisjon nr 2 går til posisjon nr 1, og nr 1 går et steg frem
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    def add_segment(self):
            r = Turtle(shape = "square")
            r.color("white")
            self.segments.append(r)

    def extend(self):
        pass

    def creating_snake(self):
        """Creating 3 turtles, making them white, setting them as a square and position them next to eachother"""
        for _ in range(0,3):
            self.add_segment()

        x = 0
        y = 0
        for turtle in self.segments:
            turtle.penup()
            turtle.goto(x, y)
            x -= 20

    def up(self):
        """Får slangen til å bevege seg oppover"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        """Får slangen til å bevege seg nedover"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    
    def left(self):
        """Får slangen til å bevege seg mot venstre"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)       


    def right(self):
        """Får slangen til å bevege seg mot høyre"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
