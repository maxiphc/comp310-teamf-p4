from randomizer import PseudoRandom

#random value generated from randomizer.py is used to display whether user placed the winning bet

def playRoulette(betAmount, bankroll):
    
        randomizer = PseudoRandom()                               
        new_rand = randomizer.generate_random(randomizer.prev,36)
        
        #asks user to input their own bet
        while(True):
            try:
                userBet = int(input(f"\nEnter a number between 0-36, Red/Odd Numbers (37), or Black/Even Numbers (38): "))
                break
            except TypeError:
                print(f"{userBet} is not a real number silly.")
                continue


        # user bets correctly on single number, 35-1 odds
        if new_rand == userBet and userBet <= 35:

            # user guesses single number correctly, 35 to 1 odds. 
            if userBet <= 36:
                payout = betAmount * 35 
                print("\nYou bet on the number " + str(userBet) + f". Congrats you won ${payout}!")

        # user bets on red (all odd numbers), even odds, 
        elif userBet == 37:

            # they are correct
            if (userBet % 2) == 1:
                payout = betAmount * 2
                print(f"\nYou bet on Red. It is Red. Congrats you won ${payout}")
                return payout

            else:
                print("\nThe winning bet was " +str(new_rand) + f", which is not Red. You lost ${userBet}")
                return -1

        # user bets on black, even odds
        elif userBet == 38:
            if (userBet % 2) == 0:
                payout = betAmount * 2
                print(f"\nYou bet on Black. It is black. Congrats you won ${payout}")
                return payout
            else:
                print("\nThe winning bet was " +str(new_rand) + f", which is not Black. You lost ${userBet}")
                return -1

        #if user types a bet higher than 38 it is invalid
        elif userBet > 38 or userBet < 0:
            print("\nYour bet is invalid. Please try again.")

        #if user types bet that does not equal random number that was generated in randomizer.py they lose
        else:
                print("\nThe winning bet was " +str(new_rand) + f". You lost ${userBet}")
                return -1

bankroll = 100
while bankroll > 0:
    #asks user if they want to bet or continue betting
    userChoice = str(input('\nDo you want to place a bet? (y/n): '))

    #checks if the choice is valid or not 
    if userChoice not in ('y', 'n'):
        print("\nInvalid input.")
        break

    # runs game if user types 'y' 
    if userChoice == 'y':
        while(True): 
            try:
                userBet = int(str(input(f'\nBetting on single number: \t35 to 1 \
                                            \nBetting on Red/Black: \t\t1 to 1 \
                                            \n\nYou have ${bankroll}.\nHow much would you like to bet? Please enter a whole number dollar amount: $')))

                if userBet > bankroll:
                    print("You don't have that much money! Try again.")
                else:
                    break

            except TypeError:
                print("Enter a real number.")
                continue

        result = playRoulette(userBet, bankroll)
        if result == -1:
            bankroll -= userBet
        else:
            bankroll += result

    #says goodbye to user if they type 'n' 
    else:
        print(f"\nThank you for betting. You ended with ${bankroll} Goodbye.\n")
        break

print('You lost. Run the program to play again! Goodbye.')
    