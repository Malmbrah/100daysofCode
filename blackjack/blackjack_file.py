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



def print_win_for_user(user_cards, computer_cards):
    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)} \nComputer's final hand: {computer_cards}, final score: {sum(computer_cards)} \n You win.")

def print_loss_for_user(user_cards, computer_cards):
    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)} \nComputer's final hand: {computer_cards}, final score: {sum(computer_cards)} \n You lose.")

def deal_new_card(list_of_cards):
    new_card = random.choice(cards)
    list_of_cards.append(new_card)
    return list_of_cards

#Legg inn sjekk her om summen er over 21, gå gjennom listen som blir sendt inn med en for-loop
def check_if_sum_is_over_21(list_with_cards):
    if sum(list_with_cards) > 21:
        return True
    else:
        return False

def display_the_cards(user_cards, computer_cards):
    #Best å bruke den innebygde sum()-funksjonen for å legge sammen alle kortene, siden vi etterhvert legger til flere (hvis man ønsker å trekke flere)
    sum_of_user_cards = sum(user_cards)
    print(f"Your cards: {user_cards}, current score: {sum_of_user_cards} \n Computer's first card: {computer_cards[0]}")

def compare_scores(user_cards, computer_cards):
    if sum(user_cards) > sum(computer_cards):
        print_win_for_user(user_cards, computer_cards)
        return
    elif sum(computer_cards) > sum(user_cards):
        print("\n" * 20)
        print("The computer has better cards than you. ")
        print_loss_for_user(user_cards, computer_cards)
        return
    else:
        print("It's a push.")
        return 

def convert_ace_to_one(list_with_cards):
    for card in list_with_cards:
        if card == 11:
            list_with_cards.remove(card)
            list_with_cards.append(1)
    return list_with_cards

def game():
    #Tenker at vi bare trekker to tilfeldige kort, mens PC bare trekker et. Når PC skal vise frem sine kort, DA kan den trekke et til
    user_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards)]
    display_the_cards(user_cards, computer_cards)
    game_over = False

    #Så lenge ikke game_over = True så fortsetter loopen
    while not game_over:
        hit_again = input("Type 'y' to get another card, type 'n' to pass: ")

        if hit_again == "y":
            #Legger til et nytt tilfeldig kort inn i brukeren sin kortstokk
            deal_new_card(user_cards)
            #Sjekke at summen om summen er over 21, og hvis den er det så avsluttes spillet
            if check_if_sum_is_over_21(user_cards):
                user_cards = convert_ace_to_one(user_cards)
                if sum(user_cards) > 21:
                    print("\n" * 3)
                    print_loss_for_user(user_cards, computer_cards)
                    game_over = True
                    break
            else:
                #Ellers så viser vi frem hvilke kort bruker har, og så fortsetter loopen
                display_the_cards(user_cards, computer_cards)
                continue
        elif hit_again == "n":
            while sum(computer_cards) < 17:
                #Da får computer trekkke et nytt kort     
                deal_new_card(computer_cards)
                #Hvis summen er over 21 så sjekker den om computer cards inneholder en 11
                if check_if_sum_is_over_21(computer_cards):
                    computer_cards = convert_ace_to_one(computer_cards)
                    if sum(computer_cards) > 21:
                        print("\n" * 3)
                        print_win_for_user(user_cards, computer_cards)
                        game_over = True
                        break
            #Hvis summen til computer er mellom 17 og 21 så må den stoppe, og vi sammenligner scores
            if 17 <= sum(computer_cards) <= 21:
                compare_scores(user_cards, computer_cards)
                game_over = True


def main():
    do_you_want_to_play = input("Do you want to play a game of Blackjack? type 'y' or 'n': ")
    if do_you_want_to_play == "y":
        game()
    else:
        return
    
main()