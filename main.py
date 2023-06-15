# Game Project

# Main Program Loop

loop = True
while loop:
    # Define reinforcement values
    reinforcements = 0 
    fakeReinforcements = 0 

    # Print Main Menu
    print("\nFinal Project Game")
    print("1 - Play Game")
    print("2 - Exit")

    # Get menu selection
    selection = input("Enter selection (1/2): ")

    if selection == "1":
        print("Game started!")

        # Functions Below!
        def startRound():
            # Set up game
            print("\nWill you - ")
            print("1 - Shoot? (" + str(reinforcements) + " attacks left.)")
            print("2 - Defend?")
            print("3 - Call reinforcements?")

            # Get user selection 
            choice = input("What is your selection? ")
            print("")
            return choice
        
            # Remind the user what they chose
        def tellChoice(choice, reinforcements):
            if choice == "1":
                if reinforcements > 0:
                    print("User chooses to shoot!")
                    reinforcements = reinforcements - 1
                else:
                    print("User chooses to shoot, but has no reinforcements! Turn is forfeited.")
                    choice = 0
            elif choice == "2":
                print("User chooses to defend!")
            elif choice == "3":
                print("User chooses to call reinforcements!")
                reinforcements = reinforcements + 1

        def getFakeChoice():
            # Make a random selection
                import random
                fakeChoice = random.randrange(1, 4)
                return fakeChoice
            
        def tellFakeChoice(fakeChoice, fakeReinforcements):
            if fakeChoice == "1":
                if fakeReinforcements > 0:
                    print("Server chooses to shoot!")
                    fakeReinforcements = fakeReinforcements - 1
                else:
                    print("Server chooses to shoot, but has no reinforcements! Turn is forfeited.")
                    fakeChoice = 0
            elif fakeChoice == "2":
                print("Server chooses to defend!")
            elif fakeChoice == "3":
                print("Server chooses to call reinforcements!")
                fakeReinforcements = fakeReinforcements + 1

        # Get the user choice
        choice = startRound()
        
        # Run function
        tellChoice(choice, reinforcements)

        # Get the server choice
        fakeChoice = getFakeChoice()
        print("fakeChoice is " + str(fakeChoice) + "!")

        # Tell the user what the server chose
        tellFakeChoice(fakeChoice, fakeReinforcements)


        
    # End Loop
    elif selection == "2":
        print("EXIT")
        loop = False