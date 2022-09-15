import random

def rollDice():
    number = random.randint(1,6)
    return number

def welcome():
    print("\n\tWelcome to Dice Roll Simulator :D")
    input("\n\tPress Enter to roll the dice...")
    diceRoll()

def diceRoll():
    print("\n\n\tRolling Dice...")
    print("\n\tThe rolled number is {}".format(rollDice()))
    playAgain()

def playAgain():
    choice = str(input("\nDo you want to roll the dice again? (y/n)"))

    if choice=="y":
        diceRoll()
    else:
         exit()

welcome()
