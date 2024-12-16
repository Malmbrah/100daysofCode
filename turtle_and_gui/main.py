from turtle import Turtle, Screen
from random import randint

#https://docs.python.org/3/library/turtle.html - documentation

#Make a square

"""
for _ in range(4):
    t.forward(100)
    t.right(90)
"""
#Draw a dotted line
"""
for _ in range(15):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()
"""

 
#Drawing different shapes, you can find the angle by dividing 360 / #sides. So square is 36+ / 4 = 90
#Each side is 100 steps 
#Each drawing should be a random color
#Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

t = Turtle()
screen = Screen()
screen.colormode(255)
t.shape("turtle")
#r = randint(0,255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    colors = (r, g, b)
    return colors

def shape_maker(number_of_sides, deg):
    t.color(random_color())
    for _ in range(number_of_sides):
        t.right(deg)
        t.forward(100)

triangle = shape_maker(3, 120)
square = shape_maker(4, 90)
pentagon = shape_maker(5, 72)
hexagon = shape_maker(6, 60)
heptagon = shape_maker(7, 51.5)
octagon = shape_maker(8, 45)
nonagon = shape_maker(9, 40)
decagon = shape_maker(10, 36)



screen.exitonclick()