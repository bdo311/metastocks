
import os 
import sys
from utils import *
from datetime import datetime
# import pandas as pd
# import pandas_datareader.data as web

USAGE_STR = """
# Purpose
# For a list of ticker symbols, generate historical stock data at the daily granularity 

# Usage 
# python historicalStockScraper.py <TICKER_SYMBOL_LIST> 

# Arguments
# <TICKER_SYMBOL_LIST> List of acronyms for the stocks of interest delimited by new line 

# Example:
# TICKER_LIST="/afs/ir.stanford.edu/users/a/k/akma327/stats205/midterm-project/metastocks/data/ticker-lists/tech-ticker-list.txt"
# python historicalStockScraper.py $TICKER_LIST

"""

K_MIN_ARG = 2

# Specify Date Range
start = datetime(2003, 1, 1)
end = datetime.today()

# # Specify symbol
# symbol = 'AAPL'

# aapl_from_google = web.DataReader("%s" % symbol, 'google', start, end)
# aapl_from_yahoo = web.DataReader("%s" % symbol, 'yahoo', start, end)

# aapl_from_google.to_csv('../data/historical-data/%s_from_google.csv' % symbol)
# aapl_from_yahoo.to_csv('../data/historical-data/%s_from_yahoo.csv' % symbol)


def calcDailyDataForAllStocks(symbols):
	for symbol in symbols:
		print("Stock Info For: " + str(symbol))
		stock_info_from_google = web.DataReader("%s" %symbol, 'google', start, end)
		stock_info_from_google.to_csv('../data/historical-data/tech/%s_from_google.csv' %symbol)





if __name__ == "__main__":
	TICKER_LIST = sys.argv[1]
	symbols = parseTickerList(TICKER_LIST)
	print(symbols)
	# calcDailyDataForAllStocks(symbols)







