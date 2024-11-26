list_with_numbers_example = [1,2,3,4]

#For loop
for number in list_with_numbers_example:
    #print(number)
    pass

# Oppgave: Vi skal finne max score ved hjelp av for-loop
student_scores = [555,544,539, 220, 999, 1000, 386, 119, 769, 800, 959, 100]

#Printer ut for å dobbeltsjekke at det blir riktig
print("Max-funksjonen: ", max(student_scores))

#Lager en max_score variabel og setter den til å være lik 0
max_score = 0

#går gjennom hvert item i listen
for score in student_scores:
    #Hvis max_score er mindre enn neste item i listen (score) så blir max_score verdien til den nye score
    if max_score < score:
        max_score = score
#print(max_score)

sum = 0
#The gauss challenge - legg sammen tallene fra 1 til 100
for number in range(1, 101):
    sum += number
print(sum)