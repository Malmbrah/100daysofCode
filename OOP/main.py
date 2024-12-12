import turtle

#man kan finne alt om hva man kan gjøre i dokumentasjonen: https://docs.python.org/3/library/turtle.html

#Man får tak i attributes ved å skrive: objekt.attributes
#print(my_screen.canvheight)

#Man får tak i methods ved å skrive: objekt.method()

#a new turtle object
timmy = turtle.Turtle()

#Endrer hvordan timmy ser ut
timmy.shape("turtle")

#Endrer fargen på turtle. Fant fargen her: https://cs111.wellesley.edu/reference/colors
timmy.color("chartreuse2")


#Turtle bevegelser
timmy.forward(100)




my_screen = turtle.Screen()


my_screen.exitonclick()

