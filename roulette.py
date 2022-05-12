from randomizer import PseudoRandom

#random value generated from randomizer.py is used to display whether user placed the winning bet

def playRoulette():
    
    #the class declartion inside the function so that each time the function is called a new no is generated 
    randomizer = PseudoRandom()                               
    new_rand = randomizer.generate_random(randomizer.prev,38)
    
    #asks user to input their own bet
    userBet = int(input("\nEnter a number between 0-36, Red (37), or Black (38): "))


    #compares random number generated in randomizer.py to the user's bet to see if they are equal
    if new_rand == userBet:

        if userBet <= 36:

            print("\nYou bet on the number " + str(userBet) +". Congrats you won!")

        elif userBet == 37:

            print("\nYou bet on Red. Congrats you won!")

        elif userBet == 38:

            print("\nYou bet on Black. Congrats you won!")

        #if user types a bet higher than 38 it is invalid

    elif userBet > 38:

            print("\nYour bet is invalid. Please try again.")

        #if user types bet that does not equal random number that was generated in randomizer.py they lose

    else:

            print("\nThe winning bet was " +str(new_rand) +". You lost.")



while True:

    #asks user if they want to bet or continue betting
    userChoice = str(input('\nDo you want to place a bet? (y/n): '))

    #checks if the choice is valid or not 
    if userChoice not in ('y', 'n'):
        print("\nInvalid input.")
        break

    
    # runs game if user types 'y' 
    if userChoice == 'y':
        playRoulette()
        
    
    #says goodbye to user if they type 'n' 
    else:

        print("\nThank you for betting. Goodbye.\n")

        break