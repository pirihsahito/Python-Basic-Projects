#  Rock, Paper, Scissors Game (vs. The Computer)

import random

while True:
    computer = random.randint(1, 3)

    try:
        user = int(input("Press 1 for Rock 2 for Paper 3 for Scissors 4 for Exit: "))

        if user == 4:
            print("Thanks for playing! Goodbye.")
            break
        
        print("You chose:", user)
        print("Computer chose:", computer)

        if user == computer:
            print("DRAW!")

        elif user == 1:
            if computer == 2:
                print("YOU LOSS!")
            else:
                print("YOU WON!")

        elif user == 2:
            if computer == 1:
                print("YOU WON!")
            else:
                print("YOU LOSS!")

        elif user == 3:
            if computer == 1:
                print("YOU LOSS!")
            else:
                print("YOU WON!")

        else:
            print("Invalid number! Please choose 1, 2, or 3.")
    except ValueError:
        print("Invalid input! You must type a number, not text.")