import num2words as n2w


def numberToWords():
    givenNum = float(input("\n\tEnter a number: "))
    numInWords = n2w.num2words(givenNum)
    print("\n\t",str(numInWords).capitalize())
    runAgain()

def runAgain():
    choice = input("\nDo you want convert another number? (y/n)")

    if choice=="y":
        numberToWords()
    else:
         exit()

print ("\n\tWelcome to Number to Words!")
numberToWords()

