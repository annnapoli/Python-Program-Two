#### BlackJack Dice Program
####
##1.	You have money
##2.	You make bet
##3.	You roll 2 dice
##4.	Dealer rolls 2 dice
##    a.	Roll again?
##    b.	Repeat until:
##        i.	# > 21
##        ii.	# <= 21
##            1.	dealer rolls same # rolls you did
##            2.	if dealer > you  you lose
##            3.	if dealer < you  you win
##            4.	if dealer = you  push
##5.	Play again?
##6.	Play until money = 0
####12.If possible, add a HELP feature, where if the player enters “H” the rules of BlackJack Dice show up.  

import random

############THIS IS HOW YOU START THE GAME################

###THIS IS HOW MUCH MONEY THEYRE GONNA SPEND###
Money = int(input("How much money do you have? "))
while Money <= 0:
    print("You came to the game with no money? Try again.")
    print("")
    Money = int(input("How much money do you really have? "))

###THIS IS HOW MUCH THEY ARE GOING TO BET###
Wager = int(input("How much would you like to bet this round? "))
while Wager <= 0 or Wager > Money:
    print("Nice try wise guy. You have to make a bet.")
    print('')
    Wager = int(input("How much would you like to bet this round? "))

print('')
print('')

###THIS IS HOW THE GAME STARTS###
Play = input('Shall we play a game? [Y/N]')
Play = Play.upper()
if Play not in ("Y", "YES", "N", "NO"):
    print("Please answer yes or no")
    Play = input('Shall we play a game? [Y/N]')
print('')

#############VARIABLES#############

Money -= Wager
Rolls = 0
Rounds = 0
DRolls = 0

#############ACTUAL CODE#############

while Money > 0 and Play in ("Y", "YES"):
    Rounds +=1
    DDie1 = random.randint(1,6)
    DDie2 = random.randint(1,6)
    TotalDRoll = DDie1 + DDie2

    PDie1 = random.randint(1,6)
    PDie2 = random.randint(1,6)
    TotalPRoll = PDie1 + PDie2
###DEALER ROLLS, YOU ROLL###
    print("You rolled", TotalPRoll)
    print('')
    Rolls += 1
    print("The Dealer rolled", TotalDRoll)
    print('')
    DRolls += 1
###ROLL AGAIN GENERAL LOOP###    
    Again = input("Would you like to roll again? [Y/N] ")
    Again = Again.upper()
    if Again not in ("Y", "YES", "N", "NO"):
        print("Please answer yes or no")
        Again = input("Would you like to roll again?")
    while Again in ("Y", "YES") and TotalPRoll < 21:
        Rolls += 1
        RollAgain = random.randint(1,6)
        TotalPRoll += RollAgain
        print("You rolled ", RollAgain)
        print("Your total is now ", TotalPRoll)
###KEEP ROLLING IF YOU HAVENT GOTTEN TO OR PAST 21 YET###
        if TotalPRoll < 21:
            Again = input("Would you like to roll again? [Y/N] ")
            Again = Again.upper()
            if Again not in ("Y", "YES", "N", "NO"):
                print("Please answer yes or no")
                Again = input("Would you like to roll again?")
###THE DEALER ROLLS AS MANY TIMES AS YOU DID###
    else:
        while TotalDRoll <= 20:
            DealerRolls = random.randint(1,6)
            print("The Dealer rolled ", DealerRolls)
            TotalDRoll += DealerRolls
            DRolls += 1
###IF DEALER IS BUST OR LESS THAN YOU, YOU WIN###
        elif TotalDRoll > TotalPRoll or TotalPRoll > 21:
            print("You lose.")
            Money -= Wager
            print("You now have ", Money, "dollars")
            Play = input("Would you like to play again? [Y/N]")
            Play = Play.upper()
            if Play not in ("Y", "YES", "N", "NO"):
                print("Please answer yes or no")
                Play = input('Shall we play a game? [Y/N]')
###IF YOU ARE BUST OR DEALER ROLLS MORE THAN YOU, YOU LOSE###
###MAYBE SWITCH THE IF AND EILF###
        if TotalPRoll > TotalDRoll or TotalDRoll > 21:
            print("Congratulations! You win!")
            Money += Wager
            print("You now have ", Money, "dollars")
            Play = input("Would you like to play again? [Y/N]")
            Play = Play.upper()
            if Play not in ("Y", "YES", "N", "NO"):
                print("Please answer yes or no")
                Play = input('Shall we play a game? [Y/N]')
###IF ITS A TIE, ITS A PUSH AND NO ONE WINS###
        else:
            print("You are push, no one wins.")
            print("You still have ", Money, "dollars.")
            Play = input("Would you like to play again? [Y/N]")
            Play = Play.upper()
            if Play not in ("Y", "YES", "N", "NO"):
                print("Please answer yes or no")
                Play = input('Shall we play a game? [Y/N]')
                      
###WHEN YOU ARE OUT OF MONEY, OR YOU NEVER PLAYED AT ALL, YOURE DONE###       
else:
    print("Thank you for playing!")
    print("You played ", Rounds, "rounds.")
            
    



