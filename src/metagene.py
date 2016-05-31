# metagene.py 

import os
import sys
import glob 
import csv
import collections
import numpy as np
import datetime as dt
import math

USAGE_STR = """
# Purpose 
# Given a folder of historical stock data, generate a metagene file that summarizes
# multiple stock trajectories. 

# Usage 
# python metagene.py <AGGREGATE_FOLDER_PATH> <MARKET_CAP_FILE> <OUTPUT_FILE> <START_DATE> <END_DATE> <ONE_DATE>

# Arguments 
# <AGGREGATE_FOLDER_PATH> Path to the folder aggregating all the daily stock data for 
# the stocks of interest. 
# <MARKET_CAP_FILE> Path to the file that has all market cap data
# <OUTPUT_FILE> Absolute path to the output metagene file. 
# <START_DATE> Start date of metagene, in form YYYYMMDD
# <END_DATE> End date of metagene, in form YYYYMMDD
# <ONE_DATE> Date where all stocks should be normalized to 1, in form YYYYMMDD

# Example
# python metagene.py ../data/historical-data/6-industrial-goods/ ../data/marketcaps.csv ../data/metagene_output/6-metagene.txt 20080101 20151231 20090101

"""

METAGENE_FILE_HEADER = "Date,Open,High,Low,Close,Volume\n"
DATES = [2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008]
WINDOW = 10

def getMarketCap(year, mktcap):
	if year in mktcap and mktcap[year] != "NA": return mktcap[year]
	
	# if the year is out of bounds
	if year < 2008: return getMarketCap(2008, mktcap)
	elif year > 2015: return getMarketCap(2015, mktcap)
	
	# if the year is within bounds
	i = DATES.index(year)
	for j in range(i)[::-1]:  # iterate backwards (forwards in time)
		cap = mktcap[DATES[j]]
		if cap != "NA": return cap
	for j in range(i, len(DATES)):  # iterate forwards (backwards in time)
		cap = mktcap[DATES[j]]
		if cap != "NA": return cap		

# Process a single stock time series file 
def processStockInfo(stock_file, mktcap, START, END, ONE):
	dateToInfo = {}
	with open(stock_file, 'r') as f:
		normalizing_prices = []
		for line in f: 
			if("Date" in line or line == "\n"): continue
			linfo = line.split(",")
			if('' in linfo): continue 
			
			datearr = linfo[0].split('-')
			date = dt.date(int(datearr[0]), int(datearr[1]), int(datearr[2]))
			if date < START or date > END: continue
			
			closeprice = float(linfo[4]) 		
			if math.fabs((date - ONE).days) < 3: normalizing_prices.append(closeprice)
			
			cap = getMarketCap(date.year, mktcap)
			dateToInfo[date] = [closeprice, cap]
		
		# normalize
		if normalizing_prices == []: return {}  # cannot find a date close enough to normalize by
		norm_price = np.mean(normalizing_prices)
		for d in dateToInfo:
			dateToInfo[d][0] /= norm_price
			
	return dateToInfo


# Average stocks over all time points
def averageStockInfo(stock_to_dict):
	averaged_stocks = collections.defaultdict(lambda: ([], []))  # date --> ([prices], [caps])
	for stock in stock_to_dict:
		for d in stock_to_dict[stock]:
			averaged_stocks[d.isoformat()][0].append(stock_to_dict[stock][d][0])
			averaged_stocks[d.isoformat()][1].append(stock_to_dict[stock][d][1])
		
	weighted = {}
	unweighted = {}
	for d in averaged_stocks:
		prices = averaged_stocks[d][0]
		caps = averaged_stocks[d][1]
		if len(prices) < 2: continue
		unweighted[d] = np.mean(prices)		
		weighted[d] = np.inner(prices, caps)/sum(caps)
	return (weighted, unweighted)

def readMarketCapFile(fn):
	stocks_to_mktcap = collections.defaultdict(lambda: {})
	with open(fn, 'r') as ifile:
		reader = csv.reader(ifile)
		reader.next()
		for row in reader:
			all_na = True
			for i in range(len(DATES)):			
				try: 
					cap = float(row[2+i].replace(',', ''))
					all_na = False
				except:
					cap = "NA"
				stocks_to_mktcap[row[0]][DATES[i]] = cap
			if all_na: del stocks_to_mktcap[row[0]]
		
	return stocks_to_mktcap	
	
def metagene(AGGREGATE_FOLDER_PATH, MARKET_CAP_FILE, OUTPUT_FILE, START, END, ONE):
	# Read in files
	mktcaps = readMarketCapFile(MARKET_CAP_FILE)
	stock_files = glob.glob(AGGREGATE_FOLDER_PATH + "/*")

	# Get normalized data for each stock over the time period
	stock_to_dict = {}
	for stock_file in stock_files:
		stock = os.path.basename(stock_file).replace("_from_google.csv", "")
		if stock not in mktcaps: 
			#print "{} not in market caps list".format(stock)
			continue
		print stock
		stock_to_dict[stock] = processStockInfo(stock_file, mktcaps[stock], START, END, ONE)
	
	# Make weighted and unweighted metagenes
	(weighted, unweighted) = averageStockInfo(stock_to_dict)

	with open(OUTPUT_FILE, 'w') as ofile:
		writer = csv.writer(ofile)
		row1 = ['date']
		row1.extend(sorted(weighted.keys()))
		writer.writerow(row1)
		
		row2 = ['weighted']
		nums = [weighted[x] for x in sorted(weighted.keys())]
		row2.extend(nums)
		writer.writerow(row2)

		row3 = ['unweighted']
		nums = [unweighted[x] for x in sorted(weighted.keys())]
		row3.extend(nums)
		writer.writerow(row3)
		
def process_date(x, prefix):
	if len(x) != 8: 
		print "Date format incorrect for {}".format(x)
		exit(1)
	d = dt.date(int(x[:4]), int(x[4:6]), int(x[6:8]))	
	print "{} date: {}".format(prefix, d)
	return d
	
if __name__ == "__main__":
	AGGREGATE_FOLDER_PATH = sys.argv[1]
	MARKET_CAP_FILE = sys.argv[2]
	OUTPUT_FILE = sys.argv[3]
	START = process_date(sys.argv[4], "Start")
	END = process_date(sys.argv[5], "End")
	ONE = process_date(sys.argv[6], "Norm")
	if ONE < START or ONE > END:
		print "Normalization date is outside the start-end range."
		exit(1)
		
	metagene(AGGREGATE_FOLDER_PATH, MARKET_CAP_FILE, OUTPUT_FILE, START, END, ONE)



