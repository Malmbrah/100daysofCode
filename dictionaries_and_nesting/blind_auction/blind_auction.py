# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import blind_auction_art

"""
Clearing the Output
There are several ways of clearing the output. The easiest is to simply print "\n" many times so that the output scrolls down many lines.

e.g.

# This will add 20 new lines to the output
print("\n" * 20)

Functionality for the program:

i) Each person writes their name and bid.

ii) The program asks if there are others who need to bid. If so, then the computer clears the output (prints several blank lines) then loops back to asking name and bid.

iii) Each person's name and bid are saved to a dictionary.

iiii) Once all participants have placed their bid, the program works out who has the highest bid and prints it.

"""

blind_auction = {}
print(blind_auction_art.logo)

def print_dictinary():
    #Lager en tom variabel som skal fylles inn
    max_bid = 0
    max_bid_name = ""
    
    #Går gjennom hver key i blind_auction
    for name in blind_auction:
        #Setter max_bid til å være lik verdien til den høyeste VERIDEN
        if max_bid < blind_auction[name]:
            max_bid = blind_auction[name]
            #Hvis det er den høyeste verdien så blir navnet også lagret
            max_bid_name = name
    print(f"{max_bid_name} is the winner with ${max_bid}")
            

def bidding():
    name = input("Please write your name: ")
    bid = int(input("Please write your bid: $"))
    blind_auction[name] = bid


def main():
    #En vi kan endre til True når man bestemmer seg for å avslutte spillet
    stop_bidding = False
    #Må sette den her utenfor loopen, ellers begynner den hver gang etter det er noen som har blitt lagt til
    bidding()

    #Loopen fortsetter til stop_bidding blir True
    while not stop_bidding:
        any_others_making_a_bid = input("Is there any others making a bid? (yes/no): ").lower()

        if any_others_making_a_bid == "yes":
            #Ingen skal se hva som tidligere har blitt bydd
            print("\n" * 20)
            bidding()
            continue
        elif any_others_making_a_bid == "no":
            print("\n" * 20)
            print_dictinary()
            #Avslutter loopen
            stop_bidding = True
        else:
            print("Please write yes or no.")

main()