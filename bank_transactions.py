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
textBorder = "****************************************"

#Interface Lines
companyName = "PIXELL RIVER FINANCIAL"
title = "ATM Simulator"
depositOption = "Deposit: D"
withdrawlOption = "Withdrawl: W"
quitOption = "Quit: Q"

#Other Lines
enterSelection = "Enter your selection: "
enterAmmount = "Enter amount of transaction: "

#Invalid Selection
printInvalidSelection = [textBorder, "INVALID SELECTION", textBorder]

#Insuffiect Funds
printInsufficientFunds = [textBorder, "INSUFFICIENT FUNDS", textBorder]

#Clears screen before first display
os.system('cls' if os.name == 'nt' else 'clear')

#Main program loop
running = True
while running == True:
    #Reset deposit/widthdrawl values, otherwise they maintain their values each loop
    desiredDepositAmount = 0
    desiredWithdrawlAmount = 0

    #Update interface so it displays the correct values
    printInterface = [textBorder,companyName,title,f"Your current balance is: ${currentBankBalance:,.2f}",depositOption,withdrawlOption,quitOption,textBorder]
    
    #print user interface
    for line in printInterface:
        print(line.center(40))

    #This while loop is for when the user inputs a wrong selection, it will re-prompt them for an answer
    prompting = True
    while prompting == True: 
        userSelection = input(enterSelection).upper()
        #Check to see if selection is valid
        if userSelection not in transactionOptions: 
            for line in printInvalidSelection:
                print(line.center(40))

        #Selection was accepted, moving on:        
        else:
            #Deposit Cash
            if userSelection == "D":
                #Take input -> convert to float -> add to currentBankBalance
                desiredDepositAmount = float(input(enterAmmount))
                currentBankBalance += desiredDepositAmount
                
                #Print updated interface
                printCurrentBalance = [textBorder, f"Your current balance is: ${currentBankBalance:,.2f}", textBorder]
                for line in printCurrentBalance:
                    print(line.center(40))
                
                #Pause -> Clear Screen -> Exit prompting loop, restarting program with updated values
                sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                prompting = False

            #Withdrawl Cash
            elif userSelection == "W":
                #Take input, convert to float
                desiredWithdrawlAmount = float(input(enterAmmount))

                #Check to see if desired withdrawl is possible
                if desiredWithdrawlAmount > currentBankBalance:
                    #Print the error message
                    for line in printInvalidSelection:
                        print(line.center(40))
                    
                    #Then remind them of what thier current balance is
                    printCurrentBalance = [textBorder, f"Your current balance is: ${currentBankBalance:,.2f}", textBorder]
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
                    printCurrentBalance = [textBorder, f"Your current balance is: ${currentBankBalance:,.2f}", textBorder]
                    for line in printCurrentBalance:
                        print(line.center(40))
                    
                    #Pause -> Clear Screen -> Exit prompting loop
                    sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    prompting = False
            
            #If user selects the Quit option
            elif userSelection == "Q":
                #Display balance
                printCurrentBalance = [textBorder, f"Your current balance is: ${currentBankBalance:,.2f}", textBorder]
                for line in printCurrentBalance:
                    print(line.center(40))

                #Pause -> Clear Screen -> Exit both loops
                sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                prompting = False #Need to stop prompting user otherwise the second loop never stops
                running = False   #Exit loop, thus exiting the program