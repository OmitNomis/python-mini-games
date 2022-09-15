import random

def coinToss():
    toss = random.randint(1,2)
    if toss == 1:
        return "Heads"
    else:
        return "Tails"

def tossCoin():
    print("\n\tTossing coin...")
    print("\n\tThe result is {}".format(coinToss()))
    playAgain()

def playAgain():
    choice = str(input("\n\nDo you want to toss the coin again? (y/n): "))
    if choice == "y":
        tossCoin()
    else:
        exit()
    
    
    
def welcome():
    print("\n\tWelcome to the coin toss game :D")
    input("\n\tPress Enter to toss the coin ... ")

    tossCoin()

welcome()

