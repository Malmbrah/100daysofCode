#Extracting colors from a painting
#import colorgram
#Want to create a list with all the colors from the painting and each item a tuple
import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)


#colors = []
#The colors is returned as objects
#colors_from_painting = colorgram.extract('hirst_painting\image.jpg', 30)
#I go through each object in color
#for object in colors_from_painting:
    #Here we get the rgb from the object
 #   color = object.rgb
    #We need to specify which color is which. Since it is a object we need to specify the r, g, b
  #  r = color.r
   # g = color.g
    #b = color.b
   # colors.append((r, g, b))

color_list = [(237, 230, 217), (63, 28, 7), (87, 96, 113), (166, 83, 30), (243, 215, 235), (220, 159, 82), (208, 223, 230), (139, 155, 181), (213, 161, 9), (87, 108, 96), (209, 5, 23), (17, 19, 53), (239, 217, 72), (225, 234, 230), (142, 161, 151), (23, 38, 27), (245, 62, 41), (78, 106, 204), (32, 44, 135), (229, 47, 77), (184, 15, 5), (213, 217, 7), (210, 138, 170), (234, 167, 207), (56, 32, 37), (165, 50, 67), (102, 78, 10), (112, 137, 121), (45, 75, 58), (178, 199, 194)]

#TASK making a 10 dots x 10 dots. Each dot size: 20. Space between is 50.
t.pensize(10)
t.speed(50)

#Lager på doten fra fargelisten vi hentet ut
def dot_color():
    color = random.choice(color_list)
    return color

#Lager en rad
def making_a_row():
    for _ in range(10):
        making_dot()
        t.penup()
        t.forward(50)
        t.pendown()

#Dette er startpunktet som oppdaterer seg for hver gang man har laget en row
def starting_point(y):
    t.teleport(-200,y)

#Lager selve doten
def making_dot():
    t.pencolor(dot_color())
    t.dot()

#Starter på -200 for å få med hele greia i bildet
y_increase = -200

#Vet at vi skal lage 10 x 10 med 50 paces i mellom. Litt hardkodet men det funker
while y_increase <= 300:
    starting_point(y_increase)
    making_a_row()
    y_increase += 50

screen.exitonclick()