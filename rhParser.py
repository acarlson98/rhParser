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

dailyGains = dict()
dailyAccountValue = dict()

# This is a very slow iterator but shouldn't matter for now
for index, row in df.iterrows():
    if row["Trans Code"] == "BTO":
        openingAmount = row["Amount"].replace("$","").replace(",","").replace("(","").replace(")","")
        accountValue -= Decimal(openingAmount)
        if row["Activity Date"] in dailyGains:
            dailyGains[row["Activity Date"]] -= Decimal(openingAmount)
        else:
            dailyGains[row["Activity Date"]] = -Decimal(openingAmount)

    if row["Trans Code"] == "STC":
        closingAmount = row["Amount"].replace("$","").replace(",","").replace("(","").replace(")","")
        accountValue += Decimal(closingAmount)
        dailyAccountValue[row["Activity Date"]] = accountValue
        if row["Activity Date"] in dailyGains:
            dailyGains[row["Activity Date"]] += Decimal(closingAmount)
        else:
            dailyGains[row["Activity Date"]] = Decimal(closingAmount)

print("Result: $" + str(accountValue) + "\n")
#f.write("Result: $" + str(accountValue) + "\n")

outputFrame = pd.DataFrame(dailyGains, index=[0])
outputFrameTransposed = outputFrame.T

print("Outputting results to dailyGains.csv...")
outputFrameTransposed.to_csv("dailyGains.csv")

# dailyAccountValue isn't working yet, probably because the keys are in backwards?

#outputFrame = pd.DataFrame(dailyAccountValue, index=[0])
#outputFrameTransposed = outputFrame.T

#print("Outputting results to dailyAccountValue.csv...")
#outputFrameTransposed.to_csv("dailyAccountValue.csv")
