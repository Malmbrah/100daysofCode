from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forwards():
    t.forward(20)

def move_left():
    t.left(10)

def move_backwards():
    t.back(20)

def move_right():
    t.right(10)

def clear_screen():
    t.reset()

#So that the screen listens after keypresses etc.
screen.listen()
#key = den knappen man trykker for å få ting til å skje.
#Legg merke til at det ikke står move_forwards(). Det er fordi parenteser gjør at den funksjonen kicker i gang der og da
#men vi vil at den kicker igang når mellomrom blir trykket på
screen.onkey(key="w", fun = move_forwards)
screen.onkey(key="a", fun = move_left)
screen.onkey(key="d", fun = move_right)
screen.onkey(key="s", fun = move_backwards)
screen.onkey(key="c", fun = clear_screen)



screen.exitonclick()