import randomizer
    
#while True:

new_rand = randomizer.rand

#random value generated from randomizer.py is used to display whether user placed the winning bet
def playRoulette():

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

playRoulette()

    # while True:

    #     userChoice = str(input('\nDo you want to bet again? (y/n): '))

    #     if userChoice in ('y', 'n'):
    #         break
    #     print("\nInvalid input.")
    # if userChoice == 'y':
    #     continue
    # else:
    #     print("\nThank you for betting. Goodbye.")
    #     break
