def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#Man kan lage variabler ut av funksjoner, eller man kan bruke deres funksjonalitet
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

ended = False

def continue_with_answer(previous_answer):
    what_operation = input(" + \n - \n * \n /\n What mathematical operation do you want to perform?: ")

    #Sjekker keysene i operations
    for op in operations:
        #Hvis den finner en key som ligner på den bruker skrev inn så går den inn i if
        if what_operation == op:
            second_number = int(input("Please write the second number: "))
            #Her setter jeg dictionary[key](verdi, verdi_2). Dictionary[key] for å komme inn i valuen til key
            #Og så bruker sender man det inn til riktig funksjon
            #Man kan lage variabler slik. my_variable = add 
            #Så kan man skrive my_variable(n1, n2) for å sende inn i funksjonen add!!
            answer = operations[op](previous_answer, second_number)
    print(f"Answer: {answer}")
    contine_to_use_answer_or_not = input(f"Do you want to continue working with {answer}, or do you want to start a new calculation? (y/n): ").lower()
    if contine_to_use_answer_or_not == "y":
        continue_with_answer(answer)
    elif contine_to_use_answer_or_not == "n":
        new_calculation()

def new_calculation():
    first_number = int(input("Please write the first number: "))
    what_operation = input(" + \n - \n * \n /\n What mathematical operation do you want to perform?: ")

    #Sjekker keysene i operations
    for op in operations:
        #Hvis den finner en key som ligner på den bruker skrev inn så går den inn i if
        if what_operation == op:
            second_number = int(input("Please write the second number: "))
            #Her setter jeg dictionary[key](verdi, verdi_2). Dictionary[key] for å komme inn i valuen til key
            #Og så bruker sender man det inn til riktig funksjon
            #Man kan lage variabler slik. my_variable = add 
            #Så kan man skrive my_variable(n1, n2) for å sende inn i funksjonen add!!
            answer = operations[op](first_number, second_number)
    print(f"Answer: {answer}")
    contine_to_use_answer_or_not = input(f"Do you want to continue working with {answer}, or do you want to start a new calculation? (y/n): ").lower()
    if contine_to_use_answer_or_not == "y":
        continue_with_answer(answer)
    elif contine_to_use_answer_or_not == "n":
        new_calculation()

new_calculation()