"""
Description:
    PiXELL River Virtual ATM
Author:
    Jared W. Pelletier
Date:
    Created On; 2024-10-01 14:45
"""
import random
import os
from time import sleep

#Set with options to choose from
transactionOptions = {"D","W","Q"} 

#Random bank balance
currentBankBalance = float(random.randrange(-1000,10000))

##Text that will be used multiple times, but do not change
TEXT_BORDER = "****************************************"

#Interface Lines
COMPANY_NAME = "PIXELL RIVER FINANCIAL"
TITLE = "ATM Simulator"
DEPOSIT_OPTION = "Deposit: D"
WITHDRAWL_OPTION = "Withdrawl: W"
QUIT_OPTION = "Quit: Q"

#Other Lines
ENTER_SELECTION = "Enter your selection: "
ENTER_AMOUNT = "Enter amount of transaction: "

#Invalid Selection
printInvalidSelection = [TEXT_BORDER, "INVALID SELECTION", TEXT_BORDER]

#Insuffiect Funds
printInsufficientFunds = [TEXT_BORDER, "INSUFFICIENT FUNDS", TEXT_BORDER]

#Clears screen before first display
os.system('cls' if os.name == 'nt' else 'clear')

#Main program loop
running = True
while running == True:
    #Reset deposit/widthdrawl values, otherwise they maintain their values each loop
    desiredDepositAmount = 0
    desiredWithdrawlAmount = 0

    #Update interface so it displays the correct values
    printInterface = [TEXT_BORDER,COMPANY_NAME,TITLE,f"Your current balance is: ${currentBankBalance:,.2f}",DEPOSIT_OPTION,WITHDRAWL_OPTION,QUIT_OPTION,TEXT_BORDER]
    
    #print user interface
    for line in printInterface:
        print(line.center(40))

    #This while loop is for when the user inputs a wrong selection, it will re-prompt them for an answer
    prompting = True
    while prompting == True: 
        userSelection = input(ENTER_SELECTION).upper()
        #Check to see if selection is valid
        if userSelection not in transactionOptions: 
            for line in printInvalidSelection:
                print(line.center(40))

        #Selection was accepted, moving on:        
        else:
            #Deposit Cash
            if userSelection == "D":
                #Take input -> convert to float -> add to currentBankBalance
                desiredDepositAmount = float(input(ENTER_AMOUNT))
                currentBankBalance += desiredDepositAmount
                
                #Print updated interface
                printCurrentBalance = [TEXT_BORDER, f"Your current balance is: ${currentBankBalance:,.2f}", TEXT_BORDER]
                for line in printCurrentBalance:
                    print(line.center(40))
                
                #Pause -> Clear Screen -> Exit prompting loop, restarting program with updated values
                sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                prompting = False

            #Withdrawl Cash
            elif userSelection == "W":
                #Take input, convert to float
                desiredWithdrawlAmount = float(input(ENTER_AMOUNT))

                #Check to see if desired withdrawl is possible
                if desiredWithdrawlAmount > currentBankBalance:
                    #Print the error message
                    for line in printInvalidSelection:
                        print(line.center(40))
                    
                    #Then remind them of what thier current balance is
                    printCurrentBalance = [TEXT_BORDER, f"Your current balance is: ${currentBankBalance:,.2f}", TEXT_BORDER]
                    for line in printCurrentBalance:
                        print(line.center(40))

                    #Pause -> Clear Screen -> Exit prompting loop
                    sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    prompting = False

                #If check passes, whithdrawl amount
                else:
                    #Withdrawl caluculate
                    currentBankBalance -= desiredWithdrawlAmount

                    #Print current balance with updated values
                    printCurrentBalance = [TEXT_BORDER, f"Your current balance is: ${currentBankBalance:,.2f}", TEXT_BORDER]
                    for line in printCurrentBalance:
                        print(line.center(40))
                    
                    #Pause -> Clear Screen -> Exit prompting loop
                    sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    prompting = False
            
            #If user selects the Quit option
            elif userSelection == "Q":
                #Display balance
                printCurrentBalance = [TEXT_BORDER, f"Your current balance is: ${currentBankBalance:,.2f}", TEXT_BORDER]
                for line in printCurrentBalance:
                    print(line.center(40))

                #Pause -> Clear Screen -> Exit both loops
                sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                prompting = False #Need to stop prompting user otherwise the second loop never stops
                running = False   #Exit loop, thus exiting the program