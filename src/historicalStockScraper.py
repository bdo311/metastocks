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
# python historicalStockScraper.py <TICKER_SYMBOL_LIST> <OUTPUT_FOLDER> <BEG_DATE> <Optional END_DATE>

# Arguments
# <TICKER_SYMBOL_LIST> List of acronyms for the stocks of interest delimited by new line 
# <OUTPUT_FOLDER> Absolute path to the output folder to store all the stock data 
# <BEG_DATE> Hyphen delimited begin date for stock (ie 1-12-2003)
# <END_DATE> Hyphen delimited end date for stock (ie 2-20-2009)
# If end date not specified then defaults to today's date 

# Example:
# setenv TICKER_SYMBOL_LIST "/afs/ir.stanford.edu/users/a/k/akma327/stats205/midterm-project/metastocks/data/ticker-lists/1-basic-materials-ticker-list.txt"
# setenv OUTPUT_FOLDER "/afs/ir.stanford.edu/users/a/k/akma327/stats205/midterm-project/metastocks/data/historical-data/1-basic-materials"
# python historicalStockScraper.py $TICKER_SYMBOL_LIST $OUTPUT_FOLDER 1-1-2000
"""

K_MIN_ARG = 4


def calcDailyDataForAllStocks(OUTPUT_FOLDER, symbols, start, end):
	for symbol in symbols:
		try:
			print("Stock Info For: " + str(symbol))
			stock_info_from_google = web.DataReader("%s" %symbol, 'google', start, end)
			stock_info_from_google.to_csv(OUTPUT_FOLDER + "/%s_from_google.csv" %symbol)
		except:
			print(symbol + " stock extraction failed")
			continue 


if __name__ == "__main__":
	if(len(sys.argv) < K_MIN_ARG):
		print(USAGE_STR)
		exit(1)
	TICKER_LIST = sys.argv[1]
	OUTPUT_FOLDER = sys.argv[2]
	BEG_DATE = sys.argv[3]
	END_DATE = None
	if(len(sys.argv) == 5):
		END_DATE = sys.argv[4]
	symbols = parseTickerList(TICKER_LIST)
	start = parseDate(BEG_DATE)
	end = parseDate(END_DATE)
	calcDailyDataForAllStocks(OUTPUT_FOLDER, symbols, start, end)







