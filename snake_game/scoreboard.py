from turtle import Turtle

#Når man har variabler som  skal brukes gjennom hele programmet er det mye bedre å ha konstante variabler som vi
#bare kan endre på her oppe. Man slipper å grave gjennom hele programmet for å endre
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

#Create a new scoreboard class. Is going to inherit from Turtle. Scoreboard will keep track of score and display it.
#Use the write()-method from Turtle. And use turtle.clear() to reset scoreboard

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(x = 0, y = 275)
        self.score = 0
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)


    def increase_count(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()