# rhParser

Goal of the project is to parse Robinhood CSV Export files and put it into our personal trade chart format.

## Requirements

This is a python script. [Python can be downloaded here.](https://www.python.org/downloads/)

This script requires pandas to run, which can be installed using pip (pip should be installed along with Python).

`pip install pandas`

The newer versions of pandas also require pyarrow, so install that too.

`pip install pyarrow`

## Robinhood CSV Export contains the following columns:

* Activity Date
* Process Date
* Settle Date
* Instrument
* Description
* Trans Code
    * STC - Sell to close
    * BTO - Buy to open
* Quantity
* Price
* Amount

## Our format:

### Need the following columns:

* Date
* Option Title
* Time Opened
* Time in market
* Win/Loss (binary)
* Start price
* End price

### These can be calculated in Sheets/Excel:

* % Change
* $ Change
* Account Value
* Day result $
* Day result %
