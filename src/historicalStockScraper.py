# historicalStockScraper.py 

import os 
import sys
from utils import *
from datetime import datetime
import pandas as pd
import pandas_datareader.data as web

USAGE_STR = """
# Purpose
# For a list of ticker symbols, generate historical stock data at the daily granularity 

# Usage 
# python historicalStockScraper.py <TICKER_SYMBOL_LIST> <BEG_DATE> <Optional END_DATE>

# Arguments
# <TICKER_SYMBOL_LIST> List of acronyms for the stocks of interest delimited by new line 
# <BEG_DATE> Hyphen delimited begin date for stock (ie 1-12-2003)
# <END_DATE> Hyphen delimited end date for stock (ie 2-20-2009)
# If end date not specified then defaults to today's date 

# Example:
# python historicalStockScraper.py /afs/ir.stanford.edu/users/a/k/akma327/stats205/midterm-project/metastocks/data/ticker-lists/tech-ticker-list.txt 1-1-2003
"""

K_MIN_ARG = 3


def calcDailyDataForAllStocks(symbols, start, end):
	for symbol in symbols:
		print("Stock Info For: " + str(symbol))
		stock_info_from_google = web.DataReader("%s" %symbol, 'google', start, end)
		stock_info_from_google.to_csv('../data/historical-data/tech/%s_from_google.csv' %symbol)


if __name__ == "__main__":
	if(len(sys.argv) < K_MIN_ARG):
		print(USAGE_STR)
		exit(1)
	TICKER_LIST = sys.argv[1]
	BEG_DATE = sys.argv[2]
	END_DATE = None
	if(len(sys.argv) == 4):
		END_DATE = sys.argv[3]
	symbols = parseTickerList(TICKER_LIST)
	start = parseDate(BEG_DATE)
	end = parseDate(END_DATE)
	calcDailyDataForAllStocks(symbols, start, end)







