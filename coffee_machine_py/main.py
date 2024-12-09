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
            else:
                return True, ""

#HVORDAN KAN JEG ENDRE VERDIEN I MENU.py??!
def do_you_have_enough_money(user_order):
    print(f"RESOURCES[money]: {menu.resources["money"]}")
    #Sjekker hva man har i resources vs hva drikken koster
    if menu.resources["money"] < user_order["cost"]:
        #Hvis man ikke har nok penger må man legge til mer
        print(f"You need to add more money.")
        added_money = int(input("How much money do you want to add?: $"))
        #Disse blir lagt inn i banken din
        menu.resources["money"] += added_money
        print(f"${added_money} was added to your bank. Your new total is ${menu.resources["money"]}")


def main():
    TURN_OFF = False

    while not TURN_OFF:
        user_order = input("What would you like? (espresso/latte/cappuccino): ")
        if user_order == "report":
            report()

        if user_order == "off":
            TURN_OFF = True
        
        #espresso-section
        if user_order == "e":
            #Setter espresso_dictionary til å være verdiene til de ulike ingrediensene i espresso
            espresso_dictionary = menu.MENU["espresso"]["ingredients"]
            espresso_cost = menu.MENU["espresso"]
            do_you_have_enough_money(espresso_cost)
            #Setter status = False/True basert på om vi har nok resources, og not_enough_of_resource til å være den man ikke har nok av
            status, not_enough_of_resource = check_resources_ingredients(espresso_dictionary)
            #Så hvis status er False
            if not status:
                print(f"Sorry, not enough of {not_enough_of_resource}")
            else:
                print("Du har nok resources")



main()