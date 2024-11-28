import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

generated_password = []
password = ""

#ENKLE VERSJONEN
if nr_letters != 0 and nr_symbols != 0 and nr_numbers != 0:
    #Man går gjennom letters antallet hvor mange ganger nr_letters er, og så må vi legge til en til for å få med alle
    for letter in range(1, nr_letters + 1):
        #random.choice velger en tilfeldig item fra listen med letters og legger den til listen generated_password
        #Det gjør den antall nr_letters ganger
        generated_password.append(random.choice(letters))

    for symbol in range(1, nr_symbols + 1):
        generated_password.append(random.choice(symbols))

    for number in range(1, nr_numbers + 1):
        generated_password.append(random.choice(numbers))

    #Går gjennom hver greie i generated_password listen og legger det til i password 
    for item in generated_password:
        password += item

    print(password)

    #HARD VERSION
    harder_password = ""
    #Går basically gjennom de allerede plukkede tall/bokstav/symbol og så plukker choice tilfeldig fra de
    for new_item in range(1, len(generated_password) + 1):
        harder_password += random.choice(generated_password)

    print("Harder password: " + harder_password)
else:
    print("It can't be zero.")