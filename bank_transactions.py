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

transactionOptions = {"D","W","Q"} 
currentBankBalance = float(random.randrange(-1000,10000))
#Text that will be used multiple times.
textBorder = "****************************************"
#Interface Lines
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

running = True
while running == True:
    #Reset deposit/widthdrawl values, otherwise they maintain their values each loop
    desiredDepositAmount = 0
    desiredWithdrawlAmount = 0
    #Update interface so it displays the correct values
    printInterface = [textBorder,title,f"Your current balance is: ${currentBankBalance:,.2f}",depositOption,withdrawlOption,quitOption,textBorder]
    #print user interface
    for line in printInterface:
        print(line.center(40))
    prompting = True
    while prompting == True: # This while loop is for when the user inputs a wrong selection.
        userSelection = input(enterSelection).upper()
        if userSelection not in transactionOptions: # Check to see if selection is valid
            for line in printInvalidSelection:
                print(line.center(40))
        else:#Selection was accepted, moving on:
            if userSelection == "D": #Deposit Cash
                desiredDepositAmount = float(input(enterAmmount))#Take input, convert to float
                currentBankBalance += desiredDepositAmount
                printCurrentBalance = [textBorder, f"Your current balance is: ${currentBankBalance:,.2f}", textBorder]
                for line in printCurrentBalance:
                    print(line.center(40))
                sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                prompting = False
            elif userSelection == "W": #Withdrawl cash
                desiredWithdrawlAmount = float(input(enterAmmount))#Take input, convert to float
                if desiredWithdrawlAmount > currentBankBalance: #Check to see if desired withdrawl is possible
                    for line in printInvalidSelection:#Print the error message
                        print(line.center(40))
                    printCurrentBalance = [textBorder, f"Your current balance is: ${currentBankBalance:,.2f}", textBorder]
                    for line in printCurrentBalance:#Then remind them of what thier current balance is
                        print(line.center(40))
                    sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    prompting = False
                else: #If check passes, whithdrawl amount
                    currentBankBalance -= desiredWithdrawlAmount
                    printCurrentBalance = [textBorder, f"Your current balance is: ${currentBankBalance:,.2f}", textBorder]
                    for line in printCurrentBalance:
                        print(line.center(40))
                    sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    prompting = False
            elif userSelection == "Q": #User wishes to quit the program
                printCurrentBalance = [textBorder, f"Your current balance is: ${currentBankBalance:,.2f}", textBorder]
                for line in printCurrentBalance:
                    print(line.center(40))
                sleep(3)
                prompting = False #Need to stop prompting user otherwise the second loop never stops
                running = False   #Exit loop, thus exiting the program