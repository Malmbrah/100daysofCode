import game_data
import art
import random

LIST_OF_ALL_THE_PERSONS = game_data.data

#Denne funksjonen skal generere en person fra game_data, og returnere personen og dens info
def generate_person():
    #Denne går inn i game_data, så inn i data. Deretter tar jeg en tilfeldig index fra 0 til lengden av listen
    #Person blir da altså én av de mange dictionaries i LIST_OF_ALL_THE_PERSONS
    person = LIST_OF_ALL_THE_PERSONS[random.randint(0, len(LIST_OF_ALL_THE_PERSONS) - 1)]
    return person

"""
def compare_followers_user_guessed_A(person_A, person_B):
    if person_A['followers'] > person_B['followers']:
        return True
    else:
        return False

def compare_followers_user_guessed_B(person_A, person_B):
    if person_A['followers'] < person_B['followers']:
        return True
    else:
        return False
"""
def check_if_user_guess_correct(guess, person_A, person_B):
    pass


def game():
    
    person_A = generate_person()
    person_B = generate_person()
    game_over = False
    score = 0

    while not game_over:
        print(art.logo)
        #Skriver ut logo og personene
        print(f"Compare A: {person_A['name']}, {person_A['description']}, {person_A['country']}")
        print(art.vs)
        print(f"Against B: {person_B['name']}, {person_B['description']}, {person_B['country']}")
        
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        #Så hvis bruker gjetter a og a har flere followers enn b
        if user_guess == "a" and person_A['follower_count'] > person_B['follower_count']:
            #score øker
            score += 1
            print(f"Your right. Current score is {score}")
            #person B blir til person A, og person B blir til en ny person
            person_A = person_B
            person_B = generate_person()

        elif user_guess == "a" and person_A['follower_count'] < person_B['follower_count']:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True

        elif user_guess == "b" and person_A['follower_count'] < person_B['follower_count']:
            score += 1
            print(f"Your right. Current score: {score}")
            person_A = person_B
            person_B = generate_person()

        elif user_guess == "b" and person_A['follower_count'] > person_B['follower_count']:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True

game()