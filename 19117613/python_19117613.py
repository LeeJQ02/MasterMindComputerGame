import random 

# Welcome menu
def welcome():
    print()
    print(" ----------------------------------- ")
    print("           MASTER MIND GAME ")
    print(" ----------------------------------- ")
    print("Welcome to the MASTER MIND GAME")
    print("[1] Instruction")
    print("[2] Start game")
    print("[3] Exit game")

# Instruction menu
def instruction():
    print()
    print("Computer will randomly choose 4 colours from the list and arrange in a order.\n"
    + "There are a total of 6 colours to choose from: (RED - R, GREEN - G, BLUE - B, YELLOW - Y, PURPLE - P, WHITE - W)\n"
    + "You must guess the 4 correct colours in the correct order to win the game.\n"
    + "After entering the colour code, computer will show player the clue:\n"
    + "0 shown means colour is correct with incorrect position.\n"
    + "1 shown means colour is in the correct position.\n"
    + "You are given 8 attempts only.\n"
    + "ENJOY! Goodluck out there.")

# Welcome selection menu
welcome()
user = int(input("Please enter the following number to continue: "))
if user == 1:
    instruction()
    game = True
elif user == 2: 
    game = True
elif user == 3:
    print("Exiting game ...")
    game = False
else:
    print("Invalid input. Exiting game...")
    game = False

# Colors list 
coloursList = ["R", "G", "B", "Y", "P", "W"]
# Secret code
secretCode = random.sample(coloursList, 4)
# print(secretCode)

# Initailize
count = 0
attempts = 8

# Game
while game == True:
    # Initialize
    correctCode = ""
    guessedCode = ""
    print()
    print("Please enter your colour code.\nR - RED\nG - GREEN\nB - BLUE\nY - YELLOW\nP - PURPLE\nW - WHITE")
    print("Example: RED GREEN BLUE WHITE --> RGBW ")
    # User input colours code
    userInput = str(input("\nPlease enter your 4 colours code: ").upper())

    # Check length of user input 
    if len(userInput) != len(secretCode):
        print("The secret code only has 4 colours. Please try again.")
        print(coloursList)
        continue
    # Check user input from colourList
    for i in range(1):
        if userInput[i] not in coloursList:
            print("Other colours out of this master mind game are not allowed. Please try again")
            print(coloursList)
            continue
    
    # Check user input colour code
    if correctCode != "1111":
        for i in range(4):
            if userInput[i] == secretCode[i]:
                correctCode += "1"
            if userInput[i] != secretCode[i] and userInput[i] in secretCode:
                guessedCode += "0"
        print()
        print("CLUE: ", correctCode + guessedCode)
    count += 1
    attempts -= 1

    if correctCode == "1111":
        if count == 1:
            print ("That is impressive that you did it on your first try! Congratulation!")
        else:
            print("You done it in " + str(count) + " times. Congratulation!")
        game = False
    
    # Check number of user input
    if count >= 1 and count < 8 and correctCode != "1111":
        print("This is your attempt number", count + 1)
        print("You still have", attempts, "attempts left.")
        print("Your guess is: ", [userInput])
        print()
        print("Next guess: ")
    elif count >= 8:
        print("You did not guess the correct secret code!\nThe secret code is: " + str(secretCode))
        game = False
    
    # Replay or end the game
    while game == False:
        end = input(str("Do want to play again? (Y/N)")).upper()
        count = 0
        if end == "N":
            print("Thank you for playing the game!")
            break
        elif end == "Y":
            game = True
            print()
            print("Starting game... ")
            print()
        else:
            print("Invalid input. Please try again.")
            game == False
