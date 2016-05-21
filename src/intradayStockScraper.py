# intradayStockScraper.py

import sys
import os 
from datetime import datetime
import pandas as pd
import pandas_datareader.data as web
import requests 
from utils import *

USAGE_STR = """
# Usage:
# python intradayStockScraper.py <TICKER_SYMBOL_LIST> 

# Arguments:
# <TICKER_SYMBOL_LIST> List of acronyms for the stocks of interest delimited by new line 

# Example:
# TICKER_LIST="/afs/ir.stanford.edu/users/a/k/akma327/stats205/midterm-project/metastocks/data/ticker-lists/042816-samp.txt"
# python intradayStockScraper.py $TICKER_LIST

"""

def get_intraday_data(symbol, interval_seconds=301, num_days=10):
    # Specify URL string based on function inputs.
    url_string = 'http://www.google.com/finance/getprices?q={0}'.format(symbol.upper())
    url_string += "&i={0}&p={1}d&f=d,o,h,l,c,v".format(interval_seconds,num_days)
    # Request the text, and split by each line
    r = requests.get(url_string).text.split()
    # Split each line by a comma, starting at the 8th line
    r = [line.split(',') for line in r[7:]]
    # Save data in Pandas DataFrame
    df = pd.DataFrame(r,columns=['Datetime','Close','High','Low','Open','Volume'])
    # Convert UNIX to Datetime format
    df['Datetime'] = df['Datetime'].apply(lambda x:datetime.fromtimestamp(int(x[1:])))
    return df

def calcDataForAllStocks(symbols):
    for symbol in symbols:
        print("Stock Info For: " + str(symbol))
        try:
            df = get_intraday_data(symbol)
            df.to_csv('../data/intra-day-data/042816-batch/%s_from_google.csv' %symbol)
        except:
            print("skipping stock: " + symbol)





if __name__ == "__main__":
    TICKER_LIST = sys.argv[1]
    symbols = parseTickerList(TICKER_LIST)
    calcDataForAllStocks(symbols)




