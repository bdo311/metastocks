# metagene.py 

import os
import sys
import glob 
import csv
import collections
import numpy as np
import datetime as dt
import pandas as pd
import math

USAGE_STR = """
# Purpose 
# Given a folder of historical stock data, generate a metagene file that summarizes
# multiple stock trajectories. 

# Usage 
# python metagene.py <AGGREGATE_FOLDER_PATH> <MARKET_CAP_FILE> <OUTPUT_FILE> <START_DATE> <END_DATE> <ONE_DATE> <USAGE_FLAG>

# Arguments 
# <AGGREGATE_FOLDER_PATH> Path to the folder aggregating all the daily stock data for 
# the stocks of interest. 
# <MARKET_CAP_FILE> Path to the file that has all market cap data, or "none" if no market cap data
# <OUTPUT_FILE> Absolute path to the output metagene file
# <START_DATE> Start date of metagene, in form YYYYMMDD
# <END_DATE> End date of metagene, in form YYYYMMDD
# <ONE_DATE> Date where all stocks should be normalized to 1, in form YYYYMMDD
# <USAGE_FLAG> 
	-metagene If user wants to compute metagene 
	-summary If user wants to compute stock to date summary table for all the market values 

# Example - Compute Metagene
python metagene.py ../data/historical-data/6-industrial-goods/ ../data/marketcaps.csv ../data/metagene_output/6-metagene.txt 20080101 20151231 20090101 -metagene

# Example - Compute Frequency Summary Table 
python metagene.py ../data/historical-data/6-industrial-goods/ ../data/marketcaps.csv ../data/metagene_output/6-metagene.txt 20080101 20151231 20090101 -summary

"""

METAGENE_FILE_HEADER = "Date,Open,High,Low,Close,Volume\n"
DATES = [2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008]
WINDOW = 10

def createDirectory(OUTPUT_FILE):
	directory = os.path.dirname(OUTPUT_FILE)
	if not os.path.exists(directory):
		os.makedirs(directory)

# Generate write file descriptor 
def genWriteDescriptor(OUTPUT_FILE):
	createDirectory(OUTPUT_FILE)
	return open(OUTPUT_FILE, 'w')

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
def processStockInfo(stock_file, do_mktcap, mktcap, START, END, ONE):
	dateToInfo = {} # {date: (value, market cap)}
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
			
			if do_mktcap:
				cap = getMarketCap(date.year, mktcap)
				dateToInfo[date] = [closeprice, cap]
			else:
				dateToInfo[date] = [closeprice, 1]
		
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
		unweighted[d] = round(np.mean(prices),4)
		weighted[d] = round(np.inner(prices, caps)/sum(caps),4)
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
	
def write_row(writer, name, data):
	row = [name]
	row.extend(data)
	writer.writerow(row)
	
def write_metagene(weighted, unweighted, OUTPUT_FILE, resample):
	ofile = genWriteDescriptor(OUTPUT_FILE)
	writer = csv.writer(ofile)
	
	write_row(writer, 'date', sorted(weighted.keys()))
	write_row(writer, 'weighted', [weighted[x] for x in sorted(weighted.keys())])
	write_row(writer, 'unweighted', [unweighted[x] for x in sorted(weighted.keys())])
	
	if resample: 
		return (ofile, writer)
	else:
		ofile.close()
		return 0

def write_metagene_resample(weighted, unweighted, resampled_weighted, resampled_unweighted, OUTPUT_FILE, resample):
	(ofile, writer) = write_metagene(weighted, unweighted, OUTPUT_FILE, resample)
	
	w5 = []
	w50 = []
	w95 = []
	uw5 = []
	uw50 = []
	uw95 = []
	
	for d in sorted(weighted.keys()):
		w = sorted([resampled_weighted[i][d] for i in resampled_weighted])
		w5.append(w[4])
		w50.append(w[49])
		w95.append(w[94])
		uw = sorted([resampled_unweighted[i][d] for i in resampled_unweighted])
		uw5.append(uw[4])
		uw50.append(uw[49])
		uw95.append(uw[94])	
		
	write_row(writer, "weighted_5pct", w5)
	write_row(writer, "weighted_50pct", w50)
	write_row(writer, "weighted_95pct", w95)
	write_row(writer, "unweighted_5pct", uw5)
	write_row(writer, "unweighted_50pct", uw50)
	write_row(writer, "unweighted_95pct", uw95)
	
		
def metagene(AGGREGATE_FOLDER_PATH, MARKET_CAP_FILE, OUTPUT_FILE, START, END, ONE, USAGE_FLAG, resample=True):
	# Read in files
	do_mktcap = True
	if MARKET_CAP_FILE != "none":
		mktcaps = readMarketCapFile(MARKET_CAP_FILE)
	else:
		do_mktcap = False
		mktcaps = collections.defaultdict(lambda: 0)
	stock_files = glob.glob(AGGREGATE_FOLDER_PATH + "/*")

	# Get normalized data for each stock over the time period
	stock_to_dict = {}
	for stock_file in stock_files:
		stock = os.path.basename(stock_file).replace("_from_google.csv", "")
		if do_mktcap and stock not in mktcaps: 
			#print "{} not in market caps list".format(stock)
			continue
		print stock
		stock_to_dict[stock] = processStockInfo(stock_file, do_mktcap, mktcaps[stock], START, END, ONE)
	
	if (USAGE_FLAG == '-summary'): return stock_to_dict
	
	# Make weighted and unweighted metagenes, and resample if necessary
	(weighted, unweighted) = averageStockInfo(stock_to_dict)

	if not resample:
		write_metagene(weighted, unweighted, OUTPUT_FILE, resample)
	else:
		resampled_weighted = {}
		resampled_unweighted = {}
		for i in range(100):
			if i % 10 == 0: print "Resample iteration {}".format(i)
			res_keys = np.random.choice(stock_to_dict.keys(), len(stock_to_dict.keys()), replace=True)
			res_sample_to_dict = {stock: stock_to_dict[stock] for stock in res_keys}
			(resampled_weighted[i], resampled_unweighted[i]) = averageStockInfo(res_sample_to_dict)
	write_metagene_resample(weighted, unweighted, resampled_weighted, resampled_unweighted, OUTPUT_FILE, resample)

			
def process_date(x, prefix):
	if len(x) != 8: 
		print "Date format incorrect for {}".format(x)
		exit(1)
	d = dt.date(int(x[:4]), int(x[4:6]), int(x[6:8]))	
	print "{} date: {}".format(prefix, d)
	return d


# CODE FOR COMPUTING FREQUENCY TABLE BETWEEN STOCKS AND DATES 

# Generate a sorted union of all times over all the stocks 
def unionizeDates(stock_to_dict):
	date_union = []
	for stock in stock_to_dict:
		date_union += stock_to_dict[stock].keys()
	return sorted(list(set(date_union)))


# Get the stock values for single stock 
def getStockValues(stock_to_dict, date_union, stock):
	date_to_val_dict = stock_to_dict[stock]
	date_vals = []
	for date in date_union:
		if(date in date_to_val_dict):
			date_vals.append(str(round(date_to_val_dict[date][0],4)))
		else:
			date_vals.append(str(float(0)))
	return date_vals

# Generate tab delimited table where rows are stocks and columns are time points
# cell entries represent normalized market value. 
def genStockToTimepointTable(stock_to_dict, OUTPUT_FILE):
	f = genWriteDescriptor(OUTPUT_FILE)
	all_stocks = stock_to_dict.keys() 
	date_union = unionizeDates(stock_to_dict)
	all_dates = [str(t) for t in date_union]
	header = "Stocks/Dates\t" + "\t".join(all_dates) + "\n"
	f.write(header)
	for stock in all_stocks:
		row_info = stock + "\t" + "\t".join(getStockValues(stock_to_dict, date_union, stock)) + "\n"
		f.write(row_info)



if __name__ == "__main__":
	AGGREGATE_FOLDER_PATH = sys.argv[1]
	MARKET_CAP_FILE = sys.argv[2]
	OUTPUT_FILE = sys.argv[3]
	START = process_date(sys.argv[4], "Start")
	END = process_date(sys.argv[5], "End")
	ONE = process_date(sys.argv[6], "Norm")
	USAGE_FLAG = sys.argv[7]
	if ONE < START or ONE > END:
		print "Normalization date is outside the start-end range."
		exit(1)
		
	stock_to_dict = metagene(AGGREGATE_FOLDER_PATH, MARKET_CAP_FILE, OUTPUT_FILE, START, END, ONE, USAGE_FLAG)
	if(USAGE_FLAG == "-summary"):
		genStockToTimepointTable(stock_to_dict, OUTPUT_FILE)



