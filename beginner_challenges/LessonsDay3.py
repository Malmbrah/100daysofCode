#If/elses

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride")
    age = int(input("What is your age: "))
    if age <= 12:
        bill = 5
        print("Child tickets costs $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets costs $7.")
    elif age >= 45 and age <= 55: #Kan skrive det 45 <= age <= 55
        print("Your ticket is free.")
    else:
        bill = 12
        print("Adult tickets costs $12.")
    
    wants_photo = input("Do you want a photo taken? y/n: ")
    if wants_photo == "y":
        #Add three dollars to the bill
        bill += 3

    print(f"Your final bill is {bill}")
else:
    print("Not tall enough")

"""

#check if odd or even using modulo
numberToCheck = int(input("What number do you want to check are odd or even: "))

if numberToCheck % 2 == 0:
    print('Even')
else:
    print('Odd')
"""