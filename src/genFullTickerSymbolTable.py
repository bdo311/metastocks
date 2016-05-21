# genFullTickerSymbolTable.py 

USAGE_STR="""
# USAGE:
# python genFullTickerSymbolTable.py ../data/ticker-symbols.csv ../data/ticker-lists/master-ticker-list.txt
"""
K_MIN_ARG = 3

import sys 

# process ticker_symbols_csv 
def process_ticker_symbols(ticker_symbols_csv, output_path):
	f = open(ticker_symbols_csv, 'r')
	fw = open(output_path, 'w')
	for line in f:
		if("#" in line or line == "\n"): continue
		else:
			ticker_symbol = line.split(",")[0]
			fw.write(ticker_symbol + "\n")


if __name__ == "__main__":
	if(len(sys.argv)<K_MIN_ARG):
		print(USAGE_STR)
		exit(1)
	ticker_symbols_csv = sys.argv[1]
	output_path = sys.argv[2]
	process_ticker_symbols(ticker_symbols_csv, output_path)
