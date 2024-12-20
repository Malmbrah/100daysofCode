from turtle import Turtle, Screen
import random
#Build a Turtle race

screen = Screen()
screen.setup(width = 500, height = 400)
#TODO Lage en pop up som spør bruker om hva slags farge den velger
#TODO Lage flere turtles, de beveger seg med tilfeldig hastighet mot høyre side
#når én av de har krysset høyre siden så er racet over
#Printer ut om bruker vant eller ei, og hvilken farge det var som vant
user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower() 

colors = ["red", "orange", "yellow", "green", "blue"]

def speed_randomizer(turtle):
    return turtle.forward(random.randint(1,10))

is_race_on = False
turtles = []
#Lager turtles
for t in range(0,5):
    r = Turtle(shape = "turtle")
    turtles.append(r)
    

x = -230
y = -100

#Må løfte opp slik at de ikke lager en strek når de går til start posisjon
for turtle in turtles:
    turtle.penup()
    turtle.goto(x,y)
    y += 50
    #Setter fargen på ulike turtles ved å bruke indexen(int) til å fange opp de ulike indexene i colors listen
    turtle.color(colors[turtles.index(turtle)])

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        #230 fordi x-koordinaten på slutten av skjermen er 230, og når en turtle krysser den så er spillet ferdig
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} is the winner!")   
            else:
                print(f"You've lost. The {winning_color} is the winner!")

        speed_randomizer(turtle)


screen.exitonclick()