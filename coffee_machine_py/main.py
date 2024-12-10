import menu 


def report():
    print(f"Water: {menu.resources["water"]}ml\nMilk: {menu.resources["milk"]}ml\nCoffee: {menu.resources["coffee"]}g\nMoney: ${menu.resources["money"]}")

RESOURCES = menu.resources

#Sjekker om vi har nok resources til å ta imot bestillingen
def check_resources_ingredients(user_order):
    #Den går inn i user_order som er en dictionary og ingredients er water, milk..
    for ingredients in user_order:
        for resource in RESOURCES:
            #Sjekker opp våre resources mot user_order. Hvis vi har mindre så returnerer false
            # Mener jeg må ha det slik for å unngå hvis user_order ikke har ingredienser, så får man feilmelding
            #hvis man har if user_order[ingredients] > RESOURCES[resource]
            if RESOURCES[resource] < user_order[ingredients]:
                #returnerer en tuple for få med status OG hvilken ingrediens som ikke det er nok av
                return False, resource
    return True, ""


def do_you_have_enough_money(drink_cost):

    total_money_inserted = menu.resources["money"]
    #Sjekker hva man har i resources vs hva drikken koster og passer på at den bruker legger inn nok penger
    while total_money_inserted < drink_cost:
        print(f"The drink is ${drink_cost}. You need to add more money. Current balance: ${total_money_inserted}")
        #Hvis man ikke har nok penger må man legge til mer
        added_money = float(input("How much money do you want to add?: $"))
        #Disse blir lagt inn i banken din
        total_money_inserted += added_money
        print(f"${added_money} was inserted.")

    change = total_money_inserted - drink_cost
    if change > 0:
        print(f"Here is ${round(change,2)} in change.")
            

def make_coffee(user_order):
    #Sjekker verdien til hver ingrediens som matcher og trekker den fra det vi har
    for ingredients in user_order:
        for resource in RESOURCES:
            if ingredients == resource:
                RESOURCES[resource] -= user_order[ingredients]
                
def espresso():
    #Setter espresso_dictionary til å være verdiene til de ulike ingrediensene i espresso
    espresso_dictionary = menu.MENU["espresso"]["ingredients"]
    espresso_cost = menu.MENU["espresso"]["cost"]
    do_you_have_enough_money(espresso_cost)
    #Setter status = False/True basert på om vi har nok resources, og not_enough_of_resource til å være den man ikke har nok av
    status, not_enough_of_resource = check_resources_ingredients(espresso_dictionary)
    print(f"status: {status}")
    #Så hvis status er False
    if not status:
        print(f"Sorry, not enough of {not_enough_of_resource}")
    else:
        make_coffee(espresso_dictionary)
        

def latte():
    #Setter espresso_dictionary til å være verdiene til de ulike ingrediensene i espresso
    latte_dictionary = menu.MENU["latte"]["ingredients"]
    latte_cost = menu.MENU["latte"]["cost"]
    do_you_have_enough_money(latte_cost)
    #Setter status = False/True basert på om vi har nok resources, og not_enough_of_resource til å være den man ikke har nok av
    status, not_enough_of_resource = check_resources_ingredients(latte_dictionary)
    #Så hvis status er False så går den inn i make coffe
    if not status:
        print(f"Sorry, not enough {not_enough_of_resource}")
    else:
        make_coffee(latte_dictionary)  

def cappuccino():
    pass

def main():
    TURN_OFF = False

    while not TURN_OFF:
        user_order = input("What would you like? (espresso/latte/cappuccino): ")
        if user_order == "report":
            report()

        elif user_order == "off":
            TURN_OFF = True
        
        #espresso-section
        elif user_order == "espresso":
            espresso()
            #print(f"Here is your {user_order}")

        elif user_order == "latte":
            latte()
            #print(f"Here is your {user_order}")

        elif user_order == "cappuccino":
            cappuccino()
            #print(f"Here is your {user_order}")





main()