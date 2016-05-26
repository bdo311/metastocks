# stockTimeSeriesView.py 

import os 
import sys
import csv 
import numpy as np
import matplotlib.pyplot as plt
from utils import *

USAGE_STR = """
# Purpose 
# Plot time series data regarding a stock's open, close, high, low, and volume metric

# Usage 
# python stockTimeSeriesView.py <STOCK_TIMESERIES_DATA>

# Arguments
# <STOCK_TIMESERIES_DATA> Absolute path to the timeseries data for either a single stock or
# metagene summary of multiple stocks 

# Example 
# python stockTimeSeriesView.py /afs/ir.stanford.edu/users/a/k/akma327/stats205/midterm-project/metastocks/data/metagene-output/tech-metagene.txt

"""

def parseDate1(date):
	date_info = date.split("-")
	year, month, day = int(date_info[0]), int(date_info[1]), int(date_info[2])
	return datetime(year, month, day)

def plotStockData(STOCK_TIMESERIES_DATA):
	with open(STOCK_TIMESERIES_DATA) as f:
		reader = csv.reader(f, delimiter=",")
		d = list(reader)
	darr = np.array(d)
	time_stamps = list(darr[:,0][1:])
	date_vals = [parseDate1(d) for d in time_stamps]
	open_vals = list(darr[:,1][1:])
	plt.plot(date_vals, open_vals)
	plt.show()


def dummy():
	d1 = datetime(2000,1,1)
	d2 = datetime(2000,1,20)
	d3 = datetime(2000,2,10)
	dates = [d1,d2,d3]
	yvals = [30,400,50]
	plt.plot(dates,yvals)
	plt.show()



if __name__ == "__main__":
	STOCK_TIMESERIES_DATA = sys.argv[1]
	plotStockData(STOCK_TIMESERIES_DATA)
	# dummy()
