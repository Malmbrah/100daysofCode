#Randomisation
import random
import my_module

#random_integer = random.randint(1,5) #Gir et tall mellom 1 og 5

#Creating random floating point number - bruke random.random(): Returns a random floating point 0.0 <= x < 1
random_number_0_to_1 = random.random()

#Uniform() - kan inkludere 10
random_float = random.uniform(1, 10)

heads_or_tails = random.randint(1,2)

if heads_or_tails == 1:
    pass
    #print("Heads")
else:
    pass
    #print("Tails")

#Who pays the bill - Få frem et tilfeldig navn
friends = ["Alice", "Magz", "Jonte", "Opsahl", "Tøggie"]

#Krusleder skrev denne - lurere å bruke denne fordi det er ikke sikkert man vet hvor lang listen er
print(random.choice(friends))
#Jeg skrev denne
print(friends[random.randint(0,4)])
