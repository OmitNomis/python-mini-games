
def slice():
    email = str(input("\n\tEnter the email you want to slice: "))
    splitText = email.split("@")

    print("\n\tSuccessful!!")
    print("\n\tUserName: {}".format(splitText[0]))
    print("\n\tDomain: {}".format(splitText[1]))
    sliceAgain()

def sliceAgain():
    choice = input("\nDo you want to slice another email? (y/n)")

    if choice=="y":
        slice()
    else:
         exit()
         
print("\n\tWelcome to Email Slicer :D")
slice()
    
