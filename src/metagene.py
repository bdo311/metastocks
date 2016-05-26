# metagene.py 

import os
import sys
import glob 

USAGE_STR = """
# Purpose 
# Given a folder of historical stock data, generate a metagene file that summarizes
# multiple stock trajectories. 

# Usage 
# python metagene.py <AGGREGATE_FOLDER_PATH> <OUTPUT_FILE>

# Arguments 
# <AGGREGATE_FOLDER_PATH> Path to the folder aggregating all the daily stock data for 
# the stocks of interest. 
# <OUTPUT_FILE> Absolute path to the output metagene file. 

# Example
# setenv AGGREGATE_FOLDER_PATH "/afs/ir.stanford.edu/users/a/k/akma327/stats205/midterm-project/metastocks/data/historical-data/tech"
# setenv OUTPUT_FILE "/afs/ir.stanford.edu/users/a/k/akma327/stats205/midterm-project/metastocks/data/metagene-output/tech-metagene.txt"
# python metagene.py $AGGREGATE_FOLDER_PATH $OUTPUT_FILE

"""

METAGENE_FILE_HEADER = "Date,Open,High,Low,Close,Volume\n"

# Process a single stock time series file 
def processStockInfo(date_to_stockinfo_dict, stock_file):
	print(stock_file)
	f = open(stock_file, 'r')
	for line in f: 
		if("Date" in line or line == "\n"): continue
		linfo = line.split(",")
		if('' in linfo): continue 
		Date, Open, High, Low, Close, Volume = linfo[0], float(linfo[1]), float(linfo[2]), float(linfo[3]), float(linfo[4]), int(linfo[5].strip())
		key = (Open, High, Low, Close, Volume)
		if(Date not in date_to_stockinfo_dict):
			date_to_stockinfo_dict[Date] = [key]
		else:
			date_to_stockinfo_dict[Date].append(key)

def avgStockStats(stock_info_list):
	Open, High, Low, Close, Volume = [0]*5
	nStocks = len(stock_info_list)
	for s in stock_info_list:
		Open += s[0]
		High += s[1]
		Low += s[2]
		Close += s[3]
		Volume += s[4]
	Open /= nStocks
	High /= nStocks 
	Low /= nStocks
	Close /= nStocks
	Volume /= nStocks
	return (str(round(Open,2)), str(round(High,2)), str(round(Low,2)), str(round(Close,2)), str(Volume))


# Average stocks for a given time point 
def averageStockInfo(date_to_stockinfo_dict):
	averageStockInfo = []
	for key in sorted(date_to_stockinfo_dict.keys()):
		stock_info_list = date_to_stockinfo_dict[key]
		avgStats = avgStockStats(stock_info_list)
		averageStockInfo.append((key, avgStats))
	return averageStockInfo


def metagene(AGGREGATE_FOLDER_PATH, OUTPUT_FILE):
	fw = open(OUTPUT_FILE, 'w')
	fw.write(METAGENE_FILE_HEADER)
	date_to_stockinfo_dict = {}
	stock_files = glob.glob(AGGREGATE_FOLDER_PATH + "/*")
	for stock_file in stock_files:
		processStockInfo(date_to_stockinfo_dict, stock_file)
	averagedStockInfo = averageStockInfo(date_to_stockinfo_dict)
	for s in averagedStockInfo:
		fw.write(s[0] + "," + s[1][0] + "," + s[1][1] + "," + s[1][2] + "," + s[1][3] + "," + s[1][4] + "\n")


if __name__ == "__main__":
	AGGREGATE_FOLDER_PATH = sys.argv[1]
	OUTPUT_FILE = sys.argv[2]
	metagene(AGGREGATE_FOLDER_PATH, OUTPUT_FILE)



