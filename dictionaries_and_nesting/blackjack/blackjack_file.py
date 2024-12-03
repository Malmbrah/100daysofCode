"""
Our Blackjack Game House Rules:

The deck is unlimited in size.
There are no jokers.
The Jack/Queen/King all count as 10.
The Ace can count as 11 or 1.
Use the following list as the deck of cards:


The cards in the list have equal probability of being drawn.
Cards are not removed from the deck as they are drawn.
The computer is the dealer.
"""
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

"""
Mine tanker: bruke random.choice() på cards for å trekke et kort - ha det i en egen funksjon kalkt
"""

#user_cards = [random.choice(cards), random.choice(cards)]
#computer_cards = [random.choice(cards)]

def deal_new_card(list_of_cards):
    #new_card = random.choice(cards)
    new_card = 5
    list_of_cards.append(new_card)
    return list_of_cards

def check_if_sum_is_over_21(list_with_cards):
    if sum(list_with_cards) > 21:
        return True
    else:
        return False

def display_the_cards(user_cards, computer_cards):
    #Best å bruke den innebygde sum()-funksjonen for å legge sammen alle kortene, siden vi etterhvert legger til flere (hvis man ønsker å trekke flere)
    sum_of_user_cards = sum(user_cards)
    print(f"Your cards: {user_cards}, current score: {sum_of_user_cards} \n Computer's first card: {computer_cards[0]}")

def compare_scores():
    pass

def game():
    #Tenker at vi bare trekker to tilfeldige kort, mens PC bare trekker et. Når PC skal vise frem sine kort, DA kan den trekke et til
    user_cards = [4, 10]
    computer_cards = [10]
    display_the_cards(user_cards, computer_cards)

    hit_again = input("Type 'y' to get another card, type 'n' to pass: ")

    if hit_again == "y":
        #Legger til et nytt tilfeldig kort inn i brukeren sin kortstokk
        deal_new_card(user_cards)
        #Sjekke at summen om summen er over 21, og hvis den er det så avsluttes spillet
        if check_if_sum_is_over_21(user_cards):
            print("\n" * 3)
            print(f"Your final hand: {user_cards}, final score: {sum(user_cards)} \nComputer's final hand: {computer_cards}, final score: {sum(computer_cards)} \nYou went over. You lose.")
        else:
            display_the_cards(user_cards, computer_cards)
    elif hit_again == "n":
        deal_new_card(computer_cards)
        if check_if_sum_is_over_21(computer_cards):
            print(f"Your final hand: {user_cards}, final score: {sum(user_cards)} \nComputer's final hand: {computer_cards}, final score: {sum(computer_cards)} \nYou went over. You win.")
        elif not check_if_sum_is_over_21(computer_cards):
            deal_new_card(computer_cards)

"""
Burde jeg legge inn en while loop for både computer og bruker? at den er noe i banen med while check_if_over_21.. og så videre"""

game()

def main():
    do_you_want_to_play = input("Do you want to play a game of Blackjack? type 'y' or 'n': ")
    if do_you_want_to_play == "y":
        game()
    else:
        return