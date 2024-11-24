#Data types
String_example = "String"
integer_example = 5
float_example = 8.3
boolean_example = True
anotherFloat_example = 8_3

#Subscripting - Begge disse to under gir det samme. + eller - sier bare hvilken retning man starter fra. - er fra høyre
#print(String_example[-2] + String_example[4])

#For å se hva slags type en variabel er kan man bryke type()
"""
print(f"{type(float_example)}")
print(type(integer_example))
print(type(boolean_example))
print(type(String_example))
"""

#Number manipulation and F strings // (round(), floor())
bmi = 93 / 1.88 ** 2
print(round(bmi, 2)) # runde ned til 2 desimaler
print(bmi)

#Hvis man prøver å printe string + int så blir det feil
#print("Din score er: " + integer_example) #Denne vil ikke funke - Man får en TypeError

#Denne vil dog funke siden vi bruker en f-string. Man kan kombinere typer
print(f"Din score er: {integer_example} or more presicely {float_example}")
