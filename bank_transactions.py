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

#Text that will be used
textBorder = "****************************************"
interfaceLine1 = "ATM Simulator"
interfaceLine2 = f"Your current balance is: ${currentBankBalance:,.2f}"
interfaceLine3 = "Deposit: D"
interfaceLine4 = "Withdrawl: W"
interfaceLine5 = "Quit: D"
invalidSelection = "INVALID SELECTION"
#Maybe change these to be more clear?
#Finish the rest of the script incase the potential names conflict
#Main Interface
printInterface = [textBorder,interfaceLine1,interfaceLine2,interfaceLine3,interfaceLine4,interfaceLine5,textBorder]

#Invalid Selection
printInvalidSelection = [textBorder, invalidSelection, textBorder]

#print user interface
for line in printInterface:
    print(line.center(40))


