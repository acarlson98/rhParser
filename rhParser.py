# Robinhood Parser v0.1
# Andrew Carlson

import sys
import pandas as pd
df = pd.read_csv(sys.argv[1], on_bad_lines='warn')

# Print preview of dataframe
print(df)

from decimal import Decimal

# TODO: Get account value as argument?
accountValue = 5000

with open('output.txt', 'a') as f:
#    f.write('Hi')

    # This is a very slow iterator but shouldn't matter for now
    for index, row in df.iterrows():
        if row["Trans Code"] == "BTO":
            openingAmount = row["Amount"].replace("$","").replace(",","").replace("(","").replace(")","")
            #print(openingAmount)
            accountValue -= Decimal(openingAmount)
            print("Bought: " + row["Description"])
            print("New Value: " + str(accountValue))
            print()

        if row["Trans Code"] == "STC":
            closingAmount = row["Amount"].replace("$","").replace(",","").replace("(","").replace(")","")
            #print(closingAmount)
            accountValue += Decimal(closingAmount)
            print("Sold: " + row["Description"])
            print("New Value: " + str(accountValue))
            print()

#print(df['Process Date'].iloc[0])

# Activity Date
# Process Date
# Settle Date
# Instrument
# Description
# Trans Code
    # STC - Sell to close
    # BTO - Buy to open
# Quantity
# Price
# Amount

# Goal is to parse this data and put it into our trade chart
# Need:
    # Date
    # Option Title
    # Time Opened
    # Time in market
    # Win/Loss
    # Start price
    # End price
    # % Change
    # $ Change
    # Account Value
# Eventually:
    # Day result $
    # Day result %
