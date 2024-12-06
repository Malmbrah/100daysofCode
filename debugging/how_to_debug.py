"""
Some bugs are sneaky, they only occur under certain conditions. In order to debug them, we need to be able 
to reliably reproduce the bug and diagnose our problem to figure out which conditions trigger the bug.

from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num])

"""
#Correct: 
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 5)
print(dice_images[dice_num])

"""

Playing computer is an important skill in debugging. You need to be able to go 
through your code line by line as if you were the 
computer to help you figure out what is going wrong.

year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

"""
#Hvis man skriver 1994 så skjer det ingenting fordi det er bare skrevet over eller under
year = int(input("What's your year of birth?"))

if year > 1980 and year <= 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
