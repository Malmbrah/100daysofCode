MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

PROFIT = 0
RESOURCES = {
    "water": 200,
    "milk": 200,
    "coffee": 100,
}

def generate_report():
    print(f"Water: {RESOURCES['water']}ml\nMilk: {RESOURCES['milk']}ml\nCoffee: {RESOURCES['coffee']}g\nMoney: ${PROFIT}")


def insert_coins():
    """Returns the total calculated from coins inserted."""
    coins = float(input("Please insert coins: $"))
    return coins

def is_transaction_sufficient(money_recieved, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is your ${change}")
        global PROFIT
        PROFIT += money_recieved
        return True
    else:
        print("That is not enough money. Money refunded.")
        return False 

def make_coffe(name_of_drink, drink):
    for item in drink["ingredients"]:
        RESOURCES[item] -= drink["ingredients"][item]
    print(f"Here is your {name_of_drink}")


def is_resources_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if RESOURCES[item] < order_ingredients[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True

def coffee_machine():
    is_on = True

    while is_on:
        choice = input("What choice of coffee would you like? (espresso/latte/cappucino): ").lower()

        if choice == "off":
            is_on = False
        
        elif choice == "report":
            generate_report()

        else:
            drink = MENU[choice]
            if is_resources_sufficient(drink["ingredients"]):
                payment = insert_coins()
                if is_transaction_sufficient(payment, drink["cost"]):
                    make_coffe(choice, drink)


coffee_machine()