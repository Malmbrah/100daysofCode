import random

CORRECT_NUMBER = random.randint(1,100)
#Store bokstaver pga global variabel


def check_if_no_more_attempts(attempts):
    if attempts == 0:
        return True
    else:
        return False

def check_if_correct_answer(user_guess):
    if user_guess > CORRECT_NUMBER:
        print("Too high. Guess again.")
    elif user_guess < CORRECT_NUMBER:
        print("Too low. Guess again. ")
    else:
        print("\n" * 20)
        print("You guessed the correct number!! You win!")

def easy_game():
    attempts = 10

    #Så lenge attempts ikke er null så fortsetter løkken
    while attempts > 0:
        print(f"You have {attempts} attempts to guess the number.")
        user_guess = int(input("Make a guess: "))

        if user_guess > CORRECT_NUMBER:
            attempts -= 1
            if check_if_no_more_attempts(attempts):
                print("You ran out of attempts. You lost.")
                break
            print("Too high. Guess again")
        elif user_guess < CORRECT_NUMBER:
            attempts -= 1
            if check_if_no_more_attempts(attempts):
                print("You ran out of attempts. You lost.")
                break
            print("Too low. Guess again.")
        else:
            print("\n" * 20)
            print("You guessed the correct number!! You win!")
            break

def hard_game():
    attempts = 5
    #Så lenge attempts ikke er null så fortsetter løkken
    while attempts > 0:
        print(f"You have {attempts} attempts to guess the number.")
        user_guess = int(input("Make a guess: "))

        if user_guess > CORRECT_NUMBER:
            attempts -= 1
            if check_if_no_more_attempts(attempts):
                print("You ran out of attempts. You lost.")
                break
            print("Too high. Guess again")
        elif user_guess < CORRECT_NUMBER:
            attempts -= 1
            if check_if_no_more_attempts(attempts):
                print("You ran out of attempts. You lost.")
                break
            print("Too low. Guess again.")
        else:
            print("\n" * 20)
            print("You guessed the correct number!! You win!")
            break

def game():
    print("\n" * 20)
    print("Welcome to the number guessing game! \nI'm thinking of a number between 0 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


    if difficulty == 'easy':
        easy_game()
    elif difficulty == 'hard':
        hard_game()
    else:
        print("Please choose difficulty.")

game()