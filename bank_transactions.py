"""
Description:
    PiXELL River Virtual ATM
Author:
    Jared W. Pelletier
Date:
    Created On; 2024-10-01 14:45
"""
import random
transactionOptions = {"D","W","Q"} 
#Later, when first handling interaction, check
#to see if the value input is in this list
currentBankBalance = float(random.randrange(-1000,10000))

#Text that will be used multiple times.
textBorder = "****************************************"
#Interface Lines
title = "ATM Simulator"
currentBalanceText = f"Your current balance is: ${currentBankBalance:,.2f}"
depositOption = "Deposit: D"
withdrawlOption = "Withdrawl: W"
quitOption = "Quit: Q"

#Other Lines
enterSelection = "Enter your selection: "
enterAmmount = "Enter amount of transaction: "

#Main Interface
printInterface = [textBorder,title,currentBalanceText,depositOption,withdrawlOption,quitOption,textBorder]

#Invalid Selection
printInvalidSelection = [textBorder, "INVALID SELECTION", textBorder]

#Insuffiect Funds
printInsufficientFunds = [textBorder, "INSUFFICIENT FUNDS", textBorder]


#print user interface
for line in printInterface:
    print(line.center(40))

userSelection = input(enterSelection).upper()
if userSelection not in transactionOptions:
    for line in printInvalidSelection:
        print(line.center(40))
else:
    if userSelection == "D":
        desiredDepositAmount = float(input(enterAmmount))
        currentBankBalance += desiredDepositAmount
        printCurrentBalance = [textBorder, f"Your current balance is: ${currentBankBalance:,.2f}", textBorder]
        for line in printCurrentBalance:
            print(line.center(40))

    elif userSelection == "W":
        desiredWithdrawlAmount = float(input(enterAmmount))
        if desiredWithdrawlAmount > currentBankBalance:
            for line in printInvalidSelection:
                print(line.center(40))
        else:
            currentBankBalance -= desiredWithdrawlAmount
            printCurrentBalance = [textBorder, f"Your current balance is: ${currentBankBalance:,.2f}", textBorder]
            for line in printCurrentBalance:
                print(line.center(40))
    elif userSelection == "Q":
        printCurrentBalance = [textBorder, f"Your current balance is: ${currentBankBalance:,.2f}", textBorder]
        for line in printCurrentBalance:
            print(line.center(40))