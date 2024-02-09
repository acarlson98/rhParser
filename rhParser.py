# Robinhood Parser v0.1

import sys
import pandas as pd
df = pd.read_csv(sys.argv[1], on_bad_lines='warn')

# Print preview of dataframe
#print(df)

#TODO: Track P/L for specific trades
#TODO: Add option for tracking Robinhood Gold cash interest
#TODO: Reverse output order to match our spreadsheet style
#TODO: 2 columns instead of 2 rows

from decimal import Decimal

accountValue = 0

days = dict()

# This is a very slow iterator but shouldn't matter for now
for index, row in df.iterrows():
    if row["Trans Code"] == "BTO":
        openingAmount = row["Amount"].replace("$","").replace(",","").replace("(","").replace(")","")
        accountValue -= Decimal(openingAmount)
        if row["Settle Date"] in days:
            days[row["Settle Date"]] -= Decimal(openingAmount)
        else:
            days[row["Settle Date"]] = -Decimal(openingAmount)

    if row["Trans Code"] == "STC":
        closingAmount = row["Amount"].replace("$","").replace(",","").replace("(","").replace(")","")
        accountValue += Decimal(closingAmount)
        if row["Settle Date"] in days:
            days[row["Settle Date"]] += Decimal(closingAmount)
        else:
            days[row["Settle Date"]] = Decimal(closingAmount)

print("Result: $" + str(accountValue) + "\n")
#f.write("Result: $" + str(accountValue) + "\n")

outputFrame = pd.DataFrame(days, index=[0])

#for key in days:
#    outputFrame.concat(key, days[key])

print("Outputting results to output.csv...")
outputFrame.to_csv("output.csv")
