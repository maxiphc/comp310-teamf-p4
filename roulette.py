from randomizer import PseudoRandom

#random value generated from randomizer.py is used to display whether user placed the winning bet

def playRoulette(betAmount, bankroll):
    
        randomizer = PseudoRandom()                               
        new_rand = randomizer.generate_random(randomizer.prev,36)
        
        #asks user to input their own bet
        while(True):
            try:
                userBet = int(input(f"\nEnter a number between 0-36, Red/Odd Numbers (37), or Black/Even Numbers (38): "))
                if userBet > 38 or userBet < 0:
                    print(f'{userBet} is not a legitable option. Try again.')
                    continue
                break
            except ValueError:
                print(f"{userBet} is not a real number silly. Try again.")
                continue


        # user bets correctly on single number, 35-1 odds
        if new_rand == userBet and userBet <= 35:

            # user guesses single number correctly, 35 to 1 odds. 
            if userBet <= 36:
                payout = betAmount * 35 
                print(f"\nYou bet on the number {userBet}. The winning bet was {str(new_rand)}. Congrats you won ${payout}!")

        # user bets on red (all odd numbers), even odds, 
        elif userBet == 37:

            # they are correct
            if (new_rand % 2) == 1:
                payout = betAmount * 2
                print(f"\nYou bet on Red. The winning bet was {str(new_rand)} (Red) Congrats you won ${payout}")
                return payout

            else:
                print(f"\nThe winning bet was {str(new_rand)} (Black). You lost ${betAmount}")
                return -1

        # user bets on black, even odds
        elif userBet == 38:
            if (new_rand % 2) == 0:
                payout = betAmount * 2
                print(f"\nYou bet on Black. The winning bet was {str(new_rand)} (Black). Congrats you won ${payout}")
                return payout
            else:
                print(f"\nThe winning bet was {str(new_rand)} (Red). You lost ${betAmount}")
                return -1

        #if user types bet that does not equal random number that was generated in randomizer.py they lose
        else:
                print(f"\nYou bet on the number {userBet}. The winning bet was {str(new_rand)}. You lost ${betAmount}")
                return -1

bankroll = 100
while bankroll > 0:
    #asks user if they want to bet or continue betting
    userChoice = str(input('\nDo you want to place a bet? (y/n): '))

    #checks if the choice is valid or not 
    if userChoice not in ('y', 'n'):
        print("\nInvalid input.")
        continue

    # runs game if user types 'y' 
    if userChoice == 'y':
        
        while(True): 
            try:
                userBet = int(str(input(f'\nBetting on single number: \t35 to 1 \
                                            \nBetting on Red/Black: \t\t1 to 1 \
                                            \n\nYou have ${bankroll}.\nHow much would you like to bet? Please enter a whole number dollar amount: $')))
                if userBet < 0:
                    print("Not a valid amount. Try again.")
                    continue
                if userBet > bankroll:
                    print("You don't have that much money! Try again.")
                    continue
                else:
                    breakLoop = True
                    break
                
            except ValueError:
                print("Enter a real number.")
                continue
    

        result = playRoulette(userBet, bankroll)
        if result == -1:
            bankroll -= userBet
        else:
            bankroll += (result - userBet)

                
    #says goodbye to user if they type 'n' 
    else:
        print(f"\nThank you for betting. You ended with ${bankroll} Goodbye.\n")
        break

print('You lost. Run the program to play again! Goodbye.')
    