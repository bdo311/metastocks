# whitneyHoustonTest.py 

import os
import sys 
import csv 
import numpy as np 
import scipy
from scipy import stats 
from datetime import datetime 
import datetime 
from utils import *

USAGE_STR = """
# Purpose 
# Perform Mann Whitney U test upon two stock vs timepoint tables. 
# We want to determine whether two sectors are significantly different 
# between a START and END date. Need at least two stock frequency table 
# to compare but can potentially extend to more 

# Usage 
# python whitneyHoustonTest.py <START_DATE> <END_DATE> <STOCK_TABLE1> <STOCK_TABLE2> ...

# Arguments 
# <START_DATE> Start date to query the column
# <END_DATE> End date to query the column
# <STOCK_TABLE1> Absolute path to the stock frequency table 
# <STOCK_TABLE2> Absolute path to second stock frequency table 

# Example 
START_DATE="2008-01-02"
END_DATE="2015-12-31"
STOCK_TABLE1="/scratch/PI/rondror/akma327/MetaStocks/metastocks/data/stock_freq_summary_table/no-market-cap/1-basic-materials-no-cap-metagene.txt"
STOCK_TABLE2="/scratch/PI/rondror/akma327/MetaStocks/metastocks/data/stock_freq_summary_table/no-market-cap/2-conglomerates-no-cap-metagene.txt"
python whitneyHoustonTest.py $START_DATE $END_DATE $STOCK_TABLE1 $STOCK_TABLE2

"""

K_MIN_ARG = 5

# Get command line argument 
def getCommandLineArguments():
	if(len(sys.argv) < K_MIN_ARG):
		print(USAGE_STR)
		exit(1)
	START_DATE = sys.argv[1]
	END_DATE = sys.argv[2]
	STOCK_TABLE1 = sys.argv[3]
	STOCK_TABLE2 = sys.argv[4]
	return START_DATE, END_DATE, STOCK_TABLE1, STOCK_TABLE2


# Get list of all column indices that fall within the start and end date
def inRangeTimeIndices(time_labels, START_DATE, END_DATE):
	in_range_time_indices = []
	beg, end = parseDate2(START_DATE), parseDate2(END_DATE)
	for index, date in enumerate(time_labels):
		if(index == 0): continue 
		curr_date = parseDate2(date)
		if(curr_date >= beg and curr_date <= end):
			in_range_time_indices.append(index)
	return in_range_time_indices


def calcMedian(stock_row, in_range_time_indices):
	freq_vals = [float(stock_row[i]) for i in in_range_time_indices]
	return np.median(freq_vals)

# Generate list of median values for each stock upon the frequencies that fall within
# the date range 
def medianStatistic(START_DATE, END_DATE, STOCK_TABLE):
	median_statistic = []
	with open(STOCK_TABLE) as f: 
		reader = csv.reader(f, delimiter='\t')
		d = list(reader)
	darr = np.array(d)
	time_labels = darr[0,:]
	in_range_time_indices = inRangeTimeIndices(time_labels, START_DATE, END_DATE)
	stock_rows = darr[1:]
	for stock_row in stock_rows:
		median_statistic.append(round(calcMedian(stock_row, in_range_time_indices),4))
	return median_statistic


# Whitney U Test Driver
def whitneyUTestDriver(START_DATE, END_DATE, STOCK_TABLE1, STOCK_TABLE2):
	median_statistic_1 = medianStatistic(START_DATE, END_DATE, STOCK_TABLE1)
	median_statistic_2 = medianStatistic(START_DATE, END_DATE, STOCK_TABLE2)
	statistic, pvalue = scipy.stats.mannwhitneyu(median_statistic_1, median_statistic_2)
	print(statistic, pvalue)


if __name__ == "__main__":
	START_DATE, END_DATE, STOCK_TABLE1, STOCK_TABLE2 = getCommandLineArguments()
	whitneyUTestDriver(START_DATE, END_DATE, STOCK_TABLE1, STOCK_TABLE2)

	



