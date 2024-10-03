"""
Description:
    Processes account data to determine interest earned
Author:
    Jared W. Pelletier
Date:
    Created On; 2024-10-01 14:46
"""

from pprint import pprint
import csv

#Create empty dictionary
accountBalances = {}

#Populates accountBalances with values from account_balances.txt
with open("account_balances.txt", "r") as accountDetails:
    for line in accountDetails:
        key, value = line.strip().split("|")
        accountBalances[key] = float(value)
#Test print to see if it is reading correct values
print("----------Read from account_balances.txt----------")
pprint(accountBalances)
print("--------------------------------------------------")

#Iterate through lines and modify their values according to their coresponding rates
for line in accountBalances:
    if accountBalances[line] >= 5000: #Interest rate of 5.0
        accountBalances[line] += ((accountBalances[line] * 0.05) /12)

    elif accountBalances[line] >=1000: #Interest rate of 1.0
        accountBalances[line] += ((accountBalances[line] * 0.025) /12)

    elif accountBalances[line] > 0: #Interest rate of 2.5
        accountBalances[line] += ((accountBalances[line] * 0.01) /12)

    elif accountBalances[line] < 0: #Interest rate of 10
        accountBalances[line] += ((accountBalances[line] * 0.1) /12)
        
#Test print to see if the values have beed modified
print("--------Modify account balances and display-------")
pprint(accountBalances)
print("--------------------------------------------------")

#Creates(If not created) and writes to updated_balances_JP.csv
fieldNames = ["Account", "Balance"]
with open("updated_balances_JP.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldNames) #Set header
    writer.writeheader()#Write header
    for account, balance in accountBalances.items(): #Write to the csv file
        writer.writerow({'Account': account, 'Balance': balance})

#Reads from the previously created CSV file and prints to console
print("------Display From updated_balances_JP.csv--------")
with open("updated_balances_JP.csv", "r")as file:#Open CSV file and read data
    reader = csv.DictReader(file)
    for line in reader:#Print each line to console
        print(line['Account'], line['Balance'])
print("--------------------------------------------------")