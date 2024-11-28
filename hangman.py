import random
import hangman_art
#Laget en egen fil med hangman ord
import hangman_words

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#Velger et tilfeldig ord fra listen
chosen_word = random.choice(hangman_words.word_list)
placeholder = ""

#Viser først frem masse "_"
for letter in chosen_word:
    placeholder += "_"
print(chosen_word)
print(placeholder)

#Når jeg setter denne til true inni loopen så vil loopen avsluttes
game_over = False
#Denne må lages utenfor loopen slik at den ikke blir oppdatert for hver gang
matched_guesses = []

#Antall liv man har
lives = 6
print(hangman_art.logo)
while not game_over:
    display = ""

    guess = input("Guess a letter in the word: ").lower()
    if guess in matched_guesses:
        print("You've have already guessed: ", guess)
    
    #Dette er hvis bruker gjetter feil
    if guess not in chosen_word:
        lives -= 1
        print(hangman_art.stages[lives])
        print("You guessed ", guess, " that's not in the word. You lose a life.")
        print("*****************************", lives , "/6 lives left ***********************************")
        if lives == 0:
            game_over = True
            print("You lose. The correct word was: ", chosen_word)
    #Leter gjennom hver bokstad i chosen_word
    for letter in chosen_word:
        #Hvis én av bokstavene er lik det man gjettet så legger man det til display        
        if guess == letter:
            display += letter
            #Dersom du får en riktig må vi måle den opp mot det vi allerede har gjettet
            matched_guesses.append(guess)
        
        #Hvis vi allerede har gjettet den så viser vi den frem også
        elif letter in matched_guesses:
            display += letter
        #Hvis ikke så viser vi "_"
        else:
            display += "_"

    #Hvis det ikke er flere "_" så har man vunnet
    if "_" not in display:
        print("You've won. Game over.")
        game_over = True

    print(display)

