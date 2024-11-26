import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

handsignals = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#Computer velger en tilfeldig innenfor 
computer_choice = random.choice(handsignals)
if your_choice != 1 or your_choice != 2 or your_choice != 3:
    print("You typed a wrong number")
else:
    print(handsignals[your_choice])
    print("Computer chose:")
    print(computer_choice)

    if handsignals[your_choice] == computer_choice:
        print("It's a tie")

    elif handsignals[your_choice] == handsignals[0] and computer_choice == handsignals[2] or handsignals[your_choice] == handsignals[1] and computer_choice == handsignals[0] or handsignals[your_choice] == handsignals[2] and computer_choice == handsignals[1]:
        print("You win")

    else:
        print("You lose")

