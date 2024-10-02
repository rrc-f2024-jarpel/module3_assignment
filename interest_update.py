"""
Description:
    Processes account data to determine interest earned
Author:
    Jared W. Pelletier
Date:
    Created On; 2024-10-01 14:46
"""
#This is for debuggig purposes, remove later if needed
from pprint import pprint


accountBalances = {}
with open("account_balances.txt", "r") as accountDetails:
    for line in accountDetails:
        key, value = line.strip().split("|")
        accountBalances[key] = float(value)

pprint(accountBalances)